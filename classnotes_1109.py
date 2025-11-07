# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6

@author: eryka
"""
coords = [(1,2),(2,3), (4,5), (5,6), (6,7)] #tuple, we can pair two values together
#hard to slice the data, so hard to use with multidimensional data

type(coords)

#Dictionaries allow us to store multi-dimensional data
#Used with {}, they take a key and value separated by a colon, each entry is separated by comma

nbateams = {'Los Angeles':'Lakers', 'Toronto':'Raptors', 'Chicago':'Bulls'}

#They are not indexed by number like a list, but they are instead indexed by keys (the keys should be unique)
#can also use dict() function which can turn a list of tuples into a library 
#Retrieve a dictionary item by calling a key
#Like:
nbateams['Toronto']
nbateams.get('Toronto')

#Can't be called by the other value (so in this case the raptors) because they can be repeated and keys can not 


#Numpy! 

import numpy as np

arr = np.array([1,2,3,4,5])
arr2 = np.array ([[[1,2,3], [4,5,6]],[[1,2,3], [4,5,6]]]) #accidentally made a 3D array here lmao

print(arr2)

arr[0] #will return the first slice of the multidimensional array
arr2[0,1] #for 3D arrays, you need 2 values to call this properly 

#We can loop through an array using the following:

for x in arr2: #this went through one level of the array
    #print(x)
    for y in x:#this goes through the next level, then it can get to printing each individual value
        print(x)
        print(y)
        for z in y:
            print(z)
    
#Can reshape an array by using arr.reshape
#Can stack two 1D arrays by passing the two arrays to np.vsstack(arr1, arr2)
#np.array_split(arr,3) splits an existing 1D into 3 parts

#We want to be able to find certain values in our data though
#We can do this in numpy (this is why it's better to use than just a list)
#We can find certain values by going through booleans while using a mask. 

newArr = [5,6,7,4,7,8,2,1,0]

newArr = np.array(newArr)

mask = newArr > 2
newArr[mask] #this is where I keep getting stuck!!!!!!!

cleanData = newArr[mask] #We can also just put the boolean in this bracket 

newArr2 = [0,1,2,3,4,5,6,7,8]

newArr2 = np.array(newArr2)

x = newArr[newArr2 > 4] #This is almost certainly where I get lost

#cleanData = rt[(cond == 1) and (block >4)]  

#np.nonzero returns all non zero elements
#np.where similar to masking, but you are defining the condition
#This allows you to mask it as more than just true or false 

data = np.loadtxt(fname = 'inflammation-01.csv', delimiter = ',')

print(type(data))

print(data.shape)

data[10,35]

print(data[0:4, 0,10]) #Colon by itseld will index everything, start is zero and end is negative one 

#a slice of 0:1, 0:1, will only return one value 

meandata = np.mean(data)

meandata = np.mean(data, 0) #this is where you can set it to just compute means over a specific axis

meandata = np.mean(data[0], 0) #will give us one value by looking at the row and column


np.mean(data[0,:]) #this will do the same thing

#Random is also useful

from numpy import random

randData = random.randint(5,10, size = [10,50]) #creates an array

random.rand()

random.choice(data[0,:]) #will grab a random value from the array

conds = [0,1,2]

print(random.shuffle(conds))

random.permutation(conds)

#differenece between numpy and pandas - numpy is good at data analysis 
#pandas is good for other kinds of data like words 
#pandas can handle several types of data whereas numpy cant necessarily

#Two data structures in pandas:
#Series - one dimensional array capable of holding data of any type 
#DataFrame - the primary strcuture. 2 dimensional, mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns)

import pandas as pd

volumes = pd.Series(['4 cups', '1 cup', '2 large', '1 can'])

s = pd.Series(data =[ 1, '2', 3, 4, '5', 6,7,8, '99', '100'])

s.astype('int') #will turn any string into an int as long as it's a number

x = s.astype('int')
x.mean()

s.astype('str') #turned everything back into a string

#You can also replace or remove missing data
data = pd.Series([1,2,pd.NA,4,5])
data.dropna(inplace = True)

data.fillna('Null', inplace = True) #this will replace the data where the na value is 

data.apply(np.sqrt)

data = [1,2,3,4,5]
data = pd.Series([1,2,3,4,5])

data.apply(np.sqrt)

data.apply(lambda x: x +1)

data = pd.read_csv('RTdata.csv') #looks like a spreadsheet

data['subjs']

data['subjs'][5]

data = pd.read_csv('RTdata.csv', index_col = 'subjs') #this is to tell it to index it by the subject row 

#iloc can look at the columns to call them, you can use a number or the column name

data.loc[:,'K'] #you can also do data[:],['K']

data.iloc[:,4] #iloc needs the number pf the column

RT = data.iloc[:,5]

data.groupby('sex').mean() #data.groupby will group data by the groups you give it
#so in this case it would do rt etc by male and female 


output = data.groupby('sex').mean() #would make a separate dataframe 

output.loc['m']['RTs']

data.groupby(['sex', 'race']).mean()

data.groupby(['sex']).mean()

data.loc[:,'sex']

help(np.mean)


data.mean()

titanic = pd.read_csv('titanic.csv')

titanic['Name'].str.lower()

titanic['Name'].str.split(",")

titanic['Surname'] = titanic['Name'].str.split(',')





