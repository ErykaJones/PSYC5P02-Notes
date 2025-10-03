#- important to know the size of screen to ensure the size of stimuli is controlled for when doing experiment
#- degrees of visual angle - important for ERP research
#- pip - install in python function 
#- knowing the screen of the device you will be displaying experiment is on 

from psychopy import visual, core
win = visual.Window([400,400])
message = visual.TextStim(win, text ='hello')
message.autodraw = True #automatically draw every frame
win.flip()
core.wait(2.0)
message.text = 'world' #change properties of existing stim
win.flip()
core.wait(2.0)

#draw is drawing a stimuli - we used text but you can use a square or other shapes - and you want to name it (declare where it's displayed, then the properties of the stimuli)
#autodraw important for drawing every frame so in this instance it was drawing on the screen until we told it to go away (you may want this to change on every frame)
#win.flip - flips the stimuli to the screen (to display it)
#win.flip is super important where it's located in the code especially if you're using EEG (you may want the win.flip to be after everything loads in as to control for time it takes to run commands)
#core.wait - delay (how long you want the stimulus displayed)
#simplest way to control time for stimulus presentation
#you can use a loop though if you need a key response 

from psychopy import visual, event, core, data
win = visual.window ([1960, 1080], fullscr=False, units = 'prix')
fixation = visual.Circle(win, size = 5, linecolor = 'white', fillColor = 'lightGrey')
probe = visual.GratingStim(win, size = 80, #'size' is 3xSD for gauss, 
pos = [300, 0], tex = None, mask = 'gauss', color = 'green')
cue = visual.ShapeStim (win, vertices = [[-30, -20], [-30, 20], [30,0]], linecolor = 'red', fillcolor = 'salmon')
info = {} #a dictionary
info['fixtime'] = 0.5 #seconds
info['cueTime'] = 0.2 
info['probeTime'] = 0.2 

#run one trial
fixation.draw()
win.flip()
core.wait(info['fixTime'])

cue.draw()
win.flip()
core.wait(info['cuetime'])

fixation.draw()
probe.draw()
win.flip()
core.wait(info['probeTime'])

#randomizing - need to refer to the class notes because I was troubleshooting my computer


#now we are inserting a clock that allows us to get a time stamp and get time between one thing and another
#we will want to reset a clock after the probe for the posner task
#then clear screen and instead of a core.wait we are going to wait on a key response 
#you want to assign a key respones to a variable 
# and also the clock output as a way to measure reaction time 
#you can calculate accuracy by using an if statement
#w = write, x = open, a = append can be used to determine how you're opening a file to save your responses
#you can add the fileID.write('format', vars) to your code to put new info in as the experiment goes along 
#done line by line 
#can open it at the beginning (before the loop begins) then close it at the end of the experiment (after the loop)
#writing to the file can be done in the loop 
