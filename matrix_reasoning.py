#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on January 22, 2021, at 11:14
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'Matrix Reasoning'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='\\\\storage.yale.edu\\home\\DanaSmall-CC1622-Drive\\Small_Lab\\resources, equipment and manuals\\Resources\\Psychopy Tasks\\matrix_reasoning\\matrix_reasoning.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
enter = keyboard.Keyboard()
practice_wais = visual.ImageStim(
    win=win,
    name='practice_wais', 
    image='images/sample.jpg', mask=None,
    ori=0, pos=(0, -110), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
instructions_1 = visual.ImageStim(
    win=win,
    name='instructions_1', 
    image='images/instr.jpg', mask=None,
    ori=0, pos=(0, 350), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
correct_practice = visual.ImageStim(
    win=win,
    name='correct_practice', 
    image='images/instr_corr.jpg', mask=None,
    ori=0, pos=(0,0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
A1 = visual.Rect(
    win=win, name='A1',
    width=(175,175)[0], height=(175,175)[1],
    ori=0, pos=(-362,-317),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=0, depth=-4.0, interpolate=True)
A2 = visual.Rect(
    win=win, name='A2',
    width=(175,175)[0], height=(175,175)[1],
    ori=0, pos=(-181, -317),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=0, depth=-5.0, interpolate=True)
A3 = visual.Rect(
    win=win, name='A3',
    width=(175, 175)[0], height=(175, 175)[1],
    ori=0, pos=(0, -317),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='blue', fillColorSpace='rgb',
    opacity=0, depth=-6.0, interpolate=True)
A4 = visual.Rect(
    win=win, name='A4',
    width=(175,175)[0], height=(175,175)[1],
    ori=0, pos=(181, -317),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='purple', fillColorSpace='rgb',
    opacity=0, depth=-7.0, interpolate=True)
A5 = visual.Rect(
    win=win, name='A5',
    width=(175,175)[0], height=(175,175)[1],
    ori=0, pos=(362, -317),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='pink', fillColorSpace='rgb',
    opacity=0, depth=-8.0, interpolate=True)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "trials"
trialsClock = core.Clock()
image_bottom = visual.ImageStim(
    win=win,
    name='image_bottom', 
    image='sin', mask=None,
    ori=0, pos=(0, -200), size=(913,191),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
trials_image = visual.ImageStim(
    win=win,
    name='trials_image', 
    image='sin', mask=None,
    ori=0, pos=(0,175), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
A1_2 = visual.Rect(
    win=win, name='A1_2',
    width=(175,175)[0], height=(175,175)[1],
    ori=0, pos=(-362,-201),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=0, depth=-2.0, interpolate=True)
A2_2 = visual.Rect(
    win=win, name='A2_2',
    width=(175,175)[0], height=(175,175)[1],
    ori=0, pos=(-181, -201),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=0, depth=-3.0, interpolate=True)
A3_2 = visual.Rect(
    win=win, name='A3_2',
    width=(175, 175)[0], height=(175, 175)[1],
    ori=0, pos=(0, -201),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='blue', fillColorSpace='rgb',
    opacity=0, depth=-4.0, interpolate=True)
A4_2 = visual.Rect(
    win=win, name='A4_2',
    width=(175,175)[0], height=(175,175)[1],
    ori=0, pos=(181, -201),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='purple', fillColorSpace='rgb',
    opacity=0, depth=-5.0, interpolate=True)
A5_2 = visual.Rect(
    win=win, name='A5_2',
    width=(175,175)[0], height=(175,175)[1],
    ori=0, pos=(362, -201),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='pink', fillColorSpace='rgb',
    opacity=0, depth=-6.0, interpolate=True)
mouse_trials = event.Mouse(win=win)
x, y = [None, None]
mouse_trials.mouseClock = core.Clock()
incorrectinrow = 0

# Initialize components for Routine "end"
endClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='You have completed the task :)',
    font='Arial',
    pos=(0, 0), height=20, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
# update component parameters for each repeat
enter.keys = []
enter.rt = []
correct_practice.setOpacity(0)
# setup some python lists for storing info about the mouse
mouse.x = []
mouse.y = []
mouse.leftButton = []
mouse.midButton = []
mouse.rightButton = []
mouse.time = []
mouse.clicked_name = []
gotValidClick = False  # until a click is received
mouse.mouseClock.reset()
# keep track of which components have finished
instructionsComponents = [enter, practice_wais, instructions_1, correct_practice, A1, A2, A3, A4, A5, mouse]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *enter* updates
    waitOnFlip = False
    if enter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enter.frameNStart = frameN  # exact frame index
        enter.tStart = t  # local t and not account for scr refresh
        enter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enter, 'tStartRefresh')  # time at next scr refresh
        enter.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(enter.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enter.status == STARTED and not waitOnFlip:
        theseKeys = enter.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *practice_wais* updates
    if practice_wais.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_wais.frameNStart = frameN  # exact frame index
        practice_wais.tStart = t  # local t and not account for scr refresh
        practice_wais.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_wais, 'tStartRefresh')  # time at next scr refresh
        practice_wais.setAutoDraw(True)
    
    # *instructions_1* updates
    if instructions_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_1.frameNStart = frameN  # exact frame index
        instructions_1.tStart = t  # local t and not account for scr refresh
        instructions_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_1, 'tStartRefresh')  # time at next scr refresh
        instructions_1.setAutoDraw(True)
    
    # *correct_practice* updates
    if correct_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        correct_practice.frameNStart = frameN  # exact frame index
        correct_practice.tStart = t  # local t and not account for scr refresh
        correct_practice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(correct_practice, 'tStartRefresh')  # time at next scr refresh
        correct_practice.setAutoDraw(True)
    
    # *A1* updates
    if A1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        A1.frameNStart = frameN  # exact frame index
        A1.tStart = t  # local t and not account for scr refresh
        A1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(A1, 'tStartRefresh')  # time at next scr refresh
        A1.setAutoDraw(True)
    
    # *A2* updates
    if A2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        A2.frameNStart = frameN  # exact frame index
        A2.tStart = t  # local t and not account for scr refresh
        A2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(A2, 'tStartRefresh')  # time at next scr refresh
        A2.setAutoDraw(True)
    
    # *A3* updates
    if A3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        A3.frameNStart = frameN  # exact frame index
        A3.tStart = t  # local t and not account for scr refresh
        A3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(A3, 'tStartRefresh')  # time at next scr refresh
        A3.setAutoDraw(True)
    
    # *A4* updates
    if A4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        A4.frameNStart = frameN  # exact frame index
        A4.tStart = t  # local t and not account for scr refresh
        A4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(A4, 'tStartRefresh')  # time at next scr refresh
        A4.setAutoDraw(True)
    
    # *A5* updates
    if A5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        A5.frameNStart = frameN  # exact frame index
        A5.tStart = t  # local t and not account for scr refresh
        A5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(A5, 'tStartRefresh')  # time at next scr refresh
        A5.setAutoDraw(True)
    if mouse.isPressedIn(A5):
            correct_practice.opacity = 1
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        mouse.status = STARTED
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [A1, A2, A3, A4, A5]:
                    if obj.contains(mouse):
                        gotValidClick = True
                        mouse.clicked_name.append(obj.name)
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                buttons = mouse.getPressed()
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(mouse.mouseClock.getTime())
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse.x', mouse.x)
thisExp.addData('mouse.y', mouse.y)
thisExp.addData('mouse.leftButton', mouse.leftButton)
thisExp.addData('mouse.midButton', mouse.midButton)
thisExp.addData('mouse.rightButton', mouse.rightButton)
thisExp.addData('mouse.time', mouse.time)
thisExp.addData('mouse.clicked_name', mouse.clicked_name)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cond_images.xlsx'),
    seed=None, name='loop_trials')
thisExp.addLoop(loop_trials)  # add the loop to the experiment
thisLoop_trial = loop_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_trial.rgb)
if thisLoop_trial != None:
    for paramName in thisLoop_trial:
        exec('{} = thisLoop_trial[paramName]'.format(paramName))

for thisLoop_trial in loop_trials:
    currentLoop = loop_trials
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_trial.rgb)
    if thisLoop_trial != None:
        for paramName in thisLoop_trial:
            exec('{} = thisLoop_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trials"-------
    # update component parameters for each repeat
    image_bottom.setImage(imgpath_bottom)
    trials_image.setImage(imgpath_top)
    # setup some python lists for storing info about the mouse_trials
    mouse_trials.x = []
    mouse_trials.y = []
    mouse_trials.leftButton = []
    mouse_trials.midButton = []
    mouse_trials.rightButton = []
    mouse_trials.time = []
    mouse_trials.clicked_name = []
    gotValidClick = False  # until a click is received
    mouse_trials.mouseClock.reset()
    # keep track of which components have finished
    trialsComponents = [image_bottom, trials_image, A1_2, A2_2, A3_2, A4_2, A5_2, mouse_trials]
    for thisComponent in trialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trials"-------
    while continueRoutine:
        # get current time
        t = trialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_bottom* updates
        if image_bottom.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_bottom.frameNStart = frameN  # exact frame index
            image_bottom.tStart = t  # local t and not account for scr refresh
            image_bottom.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_bottom, 'tStartRefresh')  # time at next scr refresh
            image_bottom.setAutoDraw(True)
        
        # *trials_image* updates
        if trials_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trials_image.frameNStart = frameN  # exact frame index
            trials_image.tStart = t  # local t and not account for scr refresh
            trials_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trials_image, 'tStartRefresh')  # time at next scr refresh
            trials_image.setAutoDraw(True)
        
        # *A1_2* updates
        if A1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            A1_2.frameNStart = frameN  # exact frame index
            A1_2.tStart = t  # local t and not account for scr refresh
            A1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A1_2, 'tStartRefresh')  # time at next scr refresh
            A1_2.setAutoDraw(True)
        
        # *A2_2* updates
        if A2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            A2_2.frameNStart = frameN  # exact frame index
            A2_2.tStart = t  # local t and not account for scr refresh
            A2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A2_2, 'tStartRefresh')  # time at next scr refresh
            A2_2.setAutoDraw(True)
        
        # *A3_2* updates
        if A3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            A3_2.frameNStart = frameN  # exact frame index
            A3_2.tStart = t  # local t and not account for scr refresh
            A3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A3_2, 'tStartRefresh')  # time at next scr refresh
            A3_2.setAutoDraw(True)
        
        # *A4_2* updates
        if A4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            A4_2.frameNStart = frameN  # exact frame index
            A4_2.tStart = t  # local t and not account for scr refresh
            A4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A4_2, 'tStartRefresh')  # time at next scr refresh
            A4_2.setAutoDraw(True)
        
        # *A5_2* updates
        if A5_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            A5_2.frameNStart = frameN  # exact frame index
            A5_2.tStart = t  # local t and not account for scr refresh
            A5_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A5_2, 'tStartRefresh')  # time at next scr refresh
            A5_2.setAutoDraw(True)
        # *mouse_trials* updates
        if mouse_trials.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_trials.frameNStart = frameN  # exact frame index
            mouse_trials.tStart = t  # local t and not account for scr refresh
            mouse_trials.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_trials, 'tStartRefresh')  # time at next scr refresh
            mouse_trials.status = STARTED
            prevButtonState = mouse_trials.getPressed()  # if button is down already this ISN'T a new click
        if mouse_trials.status == STARTED:  # only update if started and not finished!
            buttons = mouse_trials.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [A1_2, A2_2, A3_2, A4_2, A5_2]:
                        if obj.contains(mouse_trials):
                            gotValidClick = True
                            mouse_trials.clicked_name.append(obj.name)
                    x, y = mouse_trials.getPos()
                    mouse_trials.x.append(x)
                    mouse_trials.y.append(y)
                    buttons = mouse_trials.getPressed()
                    mouse_trials.leftButton.append(buttons[0])
                    mouse_trials.midButton.append(buttons[1])
                    mouse_trials.rightButton.append(buttons[2])
                    mouse_trials.time.append(mouse_trials.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trials"-------
    for thisComponent in trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_trials.addData('trials_image.started', trials_image.tStartRefresh)
    loop_trials.addData('trials_image.stopped', trials_image.tStopRefresh)
    # store data for loop_trials (TrialHandler)
    if len(mouse_trials.x): loop_trials.addData('mouse_trials.x', mouse_trials.x[0])
    if len(mouse_trials.y): loop_trials.addData('mouse_trials.y', mouse_trials.y[0])
    if len(mouse_trials.leftButton): loop_trials.addData('mouse_trials.leftButton', mouse_trials.leftButton[0])
    if len(mouse_trials.midButton): loop_trials.addData('mouse_trials.midButton', mouse_trials.midButton[0])
    if len(mouse_trials.rightButton): loop_trials.addData('mouse_trials.rightButton', mouse_trials.rightButton[0])
    if len(mouse_trials.time): loop_trials.addData('mouse_trials.time', mouse_trials.time[0])
    if len(mouse_trials.clicked_name): loop_trials.addData('mouse_trials.clicked_name', mouse_trials.clicked_name[0])
    if mouse_trials.clicked_name[0] == corrans:
        incorrectinrow = 0
    
    else:
        incorrectinrow += 1
        
    if incorrectinrow == 3:
        loop_trials.finished = True
    # the Routine "trials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop_trials'


# ------Prepare to start Routine "end"-------
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [text]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
