%November 27th


%{ 

Big difference between python for logicals - & is and and | is or
also elseif

%}


1 == 0 


%Matlab does not care about spacing and indentation, it just matters that
%we start with an if and end with an end. 
%Adding double & tells it to ignore the thing that follows it (making code
%more efficient)

%Another conditional is called a switch/case 

%tic toc function will tell you how long it takes to complete the thing. 

%Good idea to pre-allocate the variables to save time and make the code
%more efficient


%Parfor - allows you to run loop in parallel, which could allow you to run
%multiple loops at the same time (like for running participant data
%analysis)


%Set size = will set a mask that will return a series of 0 and 1 where 1 is
%when the mask = True


function outputArray = subtractOne(inputArray) 
    outputArray = inputArray - 1;
end

%Function is call subtractOne. Output array is the variable being returned
%like that. Inputarray is one that goes into the function and has one
%removed from it. 


%if nargin is the amount of arguments in a function and can be used to
%tell it what to do if given a certain amount arguments

%Addme allows for creating a help manual by using commenting and stuff lol


subjectNum = input('Please enter the subject number:')

%Cells and structures similar to the pandas dataframe 
cell1 = {'Apples', 'oranges'}

cell2 = {[1 2 3 4], [1 2 3 4 5 6]}

cell2{1}(4)

cell2{3} = "does this work?" 

data2.subject = 'SME'
data2.rt = [0.9, 1.2]

