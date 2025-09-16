## Problem Set 1 Answers
###### Eryka Jones


1. a) ls -r
b.ls -all
c. -r, --reverse
              reverse order while sorting

2. cd /~, cd /home, cd ../

3. mkdir Data
touch subj01.txt
cp subj01.txt subj02.txt
cp subj01.txt subj03.txt
cp subj01.txt subj04.txt
cp subj01.txt subj05.txt
cp subj01.txt subj11.txt
mv subj*.txt ~/Data
rm subj0*.txt

4. The aim of the pipe I created was to list all the files in the directory created to store the files for this problem set then copy them into a .txt file. First, I made sure I was in the correct directory (called ProblemSet1).Next, I used the touch command to create a new file called filelist.txt. Next, I created the pipe using ls -all and tee filelist.txt. See the full command process below.

 touch filelist.txt
psych@DESKTOP-879DCU1:~/ProblemSet1$ ls -all | tee filelist.txt
total 16
drwxr-xr-x 3 psych psych 4096 Sep 15 10:37 .
drwxr-x--- 9 psych psych 4096 Sep 15 10:35 ..
drwxr-xr-x 2 psych psych 4096 Sep 15 10:33 Data
-rw-r--r-- 1 psych psych  308 Sep 15 10:22 ProbSetAnswers.txt
-rw-r--r-- 1 psych psych    0 Sep 15 10:37 filelist.txt   

5.The files are not the same. Previous histories appear to be the same until I started working on this assignment and the commands that had been completed just before the screen opened were not present in history.txt, the file containing the screen history. In history2.txt, I do see the commands that were executed before opening the screen.

6. ![This is a screenshot of my completed tutorial](https://github.com/ErykaJones/PSYC5P02-Notes/blob/e314ed6f925b77af3e37a3cd7afb4e9654988bec/ProblemSet1/Screenshot%20(1)

7. ![This is a screenshot of my terminal window listing the files in my repo](https://github.com/ErykaJones/PSYC5P02-Notes/blob/e314ed6f925b77af3e37a3cd7afb4e9654988bec/ProblemSet1/Screenshot%20(2).png)

8.   
