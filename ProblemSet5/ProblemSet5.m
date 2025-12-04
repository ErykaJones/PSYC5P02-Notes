%Problem Set 5
%Eryka Jones

%Problem 1 

RT = [520 498 601 1200 450 475 3000 510 490]; %Create a  vector of RTs

cleanData  = RT < 1500; %loops through the RT vector and assigns a 1 if the value is under 1500ms and 0 if it is above 1500ms 

RT_clean = RT(cleanData); %looks for the values that coincide with the 1s that are in the cleandata vector, then it returns the values to this vector. So, all the values above 1500ms are removed. 

mean = mean(RT_clean) %calculate the mean of RT_clean

median = median(RT_clean) %Calculate the median of RT_clean

numRM = sum(cleanData == 0) %Calculate the number of values that were assigned 0 (so they were over 1500ms), this is the number of values that were removed in the RT_clean vector

%No semicolons on the previous three commands because I want them to print
%to the terminal. 

%% 

%Problem 2

data = [randi([1,100],10, 1), randi([1,2], 10, 1), randi([1,2],10, 1)]; %generate a three column data matrix. In the first column and instance of randi, they are numbers being generated between 1 and 100. The second randi is generating values of 1 or 2. The third instance of randi is generating values of 1 or 2 as well. Each randi function is 10 entries for each column.  

highLoad = data(:,2) == 2; %Organize the second column into highload, which was represented by 2s
lowLoad = data(:,2) == 1; %Organize the second column into low load by looking for all the ones in the column 

highLoadNum = data(highLoad); %Assign the highload data to a variable 
lowLoadNum = data(lowLoad); %assign the low load data to a variable 


meanHigh = mean(highLoadNum) %calculate the mean of high load by looking for the 2s in the second column and looking into the corresponding row in the first column for the rt. 

%% 

%Problem 3 


    if data(:,1) < 50 & data(:,3) == 1 %Loop that will look at all the rows in the first column and see if the value is less than fity and in the third column, in the same row, if there is a 1, then it will print correct. If not, it will print incorrect. 
      response = 'correct'  
    elseif data(:,1) >= 50 & data(:,3) == 2 %If column one value is greater than or equal to 50 and the value in column 3 is 2, it will also present correct. 
      response = 'correct'
    else
      response = 'incorrect' %if none of the above conditions are met, print incorrect. 
    end


%% 

%Problem 4

mu = 0.700 %the mean
std = 0.5 %I needed a standard deviation to put into the formula to accurately generate the numbers

RTS = std*randn(100,1)+mu; %formula to generate RTs with a mean of 0.700 

noise = 400; %noise to be added to the RTs
NoisyRTs = RTS + noise; %add the noise 
threshold = 2; %create a threshold of 2 SDs from the mean


removedRTs = rmoutliers(threshold, NoisyRTs) %call the function rmoutliers to recursively remove outliers



function [cleanData, counter, removedcounter] = rmoutliers(threshold, NoisyRTs)
   %RMOUTLIERS input data to calculate and remove the outliers in your data. It
   %also keeps track of how many loops it's done, how many have been
   %removed, and the new mean. 
   counter = 0 %variable to count how many loops have been completed 
   removedcounter = 0 %variable to track how many have been removed the dataset
   startLength = length(NoisyRTs) %keep track of the original length of the  data frame 
    while true %while loop to loop through data set and remove outliers
        meanRts = mean(NoisyRTs); %calculate the mean of the noisy data
        SD = std(NoisyRTs); %calculate the standard deviation
       
        upper = meanRts + threshold * SD; %calculate the upper limit to compare the RTs to
        lower = meanRts - threshold * SD; %calculate the lower limit to comapre the RTs to 
        
       
        cleanData = NoisyRTs(NoisyRTs < upper & NoisyRTs > lower); %organize the data by sorting it by noisyRTs that are lower the upper limit and are bigger than the lower limit. It then assigns all variables that pass this to the variable cleanData
        
       
        if length(cleanData) == length(NoisyRTs) %if the two lengths are the same, stop the while loop but go back to the first while loop 
            break; 
        else %if it does not match, then adding the NoisyRTs to cleanData
            NoisyRTs = cleanData; 
            rmnow = startLength - length(cleanData); %subtract the lengths of the two variables to see if one has been removed 
            removedcounter = removedcounter + rmnow; %add this number to the variable removedcounter
        end
    counter = counter +1; %add one to the loop counter 
    end
    meanNew = mean(cleanData); %calculate the mean 
    fprintf('The number of loops: %d, The mean is: %.2f, and the number removed: %d\n', counter, meanNew, removedcounter) %print the loop number, the mean of the new data and the number removed. 
end

%I looked at the class notes for the second problem set, I also had to use
%AI here because I needed help debugging the while loop in order to
%actually get it to remove the outliers. This was a difficult question to
%answer as it was in the first problem set. 

%% 

%Problem 5
load('experiment_data.mat'); %load the .mat file into matlab

fprintf('Participant ID: %s', data.participant) %list the participant ID that is the first slot. The %s shows that it's looking for a string input from the data.participant column and prints it to the terminal. 

data(2).participant = 'P002' %create a second entry titled participant ID and insert 'P002' into the column.
[data(2).trials] = deal(data(1).trials) %add data to the second participant by applying the deal function



%Most of this assignment I referenced the matlab online documentation.
%Additionally, I also used the matlab help forums and the stackoverflow.com
%forums. AI was used for problem 4 to help debug. 















