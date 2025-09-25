# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 14:38:55 2025

@author: psych
"""
#can use the console like terminal (might work to commit things to the repository)
#Script - python code meanwhile notebook - both markdown and python code
# saving file .py makes it a python script 
# use the pound sign to denote a comment, it will not be read as code and can be used to tell others and yourself what you're doing
# leave comments!!
# loops: an instruction that repeats until a specified condition is met 
# two types:
# For loops run for a preset number of times (has to end in colon!, must also have an indent)
# While loops run as long as an expression is true (almost like an if statement)
for i in range (1,5):
    print ("i am in the loop")
    print (i)
#When it runs in script, you can see it in the console 
#Ranges are not inclusive 1-5 will only list to 4 
#Non-indented line will break the loop
#variable explorer will help you keep track of the values associated with variables



#new loop 
mylist = ["apple", "banana", "cherry"]
for x in range(len (mylist)):
    print (x)

#while loop - while a conditional statment remains true
i = 1
while i < 6:
    print(i)
    i += 1
# += take the value on the left and add it to the one on the right (so i+1 for above code)
# can get stuck in an infinite loop - if you accidentally used a less than value 
# ctrl - c if you have your cursor in the terminal window will kill the running process
# other ways to move around loop or br3eak a loop:
# break command will exit out of the look entirely - if i == 3: break (indent break)
# continue command i = 0 while i < 6: i == 3: continue print i
i = 0 
while i < 6:
    i += 1
    if 1 == 3:
        continue
print(i)
# continue command will stop the next command from occuring (the continue command prevented the print (i) command)
# scope refers to the region of the code in which a variable or resource is visible and accessible
# if variables are declared within a while or for loop, their scope exists in the loop and nothing above it
# that would be local scope
# a global scope is a variable that exists everywhere in your code
# there is a global command

for i in range (0,5):
    x = i
    print(x)
print(i)
print(x)
# scope may not matter for loops 
# base python has limited capabilities
# adding libraries to the script/session can expand it's capabilities 
# They come in the form of packaged libraries (psychopy)
# they need to be imported and named, when you import use code import [packaged libraries] in console
# can import several and specific ones form larger ones
# one of the most common we will use is the random library (method)
# good for randomizing stimuli, conditions, time, created simulated data
# RNGs are seeded (tied to some value - seed) 
# can set seed to a specific value or get the state of the RNG at a particular point in time
# can also do it to state 
# randomly generated values are set to a state that can be brought back
# important for psych - in collecting data by randomizing the important things, by returning to the state we can go back to see where an error back
# or go back to your stimuli (this allows you to replicate the randomness)
# random.normalvariant - normal distribution ******important*******

#Functions
#modular bits of code that carry out a particular task or operation (can be used to increase the efficiency of your code by repeating blocks of code)
#can be called repeatedly throughout code
# can take arguments (inputs) and return values (outputs)
# print is a function

def nameprintfunc(name):
    print('the name is'+ name)
    return name

#colon is necessary and everything within it needs to be indented

def adderfunc(val):
    x = val + val
    print(x)
    return x
    
# scope is important for function!!!!!!!
# x would be unreadable outside of the function 
# return is useful for moving variables out of the scope (so from local to global)

def adderfunc(val = 4):
    x = val + val
    print(x)
    return x

def adderfunc(val1, val2 = 4):
   """adds two numbers together"""
   x = val1 + val2
   y = (val1 + val2) * 2
   return x

# needs an initial argument to go through
# can add your own help to the function
# typical to have a little comment in triple quotes to say who wrote the script and what it's for
# triple quotes is like adding a whole section of comments


# classes are like functions that have data
# allows you to build flexibility in your code and re-use common procedures 
# a form of object oriented programming 
# create a class, class has attributes (data) and methods (operations), can create multiple instances of the class 

class car: 
    def __init__(self, color="white"):
        self.speed = 0 #self allows you to access variable from anywhere else in class
        self.color = color #color is degined by (optional input)
    def drive(self):
        self.speed = self.speed + 1
    def breaking(self):
        self.speed = self.speed = 1 

vw = car()
toyota = car ('green')

carList = [car() for x in range(0,5)]

carList[2].color

for i in range(1,100):
    vw.drive()

print (str(vw.speed))

# classes can be stored in a separate file 
# using from filename import class
# %%
# class car: 
    def __init__(self, color="white"):
        self.speed = 0 #self allows you to access variable from anywhere else in class
        self.color = color #color is degined by (optional input)
    def drive(self):
        self.speed = self.speed + 1
    def breaking(self):
        self.speed = self.speed = 1 

vw = car()
toyota = car ('green')

carList = [car() for x in range(0,5)]

carList[2].color

for i in range(1,100):
   vw.drive()

print (str(vw.speed))

