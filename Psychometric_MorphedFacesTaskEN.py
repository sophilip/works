#-*-coding: utf-8-*-
# encoding=utf8  
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
pic_dur = 0.5    # Duration of image display in seconds
tr=0

exp_info = {"university":"unige", "Num Sujet":"", "session":""}
dlg = gui.DlgFromDict(dictionary = exp_info)
if dlg.OK == False:
    core.quit()

# Large display resolution
win = visual.Window(fullscr = True, size=(1920, 1080))
win.mouseVisible = False
img_stim = visual.ImageStim(win)

wd = os.getcwd()
fname = os.path.expanduser(wd + "\\logfile\\"+ "morphFaces_ET_" + exp_info["university"] + "_S" + exp_info["Num Sujet"] + "_" + exp_info["session"] + ".csv")

i=1
while exists(fname) == True:
    print "Logfile name alredy exists"
    fname = os.path.expanduser(wd + "\\logfile\\"+ "morphFaces_ET_" + exp_info["university"] + "_S" + exp_info["Num Sujet"] + "_" + exp_info["session"] + str(i) + ".csv")
    i+=1
    
datafile = open(fname, "wb")
writer = csv.writer(datafile, delimiter =";")

# Parallel port initialization
parallelPortID = 0xD020
portP = parallel.ParallelPort(address = parallelPortID)
# Add experiment ID 3 times
portP.setData(0) # resets the port to 0
portP.setData(7); core.wait(0.1)
portP.setData(0); core.wait(0.1)
portP.setData(7); core.wait(0.1)
portP.setData(0); core.wait(0.1)
portP.setData(7); core.wait(0.1)
portP.setData(0);

# *********************
# ***LANGUAGE SETUP ***

# Load instruction image
img_instr = visual.ImageStim(win)
img_instr.setImage("instruen.png")
#img_instr.size = (2,2)
img_instr.draw()
win.flip()

# Change right left button label
reminder = visual.TextStim(win, alignVert="bottom")
reminder.setColor("White")
reminder.setText("Angry? (<-) or (->) Happy?")
reminder.pos=(0, -0.7)
response_laterality = "AH"

# **********************
# ***START EXPERIMENT***

# Write Logfile Column names
writer.writerow([
                 "university",
                 "subject",
                 "session",
                 "stimulus",
                 "actor",
                 "response_laterality",
                 "key",
                 "response",
                 "morph",
                 "rt",
                 ])

touches= event.waitKeys()
if touches[0]=="escape":
    win.close()
    core.quit()
    event.clearEvents()

list_stim = ["3004_bf_01", "3004_bf_02", "3004_bf_03", "3004_bf_04", "3004_bf_05", "3004_bf_06", "3004_bf_07", "3004_bf_08",
                "3004_bf_09", "3004_bf_10", "3004_bf_11", "3004_bf_12", "3004_bf_13", "3004_bf_14", "3004_bf_15",
                "3005_bm_01", "3005_bm_02", "3005_bm_03", "3005_bm_04", "3005_bm_05", "3005_bm_06", "3005_bm_07", "3005_bm_08",
                "3005_bm_09", "3005_bm_10", "3005_bm_11", "3005_bm_12", "3005_bm_13", "3005_bm_14", "3005_bm_15",
                "3013_wf_01", "3013_wf_02", "3013_wf_03", "3013_wf_04", "3013_wf_05", "3013_wf_06", "3013_wf_07", "3013_wf_08",
                "3013_wf_09", "3013_wf_10", "3013_wf_11", "3013_wf_12", "3013_wf_13", "3013_wf_14", "3013_wf_15",
                "3016_wf_01", "3016_wf_02", "3016_wf_03", "3016_wf_04", "3016_wf_05", "3016_wf_06", "3016_wf_07", "3016_wf_08",
                "3016_wf_09", "3016_wf_10", "3016_wf_11", "3016_wf_12", "3016_wf_13", "3016_wf_14", "3016_wf_15",
                "3021_wf_01", "3021_wf_02", "3021_wf_03", "3021_wf_04", "3021_wf_05", "3021_wf_06", "3021_wf_07", "3021_wf_08",
                "3021_wf_09", "3021_wf_10", "3021_wf_11", "3021_wf_12", "3021_wf_13", "3021_wf_14", "3021_wf_15",
                "3029_bm_01", "3029_bm_02", "3029_bm_03", "3029_bm_04", "3029_bm_05", "3029_bm_06", "3029_bm_07", "3029_bm_08",
                "3029_bm_09", "3029_bm_10", "3029_bm_11", "3029_bm_12", "3029_bm_13", "3029_bm_14", "3029_bm_15",
                "3030_bm_01", "3030_bm_02", "3030_bm_03", "3030_bm_04", "3030_bm_05", "3030_bm_06", "3030_bm_07", "3030_bm_08",
                "3030_bm_09", "3030_bm_10", "3030_bm_11", "3030_bm_12", "3030_bm_13", "3030_bm_14", "3030_bm_15",
                "3031_bm_01", "3031_bm_02", "3031_bm_03", "3031_bm_04", "3031_bm_05", "3031_bm_06", "3031_bm_07", "3031_bm_08",
                "3031_bm_09", "3031_bm_10", "3031_bm_11", "3031_bm_12", "3031_bm_13", "3031_bm_14", "3031_bm_15",
                "3032_bf_01", "3032_bf_02", "3032_bf_03", "3032_bf_04", "3032_bf_05", "3032_bf_06", "3032_bf_07", "3032_bf_08",
                "3032_bf_09", "3032_bf_10", "3032_bf_11", "3032_bf_12", "3032_bf_13", "3032_bf_14", "3032_bf_15",
                "3034_wf_01", "3034_wf_02", "3034_wf_03", "3034_wf_04", "3034_wf_05", "3034_wf_06", "3034_wf_07", "3034_wf_08",
                "3034_wf_09", "3034_wf_10", "3034_wf_11", "3034_wf_12", "3034_wf_13", "3034_wf_14", "3034_wf_15",
                "3038_bf_01", "3038_bf_02", "3038_bf_03", "3038_bf_04", "3038_bf_05", "3038_bf_06", "3038_bf_07", "3038_bf_08",
                "3038_bf_09", "3038_bf_10", "3038_bf_11", "3038_bf_12", "3038_bf_13", "3038_bf_14", "3038_bf_15",
                "3046_bf_01", "3046_bf_02", "3046_bf_03", "3046_bf_04", "3046_bf_05", "3046_bf_06", "3046_bf_07", "3046_bf_08",
                "3046_bf_09", "3046_bf_10", "3046_bf_11", "3046_bf_12", "3046_bf_13", "3046_bf_14", "3046_bf_15",
                "4005_bm_01", "4005_bm_02", "4005_bm_03", "4005_bm_04", "4005_bm_05", "4005_bm_06", "4005_bm_07", "4005_bm_08",
                "4005_bm_09", "4005_bm_10", "4005_bm_11", "4005_bm_12", "4005_bm_13", "4005_bm_14", "4005_bm_15",
                "4012_wm_01", "4012_wm_02", "4012_wm_03", "4012_wm_04", "4012_wm_05", "4012_wm_06", "4012_wm_07", "4012_wm_08",
                "4012_wm_09", "4012_wm_10", "4012_wm_11", "4012_wm_12", "4012_wm_13", "4012_wm_14", "4012_wm_15"]

list_cond = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

stimcond = list(zip(list_stim, list_cond))

shuffle(stimcond)

list_stim, list_cond = zip(*stimcond)

h = 0
j = 1

fix = visual.ImageStim(win)
fix.setImage("fix.png")
fix.size = (2,2)
    
fix.draw()
reminder.draw()
win.flip()
core.wait(3)

for stim in list_stim:
    ft = 1 + uniform(0, 0.5) # Jitter fixation cross
    ind = list_stim.index(stim) # Get index of the stim
    codecond = list_cond[ind] # Get condition number for that stim
    
    # Display fixation
    fix.draw()
    reminder.draw()
    win.flip()
    core.wait(ft)
    
    # Display image 0.5s
    img_stim.setImage(stim+ ".bmp")
    tmp_size = img_stim.size
    img_stim.size *= 1.25

    # img_stim draw
    portP.setData(codecond) # Added swann to add version FR
    img_stim.draw()
    reminder.draw()
    win.flip()
    timeStim = time.time()
    core.wait(pic_dur)
    img_stim.size /= 1.25
    
    # Display fixation while waiting response
    fix.draw()
    reminder.draw()
    win.flip()

    # Get response
    touches = event.waitKeys(15)
    timeRep = time.time()
    tr = (timeRep - timeStim) # Compute TR
    
    if touches == None:
        touches ="None"
        key = "No key"
        tr = None
        rep = None
    if touches[0] =="left":
        key= "left"
        rep = 0
    elif touches[0]=="right":
        key = "right"
        rep = 1
    elif touches in ["q", "escape"]:
        key = "quit"
        win.close()
        core.quit() #quitte si touche "q" ou "ECHAP"
        event.clearEvents()
    
    writer.writerow([
                exp_info["university"],
                exp_info["Num Sujet"],
                exp_info["session"],
                stim,     # "stimulus",
                stim[:4], # "actor",
                response_laterality,
                key,
                rep,
                codecond,
                float(tr),
                 ])
    tr = 0
#    tr2 = []

# Comment for test purposes
#    h += 1
#    if h == 5:
#        break
# End Comment for test purposes


stim = visual.TextStim(win)
stim.setColor("black")
stim.setText("Thank you, take care!")
stim.draw()
win.flip()
core.wait(2.0)
