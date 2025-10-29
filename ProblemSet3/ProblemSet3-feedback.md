# PSYC 5P02- Introduction to Programming for Psychology
## Fall 2025

### Problem Set #3

### Rubric:
* Accuracy & Efficiency: 50%
* Explanation and documentation: 50%

--- 
###  Feedback:

* No data saved
* Feedback doesn't work correctly. I think it might be a simple fix. the keys are defined as `'Left'` and `'Right'`, but the logical is checking for `'left'` and `'right'`. Left != left!!!!!!!!!
* You're also calling both `resp = event.getKeys(keyList = ['Left', 'right'])` and `event.waitKeys(maxWait = 2.0)`. `getKeys` will only look for a response once, and needs to be embedded into a loop. `waitKeys`is what will take the response you're getting, and I don't believe is saving to the variable you're checking when calculating accuracy. 
* Also, with regards to that code, you're calling the lines `txtFdbkN.draw()` and  `win.flip()` for both conditions. You could more simply put those statements after the if statement just once, since you want to call it no matter what
* Glad you were able to get the trial handler to work and manage your trials, but given that we didn't really cover it in class I would like to see you document it **much** more. 
* The stimuli do overlap with each other. The check you have `targets.setPos = (x+70, y+70)` doesn't work because x and y aren't defined relative to the positions of the other stimuli I don't believe. 
* You re-use code for the practice and main experiment. Try to put repeated code into functions (defs) at minimum, or classes. 
* **Overall:** OK. Got most of it to work, but missing some elements and some aspects not working properly. Have a few coding bugs that are going to cause your code not to work but not for obvious reasons (e.g., using 'Left' instead of 'left'). You have left comments describing indivdiual sections but not neccesarily what the code is doing (e.g., experiment handlers) or how you figured it out. I want to see more documentation, especially for things not covered in class. 

**Accuracy & Efficiency:** 18/25
**Explanation and documentation:** 20/25
**Total:** 38/50

