from psychopy import visual, core, event, clock

win = visual.Window([1024, 768], fullscr=False)
RT_clock = core.Clock()

fixCross = visual.TextStim (win, text = '+', color = 'white')
fixCross.draw()
win.flip()
core.wait(1)
Go = visual.TextStim (win, text = "GO!", color = 'white')
Go.draw()
win.flip()
response = event.waitKeys(keyList = 'space')
rt = RT_clock.getTime()
RTscreen = visual.TextStim(win, text = rt, color = 'white')
RTscreen.draw()
win.flip()
core.wait(30)


