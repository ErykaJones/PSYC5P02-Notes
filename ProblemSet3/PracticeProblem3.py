from psychopy import core, event, visual, clock, data, gui
from psychopy.hardware import keyboard
import numpy as np
import random

win =  visual.Window([1536, 864], fullscr=False)

conditions = [{'setsize': 8, 'target' :''},
            {'setsize':12, 'target':''}, 
            {'setsize':16, 'target':''}] #list of conditions for the trial handler to read 

ExpInfo = {} #creating dictionary to store participant number and trials per condition
ExpInfo['participant'] = ''
ExpInfo['Trial Number'] = ''
ExpInfoDlg = gui.DlgFromDict(ExpInfo)
if not ExpInfoDlg.OK:
    core.quit()

orientations = [0, 90, 180, 270] #orientations to randomize
setsize = [7, 11, 15] #set size -1 so I can keep the size constant by adding either the target or another distractor
targets = visual.ImageStim(win, image = 'T.png', pos = (np.random.uniform(-0.8,0.8), np.random.uniform(-0.8,0.8)), size = 0.1) #draw target stimuli


def randomori(distractors, targets): #defining a function to be able to randomize orientations of the stimuli
    distractors.ori = random.choice(orientations)
    targets.ori = random.choice(orientations)

def randompos(distractors, targets): #defining a function to randomize their positions around the screen
    distractors.pos = (np.random.uniform(-0.8,0.8), np.random.uniform(-0.8,0.8))
    targets.pos = (np.random.uniform(-0.8,0.8), np.random.uniform(-0.8,0.8))

rtClock = core.Clock() #call the clock to track reaction time

title = visual.TextStim (win, text = 'Practice Trials', color = 'white') #instructions and the title to tell the participant what trials they are doing and how to do them 
title.draw()
win.flip()
core.wait(2)
instructions = visual.TextStim(win, text = 'For this experiment, you will be shown a series of stimuli. The one that is important to you is the letter T. If you see the letter T on screen, press the Left arrow key. If it is not present, press the Right arrow key. Try your best to search the screen in the time provided. Press the space bar to begin the practice trials', color = 'white')
instructions.draw()
win.flip()
move = event.waitKeys(keyList = 'space') #space bar to begin the practice trials

practice = data.TrialHandler(trialList = 'conditions', nReps = 2, method = random) #number of trials is 5 per condition
for thisTrial in practice:
    distL = [] #empty variable to append to
    x = random.choice(setsize) #randomize the amount of stimuli on screen 
    for i in range(x):
       distractors = visual.ImageStim(win, image = 'L.png', pos = (np.random.uniform(-0.8,0.8), np.random.uniform(-0.8,0.8)), size = 0.1) 
       distL.append(distractors) #loop to draw all the stimuli
    
    for distractors in distL:
        randomori(distractors, targets)
        randompos(distractors, targets)
        if distractors.overlaps(distractors) == True: #this is an attempt to make the stimuli not overlap, don't think it works well. This may be because it's technically comparing it to itself? 
            distractors.setPos = (np.random.uniform(-0.8,0.8), np.random.uniform(-0.8,0.8)),
        distractors.draw() #draw the stimuli from the list 
    y = random.choice([0,1]) #randomizing for the target being displayed 50% of the time 
    tVis = [] #appending to this list so correct answers can be tracked later?
    if y == 1:
        tVis.append(y)
        randomori(distractors, targets) #randomize orientations and positions then draw 
        randompos(distractors, targets)
        if targets.overlaps(distractors) == True:
            targets.setPos = (x+70, y+70) #making sure targets don't overlap distractors, not sure if this works as well. Unsure of how to fix. 
        targets.draw()
    else:#loop to draw another distractor if the target wasn't present 
        randomori(distractors, targets)
        randompos(distractors, targets)
        distractors.draw() 
    win.flip()
    resp = event.getKeys(keyList = ['Left', 'right']) #response keys
    event.waitKeys(maxWait = 2.0) #amount of time before the screen times out 
    
    CorrAnswer = []
    if tVis == 1 and resp == 'left': #tracking the correct answers 
        corr = 1
        corr.append(CorrAnswer)
    elif tVis == 0 and resp == 'right':
        corr = 0
    elif tVis == 0 and resp == 'right':
        corr = 1
        corr.append(CorrAnswer)
    else:
        corr = 0

    
    
#moving to the test trials
Testtitle = visual.TextStim (win, text = 'Test Trials', color = 'white') #instructions and the title to tell the participant what trials they are doing and how to do them 
Testtitle.draw()
win.flip()
core.wait(2)
test = visual.TextStim(win, text = 'The task is the same as in the practice trials. If you see the letter T on screen, press the Left arrow. If you do not see it, press the Right arrow. Press the spacebar to continue.', color='white')
test.draw()
win.flip()
event.waitKeys(keyList = 'space')
win.flip()


trials = data.TrialHandler(trialList = 'conditions', nReps = 5, method = random)
for thisTrial in trials:
    distL = []
    x = random.choice(setsize) #repeating the loops from the practice trials
    for i in range(x):
       distractors = visual.ImageStim(win, image = 'L.png', pos = (np.random.uniform(-0.8,0.8), np.random.uniform(-0.8,0.8)), size = 0.1) 
       distL.append(distractors)
    
    for distractors in distL:
        randomori(distractors, targets)
        randompos(distractors, targets)
        if distractors.overlaps(distractors) == True:
            distractors.setPos = (np.random.uniform(-0.8,0.8), np.random.uniform(-0.8,0.8)),
        distractors.draw()
    y = random.choice([0,1])
    tVis = []
    if y == 1:
        randomori(distractors, targets)
        randompos(distractors, targets)
        if targets.overlaps(distractors) == True:
            targets.setPos = (x+70, y+70)
        tVis.append(y)
        targets.draw()
    else:
        randomori(distractors, targets)
        randompos(distractors, targets)
        distractors.draw()
    win.flip()
    resp = event.getKeys(keyList = ['Left', 'right'])
    event.waitKeys(maxWait = 2.0)
    rt = rtClock.getTime()
    
    score = []
    if tVis == 1 and resp == 'left': #tracking the correct answers 
        corr = 1
        score.append(corr)
    elif tVis == 1 and resp == 'right':
        corr = 0
        score.append(corr)
    elif tVis ==  0 and resp == 'right':
        corr = 1
        score.append(corr)
    else:
        corr = 0
        score.append(corr)
    
    #this an attempt at reporting feedback, it's only showing incorrect. Unsure of how to make it actually work. 
    if score == 1:
        txtFdbkP: visual.TextStim(win, text = 'Correct', color = 'green')
        txtFdbkP.draw()
        win.flip()
    else: 
        txtFdbkN= visual.TextStim(win, text = 'Inorrect', color = 'red')
        txtFdbkN.draw()
        win.flip()
    
#I used the psychopy documentation at psychopy.org to help with this assignment. I also used the available demos to see how they run experiments.abs
#I used the discourse.psychopy.org, which are the forums available for psychopy. I used these mainly to troubleshoot if I could not understand the error I was encountering. 
    
    
    
    
    
    
    


