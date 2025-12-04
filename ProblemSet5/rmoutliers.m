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