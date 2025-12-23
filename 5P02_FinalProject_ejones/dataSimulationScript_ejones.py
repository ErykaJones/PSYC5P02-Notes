# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 12:04:57 2025

@author: Eryka
"""

import numpy as np
from numpy import random
import pandas as pd

PIDYA = random.choice(range(1,31), size = 30, replace = False) #Generate Participant IDs for the younger adults 
PIDOA = random.choice(range(31, 61), size = 30, replace = False) #Generate Participant IDs for the older adults 
PIDYA.sort() #Sort so they are in order 
PIDOA.sort() #Sort so they are in order 

YA_rts = [] #empty list to append to 
OA_rts = [] #empty list to append to 

for i in range(30): #for thirty participants 
    YA = random.normal(394.1, 78.45, 28) #generate RTs for younger adults (using Mindwandering paper for mean and SD), 28 is the number of numbers to generate beacuse in the psychopy experiment, there was only 28 trials
    YA_rts.append(YA) #append to the empty list 
    OA = random.normal(474.2, 116.0, 28) #Generate RTs for older adults (using the same Mindwandering paper for mean and SD)
    OA_rts.append(OA) #append to the older adult list 


OAdata = pd.DataFrame(data = {'PID':PIDOA, 'RTs':OA_rts, 'Group':'Older'}) #make an Older Adult Dataframe to store Participant ID, reaction time, and the group they belong to
OAdata = OAdata.explode(['RTs']) #explode basically unnests the trials so instead of one cell having 28 reaction times in it, they each get their own cell and are all associated with the same PID (so 28 reaction times will all be assigned a PID of 1 to represent the first participant's 28 trials)
YAdata = pd.DataFrame(data = {'PID':PIDYA, 'RTs':YA_rts, 'Group':'Younger'}) #make a younger adult dataframe to store Participant, reaction time, and the group they belong to 
YAdata = YAdata.explode(['RTs']) #explode this data set, does the same as above 


meanYA = np.mean(YAdata['RTs']) #calculate the mean of RTs in Younger Adults 
meanOA = np.mean(OAdata['RTs']) #calculate the mean of RTs in Older Adults 

YAdata['Trial Type'] = np.where(YAdata['RTs'] < meanYA, 'In the zone', 'Out of the zone') #Locate RTs that are under the mean, meaning they are fast responses and this is usually indicative of being "in the zone" for attention, so these will be assigned the "in the zone" label in a new column called Trial Type. If the RT is greater than the mean, it will be considered an "out of the zone" trial
OAdata['Trial Type'] = np.where(OAdata['RTs'] < meanOA, 'In the zone', 'Out of the zone') #Same as above but for the older adult data 

for i in range(30): #for 30 participants, calculate the accuracy in their judgements of living versus non living 
    dist_x = np.random.normal(50, 2, size=len(YAdata)) #generate some accuracy scores that are at change (50%) with a SD of 2. 
    dist_y = np.random.normal(75, 2, size=len(YAdata)) #generate some accuracy scores at 75% with a SD of 2 
    
    YAdata['Memory Accuracy'] = np.where(YAdata['RTs'] < meanYA, dist_y, dist_x) #For RTs that are smaller, that means the participant was in "in the zone" so they are assigned an accuracy that is 75% because data shows if you are paying attention, you are more likely to remember what you've seen. Additionally, if the RT is above the mean, it's larger. That usually indicates being "out of the zone" and so you are less likely to remember, so you get a lower accuracy score. 
    
    dist_x_oa = np.random.normal(50, 2, size=len(OAdata)) #same as above but for the older adults 
    dist_y_oa = np.random.normal(75, 2, size=len(OAdata))
    OAdata['Memory Accuracy'] = np.where(OAdata['RTs'] < meanOA, dist_y_oa, dist_x_oa)


GroupedData = pd.concat([OAdata, YAdata], ignore_index = True) #Group the data into one big data frame. They were intially separate so I could generate RTs, accuracy scores, and sort them into "in the zone" versus "out of the zone". It was just a lot easier this way. 

NoiseNum = [] #this is to keep track of the value of the noise that was generated so I could check my work and make sure the function to add noise was actually added. 
MemoryNoise = []
def AddNoise(GroupedData): #Function to add noise to the RT data. 
    for i in range(len(GroupedData['RTs'])): #For the range of all the reaction time data
        noise = np.random.uniform(low = -20,high = 20, size = None) #generating noise +/- 20ms randomly
        NoiseNum.append(noise) #add to the empty list 
        MemNoise = np.random.uniform(low = -10, high = 10, size = None) #add noise to the memory scores 
        MemoryNoise.append(MemNoise) #add to the empty list 
    GroupedData['RTs'] = GroupedData['RTs'] + NoiseNum #adding the noise generated to the RT data 
    GroupedData['Memory Accuracy'] = GroupedData['Memory Accuracy'] + MemoryNoise #adding noise to the memory data 
    
AddNoise(GroupedData) #call the function

def removeOutliers(GroupedData): #Function to remove outliers in RT
    meanRT = np.mean(GroupedData['RTs']) #get the mean
    SDRT = np.std(GroupedData['RTs']) #get the SD
    threshold = 2.5 #get the threshold (more than 2.5 SDs from the mean()
    ulimit = meanRT + threshold * SDRT #calculate upper limit 
    lLimit = meanRT + threshold * SDRT #calculate lower limit 
    mask1 = GroupedData['RTs'] > lLimit #This is the upper limit of the range. I think this is too high to actually remove the lower outliers as none the values are removed. It does work when replaced with other values like 300. 
    mask2 = GroupedData['RTs'] < ulimit #This is the lower limit of the range to remove. I think this is too high to catch the upper outliers. This function does work when replaced with smaller values. 
    ItemsRM = mask1.sum().sum() #This is to calculate the amount of RTs that were removed from the data using the upper range 
    ItemsRM2 = mask2.sum().sum() #This is to calculate the amount of RTs that were removed based on the lower range number 
    print(ItemsRM, ItemsRM2) #keep track of how many RTs are removed 

removeOutliers(GroupedData) #call function



#The two studies that helped me simulate data:
    #Mindwandering paper = https://doi.org/10.1162/jocn_a_02195
    #Sustained attention and memory performance = https://doi.org/10.1162/jocn_a_01748







    
    



    