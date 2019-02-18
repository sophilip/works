#-*-coding: utf-8-*-
import sys, os
import os.path

from os.path import exists

reload(sys)
sys.setdefaultencoding('utf8')

from psychopy import visual, core, event, gui

from math import *
import time, csv

from random import *
import random
from psychopy import parallel


# Init
pic_dur = 8    # Duration of image display in seconds

exp_info = {"university":"unige", "Num Sujet":"", "session":""}
dlg = gui.DlgFromDict(dictionary = exp_info)
if dlg.OK == False:
    core.quit()
#
parallelPortID = 0xD020
portP = parallel.ParallelPort(address = parallelPortID)
portP.setData(0) # resets the port to 0

#Correspondance sheet for Eyelink
trigeyelink = 0
while trigeyelink < 32:
    portP.setData(trigeyelink)
    time.sleep(0.1) # wait 50ms between each iteration
    portP.setData(0)
    trigeyelink += 1

# Add experiment ID 3 times
core.wait(2)
portP.setData(0);
portP.setData(8); core.wait(0.1)
portP.setData(0); core.wait(0.1)
portP.setData(8); core.wait(0.1)
portP.setData(0); core.wait(0.1)
portP.setData(8); core.wait(0.1)
portP.setData(0);

#win = visual.Window(fullscr = True)

win = visual.Window(fullscr = True, size=(1680, 1050), color=(0,0,0))
win.mouseVisible = False
img_stim = visual.ImageStim(win)

wd = os.getcwd()
fname = os.path.expanduser(wd + "\\logfile\\"+ "ReappraisalTask_" + exp_info["university"] + "_S" + exp_info["Num Sujet"] + "_" + exp_info["session"] + "_dataset1.csv")

i=1
while exists(fname) == True:
    print "Logfile name alredy exists"
    fname = os.path.expanduser(wd + "\\logfile\\"+ "ReappraisalTask_" + exp_info["university"] + "_S" + exp_info["Num Sujet"] + "_" + exp_info["session"] + str(i) + "_dataset1.csv")
    i+=1
    
datafile = open(fname, "wb")
writer = csv.writer(datafile, delimiter =";")

# *********************
# ***LANGUAGE SETUP ***

# Load instruction image
img_instr = visual.ImageStim(win)
img_instr.setImage("instru.png")
#img_instr.size = (2,2)
img_instr.draw()
win.flip()

# Change right left button label
touches= event.waitKeys()
if touches[0]=="escape":
    win.close()
    core.quit()
    event.clearEvents()
    
    
# **********************
# ***START EXPERIMENT***
#Changer les trucs dans les "" pour changer les noms des colonnes du csv
writer.writerow([
                 "university",
                 "subject",
                 "session",
                 "dataset",
                 "stimulus",
                 "iaps_ID",
                 "iaps_intensity",
                 "response_idx",
                 "codecond",
                 "instr",
                 "rt",
                 "time_onset",
                 "time_offset"
                 ])
                 

# Add 0 time
writer.writerow([
                 "university",
                 "subject",
                 "session",
                 "start",
                 "",
                 "",
                 "",
                 "",
                 "",
                 time.time(),
                 "",
                 "",
                 ])

list_stim1 = ["LN1.1", "LN2.1", "LN3.1","LN4.1","LN5.1","LN6.1","LN7.1","LN8.1","LN9.1","LN10.1", "LN11.1", "LN12.1", "LN13.1", "LN14.1", "LN15.1", "LN16.1", "LN17.1","LN18.1"]
list_stim2 = ["LNG1.1", "LNG2.1", "LNG3.1","LNG4.1","LNG5.1","LNG6.1","LNG7.1","LNG8.1","LNG9.1","LNG10.1", "LNG11.1", "LNG12.1", "LNG13.1", "LNG14.1", "LNG15.1", "LNG16.1", "LNG17.1","LNG18.1"]
list_stim3 = ["RNG1.1", "RNG2.1", "RNG3.1","RNG4.1","RNG5.1","RNG6.1","RNG7.1","RNG8.1","RNG9.1","RNG10.1", "RNG11.1", "RNG12.1", "RNG13.1", "RNG14.1", "RNG15.1", "RNG16.1", "RNG17.1","RNG18.1"]

# Please use integers NOT strings to send trigger codes
list_cond1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
list_cond2 = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
list_cond3 = [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]

list_iaps_ID1 = [5535,5740,7002,7036,7041,7052,7090,7100,7150,2190,2191,2235,2270,2320,2397,2435,2495,2499]
list_iaps_ID2 = [9412,9491,9480,2141,2799,3215,3120,9120,3063,9600,3140,1525,3010,6211,3053,2095,2276,2278]
list_iaps_ID3 = [2703,2730,2750,2800,5973,8485,9050,3230,9471,3015,9611,3062,2811,3030,6230,6244,6260,6315]

list_iaps_intensity1 = [4.11,2.59,3.16,3.32,2.6,3.01,2.61,2.89,2.61,2.41,3.61,3.36,3.15,2.9,2.77,3.94,3.19,3.08]
list_iaps_intensity2 = [6.72,5.69,5.57,5,5.02,5.44,6.84,5.77,6.35,6.46,6.36,6.51,7.16,5.9,6.96,5.25,4.63,4.55]
list_iaps_intensity3 = [5.78,6.8,4.31,5.49,5.78,6.46,6.36,5.41,4.48,5.9,5.75,5.78,6.9,6.76,7.35,5.44,6.93,6.38]

list_instr1 = ["Regardez","Regardez","Regardez","Regardez","Regardez","Regardez","Regardez","Regardez","Regardez","Regardez","Regardez","Regardez","Regardez","Regardez","Regardez","Regardez","Regardez","Regardez"]
list_instr2 = ["Regardez","Regardez","Regardez","Regardez","Regardez","Regardez","Regardez","Regardez","Regardez","Regardez","Regardez","Regardez","Regardez","Regardez","Regardez","Regardez","Regardez","Regardez"]
list_instr3 = ["Diminuez","Diminuez","Diminuez","Diminuez","Diminuez","Diminuez","Diminuez","Diminuez","Diminuez","Diminuez","Diminuez","Diminuez","Diminuez","Diminuez","Diminuez","Diminuez","Diminuez","Diminuez"]

stimcond1 = list(zip(list_stim1, list_instr1, list_cond1, list_iaps_ID1, list_iaps_intensity1))
stimcond2 = list(zip(list_stim2, list_instr2, list_cond2, list_iaps_ID2, list_iaps_intensity2))
stimcond3 = list(zip(list_stim3, list_instr3, list_cond3, list_iaps_ID3, list_iaps_intensity3))

shuffle(stimcond1)
shuffle(stimcond2)
shuffle(stimcond3)

# print stimcond1


list_stim1, list_instr1, list_cond1, list_iaps_ID1, list_iaps_intensity1 = zip(*stimcond1)
list_stim2, list_instr2, list_cond2, list_iaps_ID2, list_iaps_intensity2 = zip(*stimcond2)
list_stim3, list_instr3, list_cond3, list_iaps_ID3, list_iaps_intensity3 = zip(*stimcond3)

h = 0
j = 1
list_stim=[]
list_cond=[]
list_instr=[]
list_iaps_ID=[]
list_iaps_intensity=[]

choices_lbl=["Très faible","","faible","","Modérée","","Forte","","Très forte"]
#choices_lbl1=["Strat. 1","Strat. 2", "Strat. 3", "Other strat."]
# choices_idx=[1,2,3,4,5]
# choice_tab = list(zip(choices_lbl, choices_idx))

affect = visual.TextStim(win, alignVert="center")
affect.setColor("White")
affect.setText("Quelle est l'intensité de vos émotions négatives?")

#strategy = visual.TextStim(win, alignVert="center")
#strategy.setColor("white")
#strategy.setText("Which Strategy did you use?")

fix = visual.ImageStim(win)
fix.setImage("fix.png")
fix.size = (2,2)
    
fix.draw()
win.flip()
core.wait(0.5)

modalities = ["1","2","3", "1","2","3", "1","2","3", "1","2","3", "1","2","3", "1","2","3"]
shuffle(modalities)

idx1=0; idx2 = 0; idx3 = 0
bloc_len = 6

for moda in modalities:
    print moda
    if moda == "1":
        list_stim += list_stim1[idx1:idx1+bloc_len]
        list_instr += list_instr1[idx1:idx1+bloc_len]
        list_cond += list_cond1[idx1:idx1+bloc_len]
        list_iaps_ID += list_iaps_ID1[idx1:idx1+bloc_len]
        list_iaps_intensity += list_iaps_intensity1[idx1:idx1+bloc_len]

        idx1+=bloc_len
    elif moda == "2":
        list_stim += list_stim2[idx2:idx2+bloc_len]
        list_instr += list_instr2[idx2:idx2+bloc_len]
        list_cond += list_cond2[idx2:idx2+bloc_len]
        list_iaps_ID += list_iaps_ID2[idx2:idx2+bloc_len]
        list_iaps_intensity += list_iaps_intensity2[idx2:idx2+bloc_len]
        idx2+=bloc_len

    elif moda == "3":
        list_stim += list_stim3[idx3:idx3+bloc_len]
        list_instr += list_instr3[idx3:idx3+bloc_len]
        list_cond += list_cond3[idx3:idx3+bloc_len]
        list_iaps_ID += list_iaps_ID3[idx3:idx3+bloc_len]
        list_iaps_intensity += list_iaps_intensity3[idx3:idx3+bloc_len]
        idx3+=bloc_len

h = 0
for stim in list_stim:
    ind = list_stim.index(stim)
    instr = list_instr[ind]
    codecond = list_cond[ind]
    iaps_ID = list_iaps_ID[ind]
    iaps_intensity = list_iaps_intensity[ind]

    print(stim)
    # Displat fixation cross (2-4s)
    ft = 2 + uniform(0, 2) #Randomisation du temps d'affichage de la croix de fix
    fix.draw()
    win.flip()
    core.wait(ft)

    # Display cue (2s)
    img_cue = visual.TextStim(win, alignVert="center")
    img_cue.setColor("White")
    img_cue.setText(instr)
    img_cue.draw()
    win.flip()
    core.wait(2)
    
    # Display image (8s)
    img_stim.setImage(wd + "\\Ressources\\IAPS Groupe 1\\" + stim+ ".jpg")
    img_stim.draw()
    win.flip()
            
    portP.setData(codecond)
    time1 = time.time()
    core.wait(pic_dur)
    time2 = time.time()
    portP.setData(0)

    # Display fixation (2s)
    fix.draw()
    win.flip()
    core.wait(2)

    # Display rating scale
    rating = None; rt = None; choiceHistory = None; rating_idx = None
    ratingScale = visual.RatingScale(win, mouseOnly=True, low =1, high = 10, choices=choices_lbl, stretch = 2)
    item = affect
    while ratingScale.noResponse:
        item.draw()
        ratingScale.draw()
        win.flip()
    rating = ratingScale.getRating()
    rt = ratingScale.getRT()
    choiceHistory = ratingScale.getHistory()
    rating_idx = choices_lbl.index(rating)+1 # Get index of the stim (index start at 0 in python)

    # Write logfile
    writer.writerow([
                        exp_info["university"],
                        exp_info["Num Sujet"],
                        exp_info["session"],
                        "dataset1",
                        stim,
                        iaps_ID,
                        iaps_intensity,
                        rating_idx,
                        str(codecond),
                        instr,
                        rt,
                        time1,
                        time2
                        ])

# Comment for test purposes
#    h += 1
#    if h == 1:
#        break
# End Comment for test purposes