from psychopy import visual, event, core, data, gui
from psychopy.tools.filetools import fromFile
import random
import numpy as np

# Experiment setup
expName = 'VisualSearch' 
dlg = gui.Dlg()
dlg.addField('SubjectID:')
dlg.addField('Trials Per Cond:')
ok_data = dlg.show()
if not dlg.OK:
    core.quit()

sub_ID = ok_data[0] 
trials = int(dlg.data[1])
fileName = sub_ID + "_" + expName
dataFile = open(fileName + '.csv', 'w')
dataFile.write('SetSize,TP, RT, Correct, Missed\n')

#Both the dialogue box and file work as expected.

win = visual.Window([1920, 1080], fullscr=False, units='pix')

# Stimuli and conditions
conditions = [5, 8, 12]
stim_size = 30
T = visual.ImageStim(win, 'Stimuli/T.png', size=stim_size) #They could probably remove the 'Stimuli/' because unless you're also ensuring that everyone has a directory called 'Stimuli', it will give you an error. Additionally, you could just put the .png in a folder with this code and the code will run without issue right after someone downloads the whole folder. 
L = visual.ImageStim(win, 'Stimuli/L.png', size=stim_size) 

# Draw stimuli at random positions/orientations
def pos_and_ori(target, distract, samp_size): #Good idea to put both pos and ori in one function
    samplelist = list(range(-180, 180, 25)) 
    x = random.sample(samplelist, samp_size) 
    y = random.sample(samplelist, samp_size)
    for n in range(0, samp_size - 1):
        orientations = [0, 90, 180, 270]
        orin = random.choice(orientations)
        distract.ori = orin
        distract.pos = (x[n], y[n])
        distract.draw()
    for n in range(samp_size - 1, samp_size): #for some of the trials the stimuli overlap slightly, wonder if there's a way to ensure they never overlap? They also overlap the feedback at some points. I wonder if there's a way to block the stimuli from overlapping the feedback as well. Maybe setting coordinates around the center of the screen to avoid the feedback?
        target.pos = (x[n], y[n])
        target.draw()
    return distract, target

# Determine if target is present on a given trial
def targ_pres(trial_list, total_trials, distract, target, condition_index):
    pres_or_not = random.choice(trial_list)
    trial_list.remove(pres_or_not)
    if pres_or_not <= np.median(total_trials): #Calling np.median is interesting here, I wonder why they didn't just use random.
        targ_there = 0
        stimuli = pos_and_ori(distract, distract, condition)
    else:
        targ_there = 1
        stimuli = pos_and_ori(target, distract, condition)
    return targ_there, stimuli

# Get response and RT
def KeyGet(trial_duration=2.0, rt=None, resp=None): #This function could probably be named something different because this is quite close to the getKeys function that already exists. I would've called it ResponseKeys or something similar to that just to avoid getting confused and creating more work. 
    startTime = core.getTime()
    while core.getTime() - startTime < trial_duration and resp is None:
        keys = event.getKeys(keyList=['a', 'd', 'escape'])
        if keys:
            key = keys[0]
            rt = core.getTime() - startTime
            if key == 'a':
                resp = 'a'
                break
            elif key == 'd':
                resp = 'd'
                break
            elif key == 'escape':
                core.quit()
        core.wait(0.01)
    if resp is None:
        resp = 'no_response'
        rt = 999
    return resp, rt

# Evaluate response accuracy and feedback
def Response(resp, rt, targ_there):
    if resp == 'd' and targ_there == 1:
        corr = 1
        feedback = 'Correct!'
        response_time = round(rt, 2)
    elif resp == 'a' and targ_there == 1:
        corr = 0
        feedback = 'Incorrect!'
        response_time = round(rt, 2)
    elif resp == 'a' and targ_there == 0:
        corr = 1
        feedback = 'Correct!'
        response_time = round(rt, 2)
    elif resp == 'd' and targ_there == 0:
        corr = 0
        feedback = 'Incorrect'
        response_time = round(rt, 2)
    elif resp == 'no_response':
        corr = 0
        feedback = 'No Response'
        response_time = 'NA'
    return corr, feedback, response_time

# I like the use of functions here, gives me an idea of the ways I could use functions in order to make my code more efficient. 

# Instructions
welcome = '''' 
Welcome to the Visual Search Task

You will see an assortment of shapes in different positions and orientations.
Most will be 'L' shapes, but some may contain a 'T' shape.

If the T is present, press 'd'.
If the T is absent, press 'a'.

Respond quickly!
Press SPACE to begin 5 practice trials.
'''
#There is an extra single quotation mark at the start of the instructions is not matched to the ones at the end. There's four on the top and three at the bottom. This means that one quotation mark appears on the screen above the instructions. 
instructions = visual.TextStim(win, color='white', text=welcome, units='norm', height=0.05)
instructions.draw()
win.flip()
keys = event.waitKeys(keyList=['space'])
core.wait(0.25)

# Practice trials
practice_trials = range(1, 6) #Trial Handler would've also been helpful here. It would allow you to insert a condition list and number of repeats of each condition. This allows you to cycle through each condition for x number of times. It can also randomly show each condition in order to randomize set size condition.  
for condition in conditions: 
    appear = list(practice_trials)
    for prac_trials in practice_trials:
        targ_there, stimuli = targ_pres(appear, practice_trials, L, T, condition)
        resp, rt = KeyGet()
        corr, feedback, response_time = Response(resp, rt, targ_there)
        cor_feedback = visual.TextStim(win, text=feedback, pos=(0, 30), height=40)
        back_rt = visual.TextStim(win, text=response_time, pos=(0, -30), height=40)
        cor_feedback.draw()
        back_rt.draw()
        win.flip()
        core.wait(0.5)

# Main experiment instructions
welcome = ''''
Practice complete! Now for the real trials.

Press SPACE to begin.
'''
#Same problem as the practice trials instructions. The number of quotation marks at the beginning are not matched by the ones at the end. So, when the instructions are drawn, there is a single quotation at the start of them.  
instructions = visual.TextStim(win, color='white', text=welcome, units='pix', height=10) #these instructions were too small, I think it's because the units for the practice trials were set to norm but these are set to pix. So the first instructions were set to take up a certain amount of the window, these instructions were set to be the size of a certain number of pixels. 
instructions.draw()
win.flip()
keys = event.waitKeys(keyList=['space'])
core.wait(0.25)

# Trial setup
total_trials = range(1, trials + 1) #Trial handler would've also been helpful here for the same reasons as the practice trials. 
rt_list, corr_list, miss_rt_list = [], [], []
random.shuffle(conditions)

# Main experiment loop
for condition in conditions:  
    appear = list(total_trials)
    for trial in total_trials:
        targ_there, stimuli = targ_pres(appear, total_trials, L, T, condition)
        resp, rt = KeyGet()
        corr, feedback, response_time = Response(resp, rt, targ_there)
        cor_feedback = visual.TextStim(win, text=feedback, pos=(0, 30), height=40) #This was a better size for the text stim, unit is not specified but size is legible. 
        back_rt = visual.TextStim(win, text=response_time, pos=(0, -30), height=40)
        cor_feedback.draw()
        back_rt.draw()
        win.flip()
        core.wait(0.5)

        if rt != 999: #I learned a lot how to track correct responses from this code, I don't think I would have thought, or known what to do, to track a no - response. 
            rt_list.append(rt)
            miss_rt = 0
            corr_list.append(corr)
        else:
            miss_rt_list.append(1)
            miss_rt = 1
            corr_list.append(0)

        dataFile.write('%i, %i, %.3f, %i, %i\n' % (condition, targ_there, rt, corr, miss_rt))

dataFile.close() #right now the set size is not randomized. Randomizing wasn't part of the instructions per se, but if you wanted to, you could randomize the trials with random (make a list of conditions and shuffle to then choose the set size) or trial handler (you can import condition list and set it to randomly go through experiment conditions).

# Final feedback
average_rt = round(np.mean(rt_list), 2) #This could be put into a function
average_corr = round(np.mean(corr_list), 2)
total_miss = sum(miss_rt_list)

avg_rt_text = f'average rt: {average_rt}' #This could also be put into the function, along with the creation of the text stim and drawing of text stim.
avg_corr_text = f'average correct: {average_corr}'
miss_text = f'no response on {total_miss} trials'
leave_text = 'press SPACE to exit'

cor_avg_back = visual.TextStim(win, text=avg_corr_text, pos=(0, 50), height=20) 
rt_avg_back = visual.TextStim(win, text=avg_rt_text, pos=(0, -10), height=20)
miss_tot_back = visual.TextStim(win, text=miss_text, pos=(0, -35), height=20)
exit_text = visual.TextStim(win, text=leave_text, pos=(0, -100), height=20)

cor_avg_back.draw()
rt_avg_back.draw()
miss_tot_back.draw()
exit_text.draw()

win.flip()
keys = event.waitKeys(keyList=['space'])
win.close()
core.quit()

#Based on the feedback that I also received (and I understand now that it would make the code more efficient), there may be use for a function for the trials themselves so the actual trial loop just consists of calling functions
#I know we didn't learn about trial handler in the class, but that could make it much more efficient when setting up the trials and it would help to randomize the way it displayed each condition. Right now, it's just showing each trial for each condition one right after the other. 
#Finally, there were small things in the size of text stimuli and the quotation marks that appeared before the instructions. There was also the problem that I ran into where stimuli were overlapping each other and in this case, there was some that overlapped the trial feedback. 

#Overall, this worked pretty good and had all the things asked for in the instructions. The only problems I saw were in terms of making the code potentially a little more efficient and the properties of the text stimuli. 
#I enjoyed reading through it because I was able to see how things were applied that I didn't think of or didn't get to with my own assignment.
