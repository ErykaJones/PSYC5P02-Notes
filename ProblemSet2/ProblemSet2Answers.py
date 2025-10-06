# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 18:08:55 2025

@author: Eryka Jones
"""
#Question 1a
import numpy as np
x = np.random.normal(0.7, 0.2, 100) #randomly generate numbers with a SD of 0.2 and mean of 0.7, assign to x
y = [] #empty variable that will allow me to append the z values to to save the values that are not outliers 

#Question 1b 
def rmoutliers(var):  #function to remove outliers
    """ function to remove outliers that are more than 2.5SDs from the mean"""
    mean = np.mean(var) #calculate mean to find z scores
    SD = np.std(var) #calculate the SD of the group
    for i in (var): #loop to cycle through each value in the list 
        z = (i - mean)/SD #calculate individual SD, z to represent a z score
        if z < 2.5 : #condition
            y.append(z) #append the value that are not outliers to a list 
        elif z > -2.5:
            y.append(z) #append the value to y if it is not an outlier
        else:
            continue #command to continue if SD is greater than 2.5
    print(mean, SD) #show the group mean and SD
    
#I chose to use a for loop because I had trouble writing a while loop. It always ended up going endless and with all the reading I did (see below for sources), the for loop was one that I could get to work. 
#The function does work to remove any outliers greater than 2.5 

#Question 1c
rmoutliers(x) #runs the function to remove outliers on x (the randomly generated list of values with a mean of 0.7 and a SD 0.2). x is the variable assigned to this list.
# y is where the list is the one that becomes created as values are removed. 


#Question  2a
name = ["Lisa", "Emily", "Frank", "Will", "Victor", "Heather", "Penny", "Jill", "George", "Nicole"]
grades = [81, 80, 82, 80, 92, 90, 97, 81, 76, 88] #making the grades that were generated into a list to make it easier for the loop
#grades were generated using np.randint(76,100)

#Question 2b
for x in grades: #loop for grade, it takes the grade then prints the letter grade
    if x >=90: 
        print('A+')
    elif x >=85:
        print('A')
    elif x >=80:
        print('A-')
    elif x < 80:
        print('B+')
    else: 
        print('B+')    
 #this loop is pretty straight forward, it goes through the list of grades and determines if the grade is A+ (>= 90), A(85 - 90), A- (80 - 85), B (80 - 76)

        
#Question 3
def gradeLookup(grades):
    """this function allows for the user to input their name, it will then produce their name, their number grade and letter grade"""
    name = input('Enter your name:')
    if name == 'Lisa':
       print('Lisa, 81, A-')                 
    elif name == 'Emily':
       print('Emily, 80, A-')
    elif name == 'Frank':
       print('Frank, 82, A-')
    elif name == 'Will':
       print('Will, 80, A-')
    elif name == 'Victor':
       print('Victor, 92, A+')
    elif name == 'Heather':
       print('Heather, 90, A+')
    elif name == 'Jill':
       print('Jill, 81, A-')
    elif name == 'George':
       print('George, 76, B+')
    elif name == 'Penny':
       print ('Penny, 97, A+')
    elif name == 'Nicole':
       print ('Nicole, 88, A')
    else:
       print('not available') 
       
 #for this loop, I just attached each name to the letter and number grade
# I wasn't sure how to set it up where the two lists were attached. This was a good alternative to ensure the same result though. 
  

#Question 4 
class PersonalityProfile: #creating a class for personality using participant as an attribute to keep track of participant ID and the big five personality traits
    def __init__(self, participant, conscientiousness, agreeableness, neuroticism, openness, extraversion):
        self.participant = participant 
        self.conscientiousness = conscientiousness
        self.agreeableness = agreeableness
        self.neuroticism = neuroticism
        self.openness = openness
        self.extraversion = extraversion
    
    def is_conscientious(self):   #function to display that a participant is conscientious by using >= 3 as the trait level 
        if self.conscientiousness >= 3:
            return True
        else:
            return False

    def is_agreeable(self): #function to display that a participant is agreeable by using >=3 as the trait level
        if self.agreeableness >= 3: 
            return True
        else:
            return False
    
    def is_neurotic(self): #same as previous two functions but this time for neuroticism
        if self.neuroticism >=3:
            return True
        else:
            return False
    
    def is_open(self): #same as previous but for openness
        if self.openness >=3:
            return True
        else:
            return False
    
    def is_extrovert(self): #same as previous but for extraversion
        if self.extraversion >=3:
            return True
        else:
            return False
        

participant1 = PersonalityProfile(1, 1, 3, 4, 3, 1) #generating one fake participants data
participant2 = PersonalityProfile(2, 3, 2, 1, 3, 4) #generating a second fake participants data, both participants helped to ensure the class and functions  were working properly 

#I created a class for personality profile and listed the attributes as participant number and the big five personality traits 
#Then I created a function that would output true if the trait level was >= 3, this was based on the example used in the problem set instructions.

#I used four things to help me write this assignment:
#geeksforgeeks.org - this helped me form the loop in question 1
#numpy.org for the manual of how to randomly generate numbers and do statistics
#docs.python.org for looking up python functions, especially for the class question
#https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc - this youtube video and the playlist it is a part of helped me understand class 

        
  
            

       
   
    
    
   
    
    



                 
        
        
        
    


       
        
         
       
        
    
    






       
    
    

    
    
        