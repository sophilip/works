#-*-coding: utf-8-*-
import sys, os
import os.path

from os.path import exists

reload(sys)
sys.setdefaultencoding('utf8')

from psychopy import visual, core, event, gui
from random import *
from math import *
import time, csv
from psychopy import parallel


# Init
pic_dur = 5    # Duration of image display in seconds

exp_info = {"university":"unige", "num Sujet":"", "session":""}
dlg = gui.DlgFromDict(dictionary = exp_info)
if dlg.OK == False:
    core.quit()

## Parallel port initialization
parallelPortID = 0xD020
portP = parallel.ParallelPort(address = parallelPortID)
portP.setData(0) # resets the port to 0
## Add experiment ID 3 times
ID = 6
portP.setData(0) # resets the port to 0
portP.setData(ID); core.wait(0.1)
portP.setData(0); core.wait(0.1)
portP.setData(ID); core.wait(0.1)
portP.setData(0); core.wait(0.1)
portP.setData(ID); core.wait(0.1)
portP.setData(0);

#win = visual.Window(fullscr = True)

win = visual.Window(fullscr = True, size=(1920, 1080), color=(0,0,0))
win.mouseVisible = False
img_stim = visual.ImageStim(win)

wd = os.getcwd()
fname = os.path.expanduser(wd + "\\logfile\\"+ "IAPS_" + exp_info["university"] + "_S" + exp_info["num Sujet"] + "_" + exp_info["session"] + ".csv")

i=1
while exists(fname) == True:
    print "Logfile name alredy exists"
    fname = os.path.expanduser(wd + "\\logfile\\"+ "IAPS_" + exp_info["university"] + "_S" + exp_info["num Sujet"] + "_" + exp_info["session"] + str(i) + ".csv")
    i+=1
    
datafile = open(fname, "wb")
writer = csv.writer(datafile, delimiter =";")


# *********************
# ***LANGUAGE SETUP ***
img_instr = visual.TextStim(win)
img_instr.setColor("white")
img_instr.setText("In each trial, a + sign will appear in the center of the screen, followed by three images.\n \n Your task only consists in looking at those images. We might ask you questions about them later.\n \n \n Press any key to start or escape to leave")
img_instr.draw()
win.flip()

touches= event.waitKeys()
if touches[0]=="escape":
    win.close()
    core.quit()
    event.clearEvents()
    
# **********************
# ***START EXPERIMENT***

# Write Logfile Column names
writer.writerow([
                 "university",
                 "subject",
                 "session",
                 "stimuli",
                 "condition",
                 "time_onset",
                 "time_offset"
                 ])
                 
# Write 0 time in logfile
writer.writerow([
                "",
                "",
                "",
                "start",
                "",
                time.time(),
                ""
                ])

#name of stimuli and conditions
list_stim = ["nst1-st1","nst2-st2","nst3-st3","nst4-st4","nst5-st5",
"nst6-st6","nst7-st7","nst8-st8","nst9-st9",
"nst22-st22","nst23-st23","nst24-st24","nst25-st25",
"nst26-st26","nst27-st27","nst28-st28","nst29-st29",
"nsr1-sr1","nsr2-sr2","nsr3-sr3","nsr4-sr4","nsr5-sr5",
"nsr6-sr6","nsr7-sr7","nsr8-sr8","nsr9-sr9","nsr10-sr10","nsr11-sr11",
"st1-nst1","st2-nst2","st3-nst3","st4-nst4","st5-nst5",
"st6-nst6","st7-nst7","st8-nst8","st9-nst9",
"st21-nst21","st22-nst22","st23-nst23","st24-nst24","st25-nst25",
"st26-nst26","st27-nst27","st28-nst28","st29-nst29",
"sr1-nsr1","sr2-nsr2","sr3-nsr3","sr4-nsr4","sr5-nsr5",
"sr6-nsr6","sr7-nsr7","sr8-nsr8","sr9-nsr9","sr10-nsr10","sr11-nsr11"]

list_cond = [1,1,1,1,1,1,1,1,1,
            2,2,2,2,2,2,2,2,2,2,
            3,3,3,3,3,3,3,3,3,3,3,
            4,4,4,4,4,4,4,4,4,
            5,5,5,5,5,5,5,5,5,
            6,6,6,6,6,6,6,6,6,6,6,]

stimcond = list(zip(list_stim, list_cond))

shuffle(stimcond)

list_stim, list_cond = zip(*stimcond)

i = 0
j = 1

fix = visual.ImageStim(win)
fix.setImage("fix.png")
fix.size = (2,2)
    
fix.draw()
win.flip()


for stim in list_stim:
    #Start fixation
    ft = 1 + uniform(0, 1.5) #Randomisation du temps d'affichage de la croix de fix
    ind = list_stim.index(stim)
    codecond = list_cond[ind]
    fix.draw()
    win.flip()
    portP.setData(7)   # Marks onset of fixation cross
    writer.writerow([
                    "",
                    "",
                    "",
                    "",
                    str(7),
                    time.time(),
                    ""
                    ])
    core.wait(ft)
    portP.setData(0)   # Marks offset of fixation cross
    writer.writerow([
                    "",
                    "",
                    "",
                    "",
                    str(0),
                    time.time(),
                    ""
                    ])
    
    #Start picture
    img_stim.setImage(wd + "\\Stimuli\\" +stim+ ".png")
    img_stim.size = (2,2)
    img_stim.draw()
    
    time1 = time.time()
    win.flip()
    portP.setData(codecond)   # Marks beginning of stimulation
    core.wait(pic_dur)
    time2 = time.time()
    portP.setData(0)   # Marks ending of stimulation

    writer.writerow([
                    exp_info["university"],
                    exp_info["num Sujet"],
                    exp_info["session"],
                    stim,
                    str(codecond),
                    time1,
                    time2
                    ])
                    
# Comment for test purposes
#    i +=1
#    
#    if i == 3:
#        break
# End Comment for test purposes

stim = visual.TextStim(win)
stim.setColor("white")
stim.setText("Thank you for your patience")
stim.draw()
win.flip()
core.wait(5.0)