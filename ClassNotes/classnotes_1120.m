%main differences from python - use end to terminate the command (so in an
%if loop you need an end to stop it)
%Then uses the percent sign instead of the #

A = [1 2 3 4 5]
B = [1 2 3 4 5]


%clc clears the command window (clear will remove the variables and clear with the variable name will remove just that variable)
%If you do not assign a variable to an operation, it will create a variable
%named "ans"
%Semi colons will make sure it does not print to the command window

%You cannot run a cell but you can create a section to be able to run the
%section specifically (using section break)

%you can execute the script by typing the file name in the command window
%(so if I typed classnotes_1120, it would run this whole file. 

%who tells you who exists in the variable while whos tells you the specific
%information for each variable (like size)

d = [1;2;3;4;5] 
%commas separate out the columns, semicolons separate out the rows 

m = [1 2; 3 4;5 6;]
%creates a the row by two column matrix 

%Matrices must be rectangular, it has to have an element at every location
%in a rectangular matrix 

%If you are missing a value, you can substitute with NaN to rep 'not a
%number.' 

%To index: you use the round brackets 
A(3)

m(3)
%For a matrix, you can use number of rows down and the amount of columns
%over (r x c)
%You can find more values by providing a vector 

m([1 3],1) %tells it to look at the first and third rows in the first column

%you can also make this a variable 
trials = [1 3]

m(trials,1)

m(:,2) %every element in the second column, : tells it to give you everything 

m(2:3,2) %range between those two values 

m(2:end, 2) %from two the end is the length of the range 



a = 1:2:10 %one in the middle specifies the step, the first and third represent the start and end of the range

a' %transposes the matrix (takes the row and column vectors and flips them)

%You can also concatenate the different matrices by putting the variables
%into the square brackets [a b]

%You can add a value to a matrix by indicating the next row number and
%putting a value 

c(5) = 5 
c(10) = 6 

%If there is a missing value, it will put a zero in it's place 

c(6:9) = []

%instead of creating an empty list to append to, it's best practice to
%create your matrix and add to it in a loop 
%Can fill this array with zeroes, ones, NaNs

a = zeros (5,5);
b = ones (5,5);
c = NaN(5,5)

%matlab has a default random generator that is generated for every time you
%opend up the random generator 

%flip will flip the matrix keeping the order in tact 
%rotate will rotate the matrix 

a = [1 2; 3 4; 5 6]

rot90(a)


a .* [1 2] %default is matrix multiplication or division, to regular multiply, you add a period

save('myfirstmat')

load('myfirstmat.mat')

%the first highlighted thing when you open a bracket tells you the required
%argument. Help and the name of the function will load the documentation.
%Tells you about syntax too. Give examples 

%Can get mean and std in this without needing to import a library. 

mean(a) %gets a mean of each column
mean(a') %transposes it 
mean(a, 'all') %to get a mean of the entire matrix


%there is always a random number generator that is opened every time in
%matlab. rng('shuffle') will shuffle the RNG so it's different every time
%you open matlab. You can also seed the RNG to produce the same random
%sequence. 


%Structure is a variable type that is like a dataframe

%Imaginary  numbers - complex double value that rep the actual number and
%the imaginary number. 