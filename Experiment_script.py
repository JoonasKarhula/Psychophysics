#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on December 13, 2021, at 18:59
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Final'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
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
    originPath='F:\\New folder\\Psychophysics\\TrueFinal(60Hz)\\TrueFinal.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
Instruction_text = visual.TextStim(win=win, name='Instruction_text',
    text="After a period of time, either a blue or a purple arrow appears either on the left or the right side of the screen. Respond as quickly as possible according to rules below: \n\nIf a purple arrow points to the side of the screen it appears on, press arrow key to that direction. (e.g. purple arrow pointing right on the right side of the screen = press right)\n\nIf a blue arrow points to the middle of the screen, press arrow key to the direction of the arrow's tip. (e.g. blue arrow pointing left on the right side of the screen = press left)\n\nDo not press anything if neither of the conditions are met.\n\nFixation cross marks a beginning of a new trial!\n\nIf you understood press space bar and the experiment will start.",
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Instruction_resp = keyboard.Keyboard()

# Initialize components for Routine "Experiment"
ExperimentClock = core.Clock()
Fixation = visual.TextStim(win=win, name='Fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Stimulusarrow = visual.ImageStim(
    win=win,
    name='Stimulusarrow', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Backmask = visual.NoiseStim(
    win=win, name='Backmask',
    noiseImage=None, mask=None,
    ori=0.0, pos=[0,0], size=(0.5, 0.5), sf=None,
    phase=0.0,
    color=[1,1,1], colorSpace='rgb',     opacity=None, blendmode='avg', contrast=0.15,
    texRes=128, filter=None,
    noiseType='Binary', noiseElementSize=[0.0625], 
    noiseBaseSf=8.0, noiseBW=1.0,
    noiseBWO=30.0, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-2.0)
Backmask.buildNoise()
Frontmask = visual.NoiseStim(
    win=win, name='Frontmask',
    noiseImage=None, mask=None,
    ori=0.0, pos=[0,0], size=(0.5, 0.5), sf=None,
    phase=0.0,
    color=[1,1,1], colorSpace='rgb',     opacity=None, blendmode='avg', contrast=0.15,
    texRes=128, filter=None,
    noiseType='Binary', noiseElementSize=[0.0625], 
    noiseBaseSf=8.0, noiseBW=1.0,
    noiseBWO=30.0, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-3.0)
Frontmask.buildNoise()
Primerarrow = visual.ImageStim(
    win=win,
    name='Primerarrow', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
Response = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
Instruction_resp.keys = []
Instruction_resp.rt = []
_Instruction_resp_allKeys = []
# keep track of which components have finished
InstructionsComponents = [Instruction_text, Instruction_resp]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruction_text* updates
    if Instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruction_text.frameNStart = frameN  # exact frame index
        Instruction_text.tStart = t  # local t and not account for scr refresh
        Instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruction_text, 'tStartRefresh')  # time at next scr refresh
        Instruction_text.setAutoDraw(True)
    
    # *Instruction_resp* updates
    waitOnFlip = False
    if Instruction_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruction_resp.frameNStart = frameN  # exact frame index
        Instruction_resp.tStart = t  # local t and not account for scr refresh
        Instruction_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruction_resp, 'tStartRefresh')  # time at next scr refresh
        Instruction_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Instruction_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Instruction_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Instruction_resp.status == STARTED and not waitOnFlip:
        theseKeys = Instruction_resp.getKeys(keyList=['space'], waitRelease=False)
        _Instruction_resp_allKeys.extend(theseKeys)
        if len(_Instruction_resp_allKeys):
            Instruction_resp.keys = _Instruction_resp_allKeys[-1].name  # just the last key pressed
            Instruction_resp.rt = _Instruction_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instruction_text.started', Instruction_text.tStartRefresh)
thisExp.addData('Instruction_text.stopped', Instruction_text.tStopRefresh)
# check responses
if Instruction_resp.keys in ['', [], None]:  # No response was made
    Instruction_resp.keys = None
thisExp.addData('Instruction_resp.keys',Instruction_resp.keys)
if Instruction_resp.keys != None:  # we had a response
    thisExp.addData('Instruction_resp.rt', Instruction_resp.rt)
thisExp.addData('Instruction_resp.started', Instruction_resp.tStartRefresh)
thisExp.addData('Instruction_resp.stopped', Instruction_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Exp_loop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Conditions_Truefinal.xlsx'),
    seed=None, name='Exp_loop')
thisExp.addLoop(Exp_loop)  # add the loop to the experiment
thisExp_loop = Exp_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisExp_loop.rgb)
if thisExp_loop != None:
    for paramName in thisExp_loop:
        exec('{} = thisExp_loop[paramName]'.format(paramName))

for thisExp_loop in Exp_loop:
    currentLoop = Exp_loop
    # abbreviate parameter names if possible (e.g. rgb = thisExp_loop.rgb)
    if thisExp_loop != None:
        for paramName in thisExp_loop:
            exec('{} = thisExp_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Experiment"-------
    continueRoutine = True
    # update component parameters for each repeat
    Stimulusarrow.setOpacity(clrop)
    Stimulusarrow.setPos(coord)
    Stimulusarrow.setImage(imagefilestim)
    Backmask.setPos(coord)
    Frontmask.setPos(coord)
    Primerarrow.setOpacity(primop)
    Primerarrow.setPos(coord)
    Primerarrow.setImage(imagefileprim)
    Response.keys = []
    Response.rt = []
    _Response_allKeys = []
    # keep track of which components have finished
    ExperimentComponents = [Fixation, Stimulusarrow, Backmask, Frontmask, Primerarrow, Response]
    for thisComponent in ExperimentComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ExperimentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Experiment"-------
    while continueRoutine:
        # get current time
        t = ExperimentClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ExperimentClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and frameN >= 0.0:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            if frameN >= 30:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(False)
        
        # *Stimulusarrow* updates
        if Stimulusarrow.status == NOT_STARTED and frameN >= 33+onst:
            # keep track of start time/frame for later
            Stimulusarrow.frameNStart = frameN  # exact frame index
            Stimulusarrow.tStart = t  # local t and not account for scr refresh
            Stimulusarrow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stimulusarrow, 'tStartRefresh')  # time at next scr refresh
            Stimulusarrow.setAutoDraw(True)
        if Stimulusarrow.status == STARTED:
            if frameN >= 33+onst+2:
                # keep track of stop time/frame for later
                Stimulusarrow.tStop = t  # not accounting for scr refresh
                Stimulusarrow.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Stimulusarrow, 'tStopRefresh')  # time at next scr refresh
                Stimulusarrow.setAutoDraw(False)
        
        # *Backmask* updates
        if Backmask.status == NOT_STARTED and frameN >= 32+onst:
            # keep track of start time/frame for later
            Backmask.frameNStart = frameN  # exact frame index
            Backmask.tStart = t  # local t and not account for scr refresh
            Backmask.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Backmask, 'tStartRefresh')  # time at next scr refresh
            Backmask.setAutoDraw(True)
        if Backmask.status == STARTED:
            if frameN >= 32+onst+1:
                # keep track of stop time/frame for later
                Backmask.tStop = t  # not accounting for scr refresh
                Backmask.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Backmask, 'tStopRefresh')  # time at next scr refresh
                Backmask.setAutoDraw(False)
        if Backmask.status == STARTED:
            if Backmask._needBuild:
                Backmask.buildNoise()
        
        # *Frontmask* updates
        if Frontmask.status == NOT_STARTED and frameN >= 30+onst:
            # keep track of start time/frame for later
            Frontmask.frameNStart = frameN  # exact frame index
            Frontmask.tStart = t  # local t and not account for scr refresh
            Frontmask.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Frontmask, 'tStartRefresh')  # time at next scr refresh
            Frontmask.setAutoDraw(True)
        if Frontmask.status == STARTED:
            if frameN >= 30+onst+1:
                # keep track of stop time/frame for later
                Frontmask.tStop = t  # not accounting for scr refresh
                Frontmask.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Frontmask, 'tStopRefresh')  # time at next scr refresh
                Frontmask.setAutoDraw(False)
        if Frontmask.status == STARTED:
            if Frontmask._needBuild:
                Frontmask.buildNoise()
        
        # *Primerarrow* updates
        if Primerarrow.status == NOT_STARTED and frameN >= 31+onst:
            # keep track of start time/frame for later
            Primerarrow.frameNStart = frameN  # exact frame index
            Primerarrow.tStart = t  # local t and not account for scr refresh
            Primerarrow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Primerarrow, 'tStartRefresh')  # time at next scr refresh
            Primerarrow.setAutoDraw(True)
        if Primerarrow.status == STARTED:
            if frameN >= 31+onst+1:
                # keep track of stop time/frame for later
                Primerarrow.tStop = t  # not accounting for scr refresh
                Primerarrow.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Primerarrow, 'tStopRefresh')  # time at next scr refresh
                Primerarrow.setAutoDraw(False)
        
        # *Response* updates
        waitOnFlip = False
        if Response.status == NOT_STARTED and frameN >= 33+onst:
            # keep track of start time/frame for later
            Response.frameNStart = frameN  # exact frame index
            Response.tStart = t  # local t and not account for scr refresh
            Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response, 'tStartRefresh')  # time at next scr refresh
            Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Response.status == STARTED:
            if frameN >= 33+onst+90:
                # keep track of stop time/frame for later
                Response.tStop = t  # not accounting for scr refresh
                Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Response, 'tStopRefresh')  # time at next scr refresh
                Response.status = FINISHED
        if Response.status == STARTED and not waitOnFlip:
            theseKeys = Response.getKeys(keyList=['left', 'right'], waitRelease=False)
            _Response_allKeys.extend(theseKeys)
            if len(_Response_allKeys):
                Response.keys = _Response_allKeys[-1].name  # just the last key pressed
                Response.rt = _Response_allKeys[-1].rt
                # was this correct?
                if (Response.keys == str(correc)) or (Response.keys == correc):
                    Response.corr = 1
                else:
                    Response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ExperimentComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Experiment"-------
    for thisComponent in ExperimentComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Exp_loop.addData('Fixation.started', Fixation.tStartRefresh)
    Exp_loop.addData('Fixation.stopped', Fixation.tStopRefresh)
    Exp_loop.addData('Stimulusarrow.started', Stimulusarrow.tStartRefresh)
    Exp_loop.addData('Stimulusarrow.stopped', Stimulusarrow.tStopRefresh)
    Exp_loop.addData('Backmask.started', Backmask.tStartRefresh)
    Exp_loop.addData('Backmask.stopped', Backmask.tStopRefresh)
    Exp_loop.addData('Frontmask.started', Frontmask.tStartRefresh)
    Exp_loop.addData('Frontmask.stopped', Frontmask.tStopRefresh)
    Exp_loop.addData('Primerarrow.started', Primerarrow.tStartRefresh)
    Exp_loop.addData('Primerarrow.stopped', Primerarrow.tStopRefresh)
    # check responses
    if Response.keys in ['', [], None]:  # No response was made
        Response.keys = None
        # was no response the correct answer?!
        if str(correc).lower() == 'none':
           Response.corr = 1;  # correct non-response
        else:
           Response.corr = 0;  # failed to respond (incorrectly)
    # store data for Exp_loop (TrialHandler)
    Exp_loop.addData('Response.keys',Response.keys)
    Exp_loop.addData('Response.corr', Response.corr)
    if Response.keys != None:  # we had a response
        Exp_loop.addData('Response.rt', Response.rt)
    Exp_loop.addData('Response.started', Response.tStartRefresh)
    Exp_loop.addData('Response.stopped', Response.tStopRefresh)
    # the Routine "Experiment" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Exp_loop'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
