## Problem Set 1 Answers
###### Eryka Jones

### Modified by SM EMrich


1. a) ls -r
   
>> **You need to add the ``-t`` to include sorted by time**

b.ls -all

>> **Be sure to list the full command: ``ls -lrt``**

c. -r, --reverse  
              reverse order while sorting
>> **Try to add more explanation.**

:memo: **1/3**

2. cd /~, cd /home, cd ../
  >> **``cd /~`` doesn't work. It's ``cd ~/``**
  >> **Based on the convention I described, you need to spell out the full path: ``cd /users/home`` or something similar. Again, please provide more context for your answers!!** 

:memo: **1/3**

4. mkdir Data  
touch subj01.txt  
cp subj01.txt subj02.txt  
cp subj01.txt subj03.txt  
cp subj01.txt subj04.txt  
cp subj01.txt subj05.txt  
cp subj01.txt subj11.txt  
mv subj*.txt ~/Data  
rm subj0*.txt

:memo: **5/5**

6. The aim of the pipe I created was to list all the files in the directory created to store the files for this problem set then copy them into a .txt file. First, I made sure I was in the correct directory (called ProblemSet1).Next, I used the touch command to create a new file called filelist.txt. Next, I created the pipe using ls -all and tee filelist.txt. See the full command process below.

 touch filelist.txt
psych@DESKTOP-879DCU1:~/ProblemSet1$ ls -all | tee filelist.txt  
total 16  
drwxr-xr-x 3 psych psych 4096 Sep 15 10:37 .  
drwxr-x--- 9 psych psych 4096 Sep 15 10:35 ..  
drwxr-xr-x 2 psych psych 4096 Sep 15 10:33 Data  
-rw-r--r-- 1 psych psych  308 Sep 15 10:22 ProbSetAnswers.txt  
-rw-r--r-- 1 psych psych    0 Sep 15 10:37 filelist.txt   

:memo: **3/3**

5.The files are not the same. The file (history.txt) created while in the screen showed all the history up until the creation of the screen then showed only the commands that were executed while in the screen. When the screen was detached, the history file created in the terminal did not have the commands that were executed in the screen. This file (history2.txt) only shows the history of commands executed in the terminal, which includes everything up to the creation of the screen and after the screen was detached. 

:memo: **3/3**

6. ![This is a screenshot of my completed tutorial](https://github.com/ErykaJones/PSYC5P02-Notes/blob/e314ed6f925b77af3e37a3cd7afb4e9654988bec/ProblemSet1/Screenshot%20(1).png)

7. ![This is a screenshot of my terminal window listing the files in my repo](https://github.com/ErykaJones/PSYC5P02-Notes/blob/e314ed6f925b77af3e37a3cd7afb4e9654988bec/ProblemSet1/Screenshot%20(2).png)

8. The command I used to create the file were history | tail -n 341. I used this because I was trying to isolate the commands, which were further up in the history. I used touch to create a blank text file to copy the history into, that file is called githistory.txt.   

>>**Why so many lines of next? You could just do the last few lines. Something like `history | tail -n 4 > git_commit_commands.txt`. Also how did you copy everything into the file?

:memo: **1/3**

:memo: **Total: 21/26
