from psychopy import visual, core, event
win = visual.Window([400,400])
message = visual.TextStim(win, text = 'hello')
message.autoDraw = True
win.flip()
core.wait(2.0)
message.text = 'world'
win.flip()
core.wait(2.0)

#autodraw good to keep the message on until you need it to turn off 


timer = core.Clock() 
x = 0.0
y = 0.0

startTime = timer.getTime()
mouse = event.mouse(visible = true)

while timer.getTime() - startTime < (20.0): #current time subtract startTime 
    x = mouse.getPos()[0]
    y = mouse.getPos()[1]
    message.pos = [x,y]
    win.flip()



