# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 14:36:24 2025

@author: Eryka Jones
"""
import random 
import numpy as np

rt = [] #list of randomly generated reaction times for ten participants
trials = random.randrange(10,20)
for i in range(trials):
    participant = random.randrange(450, 700) 
    rt.append(participant) 

RTmean = np.mean(rt) #calculate the means of the RTs
RTstd = np.std(rt) #calculate the STDs of the RTs
    
complete = [trials] #number of trials completed
print('Trials completed =', complete) #print number of trials completed 

lowRT = min(rt) #the lowest reaction time
highRT = max(rt) #the highest reaction time 

print(lowRT) #print the values
print(highRT)

#Question 2

trimmed_rts = [] #new variable to append to
cut_off = [600] #cut off to trim reactions times

def trim_rts (rt, cut_off): #function to remove RT that are  above 600 by appending only the ones we need to a new variable 
        for i in rt:
            if rt < cut_off:
                rt.append(trimmed_rts) 


#this was an attmept, I'm not sure where it went wrong 

    
#Question 3

def summarize_rts(var): #variable to summarize reaction time, including mean and standard deviation, var allows any list to be put into the function
    rt_mean = np.mean(var) 
    rt_STD = np.std(var)
    complete = [trials]
    print(rt_mean)
    print(rt_STD)
    print(complete)
    
summarize_rts(rt) #put the first list of reaction times into the function





        
    
    


    


        
    




    


    
    



    






    
    
    
    
     

