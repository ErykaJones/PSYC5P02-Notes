from psychopy import visual, core, clock, event, gui, data
from psychopy.hardware import keyboard
import random
import numpy as np
import pandas as pd

win =  visual.Window([1536, 864], fullscr=False)

living = pd.DataFrame(['goose_living.jpg', 'giraffe_living.jpg', 'flamingo_living.jpg', 'camel_living.jpg', 'cockroach_living.jpg']) #setting up a dataframe to store my stimuli, this was easier to use because it's a lot easier to locate things
nonliving = pd.DataFrame(['cabin_nonliving.jpg', 'cake_nonliving.jpg', 'carabiner_nonliving.jpg', 'drum_nonliving.jpg', 'electric_guitar_nonliving.jpg', 
    'cabinet_nonliving.jpg', 'camera_nonliving.jpg', 'headphones_nonliving.jpg', 'fanny-pack_nonliving.jpg', 'dumbell_nonliving.jpg', 'chalkboard_nonliving.jpg', 
    'cd_nonliving.jpg', 'pitcher_nonliving.jpg', 'pearlnecklace_nonliving.jpg', 'ornament_nonliving.jpg', 'margarita_nonliving.jpg', 'loveseat_nonliving.jpg', 'lightbulb_nonliving.jpg',]) #creating a separte dataframe for the nonliving stimuli because it's easier for the randomization of it 

#Create a dataframe consisting of all the above stimuli that will be old for the surprise recognition task
OldStim = pd.DataFrame(['cabin_nonliving.jpg', 'cake_nonliving.jpg', 'carabiner_nonliving.jpg', 'drum_nonliving.jpg', 'electric_guitar_nonliving.jpg', 
    'cabinet_nonliving.jpg','goose_living.jpg', 'camera_nonliving.jpg', 'headphones_nonliving.jpg', 'giraffe_living.jpg',
    'fanny-pack_nonliving.jpg', 'dumbell_nonliving.jpg', 'chalkboard_nonliving.jpg', 
    'cd_nonliving.jpg', 'pitcher_nonliving.jpg', 'pearlnecklace_nonliving.jpg', 
    'ornament_nonliving.jpg', 'margarita_nonliving.jpg', 'loveseat_nonliving.jpg', 'lightbulb_nonliving.jpg','flamingo_living.jpg']) 

#this dataframe consists of stimuli that will be the 'new' stimuli the participant will see in the memory test 
NewStim = pd.DataFrame (['fan_nonliving.jpg', 'alarm_clock_nonliving.jpg', 'peacock_living.jpg', 
    'backpack_nonliving.jpg', 'ballet_slipper_nonliving.jpg', 'antelope_living.jpg', 'bear_living.jpg', 'atm_nonliving.jpg', 
     'canoe_nonliving.jpg', 'bull_living.jpg']) 

#loading in some stimuli that will be used in the sustained attention practice trials (this is for ease and efficiency)
practiceAttn = pd.DataFrame(['kettle_nonliving.jpg', 'jumprope_nonliving.jpg', 'crow_living.jpg', 'cowboy_boot_nonliving.jpg', 'xylophone_nonliving.jpg', 'hockey_stick_nonliving.jpg', 
    'hand_mirror_nonliving.jpg', 'gift_bag_nonliving.jpg', 'grandfather_clock_nonliving.jpg', 'fish_living.jpg'])

#load in some stimuli for the surprise recognition memory task
PracticeMem = pd.DataFrame (['kettle_nonliving.jpg', 'jumprope_nonliving.jpg', 'crow_living.jpg', 'cowboy_boot_nonliving.jpg', 
    'xylophone_nonliving.jpg', 'hockey_stick_nonliving.jpg', 'accordion_nonliving.jpg', 'accent_lamp_nonliving.jpg', 'donkey_living.jpg'])

#These are the variables that I will be passing into functions later
#Specifically to draw the text that acts as a prompt for the participant to respond and stays constant on screen
#They will also be passed in the randomizing function because it will be helpful to keep track of what type of stimuli the participant is seeing 
livingText = 'living' 
nonlivingText = 'nonliving'
OldText = 'Old'
NewText = 'New'


#writing out the instructions now and will be used in the drawing of them before the tasks 
attnInstructions = '''Sustained Attention Task:
    You will see a series of objects presented to you in the middle of the screen. Your job is to identify whether that object is living or nonliving
    
    If the object is LIVING, press j 
    If the object is NONLIVING, press l 
    
    Pay attention and try to respond as fast as you can.
    Press 'space' to begin the task'''
    
memInstructions = ''' Surprise Recognition Task:
    You will now be shown another series of objects presented to you in the middle of the screen. Your job is to identify whether or not you recognize the object from the attention task you just completed.
    
    If the object is one you saw in the memory task, it is OLD and press 'j'
    If the object is new to you, it's NEW and press 'l'
    
    Try to respond as fast as possible. 
    Press 'space' to begin the task'''

SetUpInfo = {} #Set up a dictionary to store participant information
SetUpInfo['Participant Number'] = '' #Store participant number in the dictionary 
dlg = gui.DlgFromDict(SetUpInfo) #Before experiment begins, show a dialogue box that prompts the user to input participant number 
if not dlg.OK: #if okay is not pressed, the program will quit 
    core.quit()

fileName = f"data/{SetUpInfo['Participant Number']}_Attn" #create a file name using the participant ID collected in the dialogue box and the type of task (attention)
#open a data file to track stimuli path, stimuli type, key pressed, reaction time, and if it was correct 
thisExp = data.ExperimentHandler(name= 'Sustained Attention', version = '1.0', extraInfo = SetUpInfo, dataFileName = fileName)

def Practice(practiceAttn): #Function to randomize practice stimuli, assign it to a variable and then draw it, used in both the attention and memory tasks 
    y = visual.ImageStim(win, units = 'pix', size = [200, 150]) #create a visual stimuli
    img_row = practiceAttn.sample(1) #take a random sample from the practice stimuli dataframe 
    index = img_row.index #locate it in the index 
    img = img_row.iloc[0,0] #locate the specific cell for the image path
    practiceAttn.drop(index, inplace = True) #remove the stimulus from the dataframe so there's no repeats 
    y.setImage(img) #set the image path  
    y.draw() #draw the image 

def PracticeTrials(practiceAttn, attnInstructions, livingText, nonlivingText): #function to run the practice trials, it takes the dataframe the stimuli is in, the type of instructions for the specific task, and the text that prompts a response to display on screen for the trials as arguments 
    title = visual.TextStim(win, text = 'Practice Trials', color = 'white', pos = [0.0, 0.9]) #title to let participant know where they are in the experiment 
    instructions = visual.TextStim (win, text = attnInstructions, color = 'white') #instructions 
    instructions.draw() #draw instructions 
    title.draw() #draw title
    win.flip() #show to participant 
    event.waitKeys(keyList = ['space']) #wait for a space bar press before moving on
    event.clearEvents() #clear space bar press before going into the trial loop
    for i in range (5): #five practice trials just to keep things simple for now 
        Practice(practiceAttn) #draw practice stimuli
        ScreenText(livingText, nonlivingText) #draw living and nonliving text
        win.flip() #show to participant 
        event.waitKeys(maxWait = 1.5, keyList = ['j','l']) #wait for a key press, max wait representing the max amount of time a participant will have to respond  
        win.flip() #move to next screen
        fixation() #draw the fixation cross 
        win.flip() #show to the participant 
        core.wait(0.5) #500ms inter trial interval

def drawInstructions(attnInstructions): #function to draw instructions of the test trials, takes a string as an argument (assign your instructions to a variable and pass it into this function)
    title = visual.TextStim(win, text = 'Test Trials', color = 'white', pos = [0.0, 0.9]) #title so the participant knows it's now the test 
    instructions = visual.TextStim (win, text = attnInstructions, color = 'white') #instructions again
    instructions.draw() #draw the instructions 
    title.draw() #draw the title 
    win.flip() #show to participant 
    event.waitKeys(keyList = ['space']) #wait for a space bar press before they move onto the practice trials 
    event.clearEvents() #clear the space bar press before the start of the test trials 
    
def StimRandom (living, nonliving, livingText, nonlivingText): #function to randomize what type of stimuli and which of the stimuli from the dictionary will be presented (takes the the two dataframes as the first two arguments, first dataframe should be the less frequent stimuli and the second should be more frequent. Also takes the text variables that were passed to the screen text function as an easy way of keeping track of stimuli type)
     global stimType #this is so the stimType can be referenced later on in the response function
     x = random.randrange(0, 100, 1) #We want the living stimuli to only appear 10% of the time and nonliving to be the majority, so I set the random in range 1-100 
     y = visual.ImageStim(win, units = 'pix', size = [200, 150]) #assign the properties of the stimuli other than the image path so it is easier to just assign the image path and draw the image later in the loop  
     if x <= 10 and not living.empty: #This will allow us to make sure only 10% of trials will contain a living stimuli and if the dataframe is not empty 
        img_row = living.sample(1) #take a random sample of one row from the living stimuli dataframe
        img = img_row.iloc[0,0] #Locate the row and column of the stimulus path
        index = img_row.index #locate the row, this will be used later
        stimType = livingText #make sure to note what type of stimuli it is for response tracking and the csv(also important for the CSV)
        y.setImage(img) #set the image path so it knows what image to choose
        y.draw() #draw the image
        
        living.drop(index, inplace = True) #this is to remove the row of the stimulus that was just shown so there will be no repeats of stimuli
     elif x > 10 and not nonliving.empty: #most of the stimuli should be nonliving (90% of the time) and making sure that it is not drawing from here if the dataframe is empty
        img_row = nonliving.sample(1) #sample one cell from the dataframe
        img = img_row.iloc[0,0] #locate the sample
        index = img_row.index #keep track of the row it is in
        stimType = nonlivingText #keep track of what type of stimuli for responses and for csv
        y.setImage(img) #set the image based on the path (all stimuli is stored in the dataframe with their image path)
        y.draw() #draw stimulus 
        
        nonliving.drop(index, inplace = True) #same thing here where it will drop the row once it has been used so there is no repeats of stimuli
     else:
        return None #if the conditions above are not met, then return None
     thisExp.addData('stim', img) #add the image path to the csv
     thisExp.addData('stimType', stimType) #add the type of stimulus that was shown to the csv
    
def ScreenText(livingText, nonlivingText): #the text on screen will remain constant through the whole experiment as it is prompting the participant to respond. This function will allow us to draw the onscreen text that stays context and takes strings that are assigned to variables as arguments. 
    screenText1 = visual.TextStim(win, pos = (-0.4, -0.4), units = "norm", color = 'white') #one prompt will sit on the left side of the screen
    screenText1.setText(livingText) #set the text to living, (this will change if you pass another string variable into the function arguments)
    screenText2 = visual.TextStim (win, pos = (0.4, -0.4), units = "norm", color = 'white') #the second prompt will sit on the right side of the screen
    screenText2.setText(nonlivingText) #set the text to nonliving (this will change if you pass another string into the function arguments)
    screenText1.draw() #draw the word living
    screenText2.draw() #draw the word nonliving

def fixation(): #draw a fixation cross, this is so it does not need to be hard coded into the experiment loop
    fixCross = visual.TextStim(win, text = '+', color = 'white') #this is the command to draw the fixation cross, it will be white and in the middle of the screen
    fixCross.draw() #draw the fixation cross

def get_responseAttn (trialDuration = 1.5, rt = None, resp = None): #create a function to track response, it will look at both the key pressed AND whether or not that was the correct response 
    start_time = core.getTime() #start by getting the time 

    keys = event.waitKeys(maxWait = 1.5, keyList=['j', 'l'], timeStamped=True) #create a list of keys, waitKeys means that it will wait for the key to be pressed then move on but it  also has a max wait which is what our max trial duration will be (1.5 seconds)
        
    key = None #start with no keys pressed
    rt = None #no reaction
    corr = 0 #nothing correct
    if keys: #if a key is pressed
        key, press_time = keys[0] #keys is returned as a tuple of key pressed and the time it was pressed, so here I am assigning key pressed to the variable key and time that the key was pressed to the variable press time
        rt = press_time - start_time #reaction time made up of the time that a key was pressed subtracted from the start time 
            
        if key == 'j': #if the letter 'j' was pressed then the response is j 
            resp = 'j'
        elif key == 'l': #if the letter 'l' was pressed then response is l
            resp = 'l'
            
        if resp == 'j' and stimType == 'living': #this is the loop to track correct responses
            corr = 1 #correct living respone is when the response is j and the stimType is living
        elif resp == 'l' and stimType == 'nonliving':
            corr = 1 #correct nonliving response is when the resp is l and the stimType is nonliving (this is why it was important to be able to access the variable stimType outside of the function (it needed to be global to be accessed here))
        else:
            corr = 0 #if you press the wrong key in response to the wrong stimType, you get a 0
        thisExp.addData('keyPress', resp) #add key pressed to csv to make sure I'm tracking that a key has been pressed
        thisExp.addData('rt', rt) #add reaction time
        thisExp.addData('corr', corr) #add correct response 
        return key, rt #return the key pressed and reaction time 
        
        return None, None#if no key is pressed then return none for key press and reaction time 


#Start of Sustained Attention Task
PracticeTrials(practiceAttn, attnInstructions, livingText, nonlivingText) #call function to begin the practice trials
drawInstructions(attnInstructions) #call function to draw the instructions again for the actual test trials 
    
for i in range(21) : #experiment loop (out of 21 because that's how many stimuli there are and the experiment requires that all be shown (there will be more in the actual experiment to be able to get people to stop focusing but I only included 21 to make it easier for everyone))
    currentType = StimRandom(living, nonliving, livingText, nonlivingText) #assigning the current stim type to call the function (this will allow us to put it into the response function so it can be used to track responses accurately)
    ScreenText(livingText, nonlivingText) #draw the screen text
    win.flip() #flip the window to display to the participant
    get_responseAttn(currentType)#wait for a response then track the response and whether it was correct based on the stimuli type 
    thisExp.nextEntry() #move to the next row in the csv for the next trial
    win.flip() #flip the window
    fixation() #draw the fixation cross
    win.flip() #flip it to the participant's screen
    core.wait(0.5) #500ms delay before showing the next image 


# Surprise Recognition Task
memfileName = f"data/{SetUpInfo['Participant Number']}_Mem" #create a file name for this specific task and using the participant number collected at the beginning of the experiment
memExp = data.ExperimentHandler(name = 'Memory Task', version = '1.0', extraInfo = SetUpInfo, dataFileName = memfileName) #Open a seperate csv for the memory task
    
def mem_resp (trialDuration = 1.5, rt = None, resp = None,): #create a function to track response, it will look at both the key pressed AND whether or not that was the correct response 
    start_time = core.getTime() #start by getting the time 

    keys = event.waitKeys(maxWait = 1.5, keyList=['j', 'l'], timeStamped=True) #create a list of keys, waitKeys means that it will wait for the key to be pressed then move on but it  also has a max wait which is what our max trial duration will be (1.5 seconds)
        
    key = None #start with no keys pressed
    rt = None #no reaction
    corr = 0 #nothing correct
    if keys: #if a key is pressed
        key, press_time = keys[0] #keys is returned as a tuple of key pressed and the time it was pressed, so here I am assigning key pressed to the variable key and time that the key was pressed to the variable press time
        rt = press_time - start_time #reaction time made up of the time that a key was pressed subtracted from the start time 
            
        if key == 'j': #if the letter 'j' was pressed then the response is j 
            resp = 'j'
        elif key == 'l': #if the letter 'l' was pressed then response is l
            resp = 'l'
            
        if resp == 'j' and stimType == 'New': #this is the loop to track correct responses
            corr = 1 #correct living respone is when the response is j and the stimType is new 
        elif resp == 'l' and stimType == 'Old':
            corr = 1 #correct nonliving response is when the resp is l and the stimType is old
        else:
            corr = 0 #if you press the wrong key in response to the wrong stimType, you get a 0
        memExp.addData('keyPress', key) #add key pressed to csv to make sure I'm tracking that a key has been pressed
        memExp.addData('rt', rt) #add reaction time
        memExp.addData('corr', corr) #add correct response 
        return key, rt #return the values for key pressed and reaction time 
        
        return None, None # if a key is not pressed, return none for key pressed and reaction time 



#Start of memory experiment
PracticeTrials(PracticeMem, memInstructions, NewText, OldText) #call the practice trials, input memory specific practice dataframe, memory task instructions, and the screen text to held constant on screen as arguments 
drawInstructions(memInstructions) #draw instructions for the test trials (using memory specific instructions)
for i in range(21): #trial loop, again all stimuli will be shown to the participant. It's 21 here for the sake of it being easy to code for this assignment/to mark
    currentType = StimRandom(NewStim, OldStim, NewText, OldText) #get the current type of stimulus (old versus new)
    ScreenText(NewText, OldText) #draw the old versus new prompt on the screen
    win.flip() #display to the participant
    mem_resp(currentType)#wait for response, max wait will be 1.5 seconds
    memExp.nextEntry() #move to the next row for the next trial 
    win.flip() #remove the stimuli from screen
    fixation() #draw the fixation cross 
    win.flip() #flip the screen, remove the fixation cross from the screen
    core.wait(0.5) #wait 500ms between each stimulus presentation
    
#The psychopy experiment was based on this paper = https://doi.org/10.1177/0956797623120676  
    

