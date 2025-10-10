# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 14:38:32 2025

@author: psych
"""

#for problem sets, try to think about if it could be a variable instead of number/word etc
#can use websites for the midterm
#review, coding the assignment again 

#for question 2, should have defined the upper and lower limits 
#calculate the SD and mean should have happened more than once 

import statistics, random
import numpy as np
data = [random.normalvariate(0.7, 0.2) for i in range(100)] #create list of variables 
threshold = 2.5 #cutoff threshold

cleanedData = [] #empty variable to append to 

def trimmMeans(data, threshold):
    
#while loop to circle through data points in data and append them to cleanedData
    while True:
        cleanedData = []
        mean = statistics.mean(data) #mean
        SD = statistics.stdev(data) #standard deviation
    
    #calculate limits 
        uLimit = mean + threshold * SD
        lLimit = mean - threshold * SD
    
    #remove outliers in the loop:
    
    #cleanedData = [value for value in data if lLimit <= value >= uLimit] #value instead of the list itself solved the float to list problem
    #for value in data is a loop, it will go through the list 
    
    #remove outliers in numpy slicing 
        data = np.array(data)
        cleanedData  = data [(data<uLimit) & (data>lLimit)]
    #this is looking at each value and going True or False. If the values are True, then those will be taken. Acts like a loop. 
    #if you can slice using loops, it may be more beneficial 
     
        if len(cleanedData) == len(data):
            break
        else:
            data = cleanedData 
    
        return cleanedData 

newData = trimmMeans(data, threshold)

#figure out what operations you need to do before functions 


#Question 2
names = ["Alyssa", "Rosa", "Christine", "Holly", "Joel", "Mimi"]
grades = np.random.randint(71,90,6)

#what is important here is indexing

for i in range(len(names)): 
    print(names[i] + grades[i])

#you can put two lists together - using a comma and [] to make a new variable

#for question 3 
#names.index("Joel")
#function should have just been able to locate the location of the name and print out all the things associated 

inputName = input("Please enter a name:")
idx = names.index(inputName)
print(names[inputName]+ "'s grade is" + str(grades[names.index[idx]]))





    