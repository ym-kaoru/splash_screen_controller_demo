# -*- coding: utf-8 -*-
import os
import sys


class OpenCloseController(object):

    def __init__(self, activity, pending_tasks, timer_tasks):
        super(OpenCloseController, self).__init__()
        self.activity = activity
        self.pending_tasks = pending_tasks
        self.timer_tasks = timer_tasks
        self.state_machine = None
        self.constructStateMachine()

    def onCreate(self, saved_instance_state):
        self.prepareStateMachine(True, saved_instance_state)
        #self.state_machine.onCreate(saved_instance_state)

    def onStart(self):
        pass

    def onResume(self):
        # self.state_machine.onResume()
        pass

    def onPause(self):
        # self.state_machine.onPause()
        pass

    def isResumed(self):
        return self.activity.isResumed()

    def onSaveInstanceState(self, out_instance_state):
        self.saveStateMachine(out_instance_state)

    def onStop(self):
        pass

    def onDestroy(self):
        pass

    def showAntenna(self):
        pass

    def hideAntenna(self):
        pass

    # TODO: Add or customize action handlers here.

    def post(self, action):
        self.pending_tasks.append(action)
        return action

    def postDelayed(self, action, delayMillis):
        self.timer_tasks.append(action)
        return action

    def removeCallbacks(self, task_id):
        self.pending_tasks[:] = [action for action in self.pending_tasks if action != task_id]
        self.timer_tasks[:] = [action for action in self.timer_tasks if action != task_id]

    def constructStateMachine(self):
        self.state_machine = OpenCloseStateMachine(self)

    # %%

    #
    # 以下の行は自動生成されているので直接編集しないでください。
    #
    # Generated by View Generator
    #

    def prepareStateMachine(self, debug_flag, saved_instance_state):
        self.state_machine.setDebugFlag(debug_flag)
        if (saved_instance_state is not None) and ('state_machine' in saved_instance_state):
            self.state_machine.restoreInstanceState(saved_instance_state['state_machine'])
        else:
            self.state_machine.enterStartState()

    def saveStateMachine(self, out_instance_state):
        out_instance_state['state_machine'] = {}
        self.state_machine.saveInstanceState(out_instance_state['state_machine'])

    # Public method for OpenCloseStateMachine

    def open(self, animated):
        self.state_machine.open(animated)

    def close(self, animated):
        self.state_machine.close(animated)

    def toggle(self, animated):
        self.state_machine.toggle(animated)

    def startToOpen(self):
        self.state_machine.startToOpen()

    def startToClose(self):
        self.state_machine.startToClose()


class OpenCloseStateMachine(object):

    class_instance_counter = 0

    ENTRY_POINT = 0
    CLOSED = 1
    OPEN = 2
    ANIMATING_CLOSE_TO_OPEN = 3
    ANIMATING_OPEN_TO_CLOSE = 4

    GROUP_ANTENNA_INVISIBLE = 0
    GROUP_ANTENNA_VISIBLE = 1
    GROUP_IN_TRANSITION = 2

    def __init__(self, parent_context):
        super(OpenCloseStateMachine, self).__init__()
        self.instance_index = OpenCloseStateMachine.class_instance_counter
        OpenCloseStateMachine.class_instance_counter += 1
        self.parent_context = parent_context
        self.mDebugFlag = False
        self.mInTransition = False
        self.mCurrentState = 0
        self.mGroupState = [False, False, False]
        self.mPendingState = 0
        self.mPendingEvent = None
        self.mPendingPriority = 0
        self.mDebugLevel = 2

    def getCurrentState(self):
        return self.mCurrentState

    def getCurrentStateName(self):
        return OpenCloseStateMachine.STATE_TABLE[self.mCurrentState]

    def setCurrentState(self, state):
        self.mCurrentState = state
        self.clearPendingState()
        self.debugPrintCurrentState('ENTER STATE')

    def debugPrintCurrentState(self, msg):
        state = self.mCurrentState
        if self.mDebugFlag and state < len(OpenCloseStateMachine.STATE_TABLE):
            print "OpenCloseStateMachine(%d): %s: %s" % (self.instance_index, msg, OpenCloseStateMachine.STATE_TABLE[state])

    def clearPendingState(self):
        self.mPendingEvent = None
        self.mPendingPriority = 0
        self.mPendingState = 0

    def isInTransition(self):
        return self.mInTransition

    def isDebugFlag(self):
        return self.mDebugFlag

    def setDebugFlag(self, debugFlag):
        self.mDebugFlag = debugFlag

    def getDebugLevel(self):
        return self.mDebugLevel

    def setDebugLevel(self, debugLevel):
        self.mDebugLevel = debugLevel

    def enterStartState(self):
        self.debugPrintCurrentState('START STATE')
        self.clearPendingState()

    def evaluatePendingCondition(self):
        if self.mPendingEvent is None or self.mPendingState == 0:
            return

    def saveInstanceState(self, out_instance_state):
        while True:
            break

        out_instance_state['mCurrentState'] = self.mCurrentState
        out_instance_state['mGroupState'] = self.mGroupState
        self.debugPrintCurrentState('SAVE STATE')

    def restoreInstanceState(self, saved_instance_state):
        self.mCurrentState = saved_instance_state['mCurrentState']
        self.mGroupState = saved_instance_state['mGroupState']
        self.debugPrintCurrentState('RESTORE STATE')

        while True:
            break

    def open(self, animated):
        if self.mInTransition:
            raise RuntimeError("inTransition must be false. HINT: Use postOpen.")

        self.evaluatePendingCondition()

        self.mInTransition = True

        try:
            if self.getDebugLevel() >= 2:
                print '  open'

            while True:
                if self.mCurrentState == OpenCloseStateMachine.CLOSED:
                    if animated:
                        # Leave group ANTENNA_INVISIBLE
                        self.mGroupState[OpenCloseStateMachine.GROUP_ANTENNA_INVISIBLE] = False
                        self.setCurrentState(OpenCloseStateMachine.ANIMATING_CLOSE_TO_OPEN)
                        self.parent_context.startAnimationCloseToOpen()
                        # Enter group ANTENNA_VISIBLE
                        self.mGroupState[OpenCloseStateMachine.GROUP_ANTENNA_VISIBLE] = True
                        self.parent_context.showAntenna()
                        # Enter group IN_TRANSITION
                        self.mGroupState[OpenCloseStateMachine.GROUP_IN_TRANSITION] = True
                        self.parent_context.setAnimating(True)
                    else:
                        # Leave group ANTENNA_INVISIBLE
                        self.mGroupState[OpenCloseStateMachine.GROUP_ANTENNA_INVISIBLE] = False
                        self.setCurrentState(OpenCloseStateMachine.OPEN)
                        # Enter group ANTENNA_VISIBLE
                        self.mGroupState[OpenCloseStateMachine.GROUP_ANTENNA_VISIBLE] = True
                        self.parent_context.showAntenna()
                    break

                # default
                break

        finally:
            self.mInTransition = False

    def close(self, animated):
        if self.mInTransition:
            raise RuntimeError("inTransition must be false. HINT: Use postClose.")

        self.evaluatePendingCondition()

        self.mInTransition = True

        try:
            if self.getDebugLevel() >= 2:
                print '  close'

            while True:
                if self.mCurrentState == OpenCloseStateMachine.OPEN:
                    if animated:
                        self.setCurrentState(OpenCloseStateMachine.ANIMATING_OPEN_TO_CLOSE)
                        self.parent_context.startAnimationOpenToClose()
                        # Enter group IN_TRANSITION
                        self.mGroupState[OpenCloseStateMachine.GROUP_IN_TRANSITION] = True
                        self.parent_context.setAnimating(True)
                    else:
                        # Leave group ANTENNA_VISIBLE
                        self.mGroupState[OpenCloseStateMachine.GROUP_ANTENNA_VISIBLE] = False
                        self.setCurrentState(OpenCloseStateMachine.CLOSED)
                        # Enter group ANTENNA_INVISIBLE
                        self.mGroupState[OpenCloseStateMachine.GROUP_ANTENNA_INVISIBLE] = True
                        self.parent_context.hideAntenna()
                    break

                # default
                break

        finally:
            self.mInTransition = False

    def toggle(self, animated):
        if self.mInTransition:
            raise RuntimeError("inTransition must be false. HINT: Use postToggle.")

        self.evaluatePendingCondition()

        self.mInTransition = True

        try:
            if self.getDebugLevel() >= 2:
                print '  toggle'

            while True:
                if self.mCurrentState == OpenCloseStateMachine.CLOSED:
                    if animated:
                        # Leave group ANTENNA_INVISIBLE
                        self.mGroupState[OpenCloseStateMachine.GROUP_ANTENNA_INVISIBLE] = False
                        self.setCurrentState(OpenCloseStateMachine.ANIMATING_CLOSE_TO_OPEN)
                        self.parent_context.startAnimationCloseToOpen()
                        # Enter group ANTENNA_VISIBLE
                        self.mGroupState[OpenCloseStateMachine.GROUP_ANTENNA_VISIBLE] = True
                        self.parent_context.showAntenna()
                        # Enter group IN_TRANSITION
                        self.mGroupState[OpenCloseStateMachine.GROUP_IN_TRANSITION] = True
                        self.parent_context.setAnimating(True)
                    else:
                        # Leave group ANTENNA_INVISIBLE
                        self.mGroupState[OpenCloseStateMachine.GROUP_ANTENNA_INVISIBLE] = False
                        self.setCurrentState(OpenCloseStateMachine.OPEN)
                        # Enter group ANTENNA_VISIBLE
                        self.mGroupState[OpenCloseStateMachine.GROUP_ANTENNA_VISIBLE] = True
                        self.parent_context.showAntenna()
                    break

                if self.mCurrentState == OpenCloseStateMachine.OPEN:
                    if animated:
                        self.setCurrentState(OpenCloseStateMachine.ANIMATING_OPEN_TO_CLOSE)
                        self.parent_context.startAnimationOpenToClose()
                        # Enter group IN_TRANSITION
                        self.mGroupState[OpenCloseStateMachine.GROUP_IN_TRANSITION] = True
                        self.parent_context.setAnimating(True)
                    else:
                        # Leave group ANTENNA_VISIBLE
                        self.mGroupState[OpenCloseStateMachine.GROUP_ANTENNA_VISIBLE] = False
                        self.setCurrentState(OpenCloseStateMachine.CLOSED)
                        # Enter group ANTENNA_INVISIBLE
                        self.mGroupState[OpenCloseStateMachine.GROUP_ANTENNA_INVISIBLE] = True
                        self.parent_context.hideAntenna()
                    break

                # default
                break

        finally:
            self.mInTransition = False

    def startToOpen(self):
        if self.mInTransition:
            raise RuntimeError("inTransition must be false. HINT: Use postStartToOpen.")

        self.evaluatePendingCondition()

        self.mInTransition = True

        try:
            if self.getDebugLevel() >= 2:
                print '  startToOpen'

            while True:
                if self.mCurrentState == OpenCloseStateMachine.ENTRY_POINT:
                    self.setCurrentState(OpenCloseStateMachine.OPEN)
                    # Enter group ANTENNA_VISIBLE
                    self.mGroupState[OpenCloseStateMachine.GROUP_ANTENNA_VISIBLE] = True
                    self.parent_context.showAntenna()
                    break

                # default
                break

        finally:
            self.mInTransition = False

    def startToClose(self):
        if self.mInTransition:
            raise RuntimeError("inTransition must be false. HINT: Use postStartToClose.")

        self.evaluatePendingCondition()

        self.mInTransition = True

        try:
            if self.getDebugLevel() >= 2:
                print '  startToClose'

            while True:
                if self.mCurrentState == OpenCloseStateMachine.ENTRY_POINT:
                    self.setCurrentState(OpenCloseStateMachine.CLOSED)
                    # Enter group ANTENNA_INVISIBLE
                    self.mGroupState[OpenCloseStateMachine.GROUP_ANTENNA_INVISIBLE] = True
                    self.parent_context.hideAntenna()
                    break

                # default
                break

        finally:
            self.mInTransition = False

    def notifyAnimationFinished(self):
        if self.mInTransition:
            raise RuntimeError("inTransition must be false. HINT: Use postNotifyAnimationFinished.")

        self.evaluatePendingCondition()

        self.mInTransition = True

        try:
            if self.getDebugLevel() >= 2:
                print '  notifyAnimationFinished'

            while True:
                if self.mCurrentState == OpenCloseStateMachine.ANIMATING_CLOSE_TO_OPEN:
                    # Leave group IN_TRANSITION
                    self.mGroupState[OpenCloseStateMachine.GROUP_IN_TRANSITION] = False
                    self.parent_context.setAnimating(False)
                    self.setCurrentState(OpenCloseStateMachine.OPEN)
                    break

                if self.mCurrentState == OpenCloseStateMachine.ANIMATING_OPEN_TO_CLOSE:
                    # Leave group ANTENNA_VISIBLE
                    self.mGroupState[OpenCloseStateMachine.GROUP_ANTENNA_VISIBLE] = False
                    # Leave group IN_TRANSITION
                    self.mGroupState[OpenCloseStateMachine.GROUP_IN_TRANSITION] = False
                    self.parent_context.setAnimating(False)
                    self.setCurrentState(OpenCloseStateMachine.CLOSED)
                    # Enter group ANTENNA_INVISIBLE
                    self.mGroupState[OpenCloseStateMachine.GROUP_ANTENNA_INVISIBLE] = True
                    self.parent_context.hideAntenna()
                    break

                # default
                break

        finally:
            self.mInTransition = False

    STATE_TABLE = ["ENTRY_POINT", "CLOSED", "OPEN", "ANIMATING_CLOSE_TO_OPEN", "ANIMATING_OPEN_TO_CLOSE"]
