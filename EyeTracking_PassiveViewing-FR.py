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

exp_info = {"university":"unige", "Num Sujet":"", "session":""}
dlg = gui.DlgFromDict(dictionary = exp_info)
if dlg.OK == False:
    core.quit()

# Parallel port initialization
parallelPortID = 0xD020
portP = parallel.ParallelPort(address = parallelPortID)
portP.setData(0) # resets the port to 0
# Add experiment ID 3 times
ID = 3
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
fname = os.path.expanduser(wd + "\\logfile\\"+ "ET_face_" + exp_info["university"] + "_S" + exp_info["Num Sujet"] + "_" + exp_info["session"] + ".csv")

i=1
while exists(fname) == True:
    print "Logfile name alredy exists"
    fname = os.path.expanduser(wd + "\\logfile\\"+ "ET_face_" + exp_info["university"] + "_S" + exp_info["Num Sujet"] + "_" + exp_info["session"] + str(i) + ".csv")
    i+=1
    
datafile = open(fname, "wb")
writer = csv.writer(datafile, delimiter =";")


# *********************
# ***LANGUAGE SETUP ***
img_instr = visual.TextStim(win)
img_instr.setColor("white")
img_instr.setText("Chaque essai sera constitué d'un signe + qui apparaitra au milieu de l’ecran, suivi d’une paire de visages.\n\nVotre tâche consiste simplement à regarder ces visages, il se peut que nous vous posions des questions concernant ces visages plus tard.\n\nAppuyez sur n'importe quelle touche pour commencer")
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
list_stim = ["F1AN","F1NA","F1HN","F1NH","F1AH","F1HA","F1NN", "F1NN2",
             "F2AN", "F2NA", "F2HN", "F2NH","F2AH","F2HA", "F2NN", "F2NN2",
             "F3AN", "F3NA", "F3HN", "F3NH","F3AH","F3HA", "F3NN", "F3NN2",
             "F5AN", "F5NA", "F5HN", "F5NH", "F5AH", "F5HA", "F5NN", "F5NN2",
             "F6AN", "F6NA", "F6HN", "F6NH", "F6AH", "F6HA", "F6NN", "F6NN2",
             "F7AN", "F7NA", "F7HN", "F7NH", "F7AH", "F7HA", "F7NN", "F7NN2",
             "F8AN", "F8NA", "F8HN", "F8NH", "F8AH", "F8HA", "F8NN", "F8NN2",
             "F9AN", "F9NA", "F9HN", "F9NH", "F9AH", "F9HA", "F9NN", "F9NN2",
             "M1AN","M1NA","M1HN","M1NH", "M1AH", "M1HA","M1NN", "M1NN2",
             "M3AN","M3NA","M3HN","M3NH","M3AH","M3HA","M3NN", "M3NN2",
             "M4AN","M4NA","M4HN","M4NH","M4AH","M4HA","M4NN", "M4NN2",
             "M5AN","M5NA","M5HN","M5NH","M5AH","M5HA","M5NN", "M5NN2",
             "M6AN","M6NA","M6HN","M6NH","M6AH","M6HA","M6NN", "M6NN2",
             "M7AN","M7NA","M7HN","M7NH","M7AH","M7HA","M7NN", "M7NN2"]


list_cond = [1, 2, 3, 4, 5, 6, 7, 7,
             1, 2, 3, 4, 5, 6, 7, 7,
             1, 2, 3, 4, 5, 6, 7, 7,
             1, 2, 3, 4, 5, 6, 7, 7,
             1, 2, 3, 4, 5, 6, 7, 7,
             1, 2, 3, 4, 5, 6, 7, 7,
             1, 2, 3, 4, 5, 6, 7, 7,
             1, 2, 3, 4, 5, 6, 7, 7,
             1, 2, 3, 4, 5, 6, 7, 7]

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
    ft = 2 + uniform(0, 1.5) #Randomisation du temps d'affichage de la croix de fix
    ind = list_stim.index(stim)
    codecond = list_cond[ind]
    fix.draw()
    win.flip()
    core.wait(ft)
    
    #Start picture
    img_stim.setImage(stim+ ".png")
    img_stim.size = (2,2)
    img_stim.draw()
    
    time1 = time.time()
    win.flip()
    portP.setData(codecond)   # Marks begining of stimulation
    core.wait(pic_dur)
    time2 = time.time()
    portP.setData(0)   # Marks ending of stimulation

    writer.writerow([
                    exp_info["university"],
                    exp_info["Num Sujet"],
                    exp_info["session"],
                    stim,
                    str(codecond),
                    time1,
                    time2
                    ])
                    
# Comment for test purposes
#    i +=1
    
#    if i == 3:
#        break
# End Comment for test purposes

stim = visual.TextStim(win)
stim.setColor("white")
stim.setText("Merci, au revoir!")
stim.draw()
win.flip()
core.wait(5.0)
