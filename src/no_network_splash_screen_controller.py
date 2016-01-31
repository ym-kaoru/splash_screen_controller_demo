# -*- coding: utf-8 -*-
import os
import sys

TAG = "Controller"


class NoNetworkSplashScreenController(object):

    def __init__(self, activity, pending_tasks, timer_tasks):
        super(NoNetworkSplashScreenController, self).__init__()
        self.activity = activity
        self.pending_tasks = pending_tasks
        self.timer_tasks = timer_tasks
        self.state_machine = NoNetworkSplashScreenControllerStateMachine(self)

    def onCreate(self, saved_instance_state):
        self.prepareStateMachine(True, saved_instance_state)
        self.state_machine.onCreate(saved_instance_state)

    def onStart(self):
        pass

    def onResume(self):
        self.state_machine.onResume()

    def onPause(self):
        self.state_machine.onPause()

    def isResumed(self):
        return self.activity.isResumed()

    def onSaveInstanceState(self, out_instance_state):
        self.saveStateMachine(out_instance_state)

    def onStop(self):
        pass

    def onDestroy(self):
        pass

    def showSplashScreen(self):
        self.activity.add_fragment("SplashScreen")

    def hideSplashScreen(self):
        self.activity.pop_back()

    def onReady(self):
        # TODO: Relay onReady event to parent context.
        pass

    def post(self, action):
        self.pending_tasks.append(action)
        return action

    def postDelayed(self, action, delayMillis):
        self.timer_tasks.append(action)
        return action

    def removeCallbacks(self, task_id):
        self.pending_tasks[:] = [action for action in self.pending_tasks if action != task_id]
        self.timer_tasks[:] = [action for action in self.timer_tasks if action != task_id]

    def checkThread(self):
        pass

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


class NoNetworkSplashScreenControllerStateMachine(object):

    class_instance_counter = 0

    ENTRY_POINT = 0
    SPLASH_SCREEN = 1
    READY = 2

    def __init__(self, parent_context):
        super(NoNetworkSplashScreenControllerStateMachine, self).__init__()
        self.instance_index = NoNetworkSplashScreenControllerStateMachine.class_instance_counter
        NoNetworkSplashScreenControllerStateMachine.class_instance_counter += 1
        self.parent_context = parent_context
        self.mDebugFlag = False
        self.mInTransition = False
        self.mCurrentState = 0
        self.mGroupState = []
        self.mPendingState = 0
        self.mPendingEvent = None
        self.mPendingPriority = 0
        self.mDebugLevel = 2

    def getCurrentState(self):
        return self.mCurrentState

    def getCurrentStateName(self):
        return NoNetworkSplashScreenControllerStateMachine.STATE_TABLE[self.mCurrentState]

    def setCurrentState(self, state):
        self.mCurrentState = state
        self.clearPendingState()
        self.debugPrintCurrentState('ENTER STATE')

    def debugPrintCurrentState(self, msg):
        state = self.mCurrentState
        if self.mDebugFlag and state < len(NoNetworkSplashScreenControllerStateMachine.STATE_TABLE):
            print "NoNetworkSplashScreenControllerStateMachine(%d): %s: %s" % (self.instance_index, msg, NoNetworkSplashScreenControllerStateMachine.STATE_TABLE[state])

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

        # notify_timer1_timeout
        if self.mPendingState == 5:
            if not self.parent_context.isResumed():
                return

            pending_event = self.mPendingEvent
            self.clearPendingState()
            pending_event()

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
            if self.mCurrentState == NoNetworkSplashScreenControllerStateMachine.SPLASH_SCREEN:
                self.startTimer1()
            break

    def onCreate(self, saved_instance_state):
        if self.mInTransition:
            raise RuntimeError("inTransition must be false. HINT: Use postOnCreate.")

        self.evaluatePendingCondition()

        self.mInTransition = True

        try:
            if self.getDebugLevel() >= 2:
                print '  onCreate'

            while True:
                if self.mCurrentState == NoNetworkSplashScreenControllerStateMachine.ENTRY_POINT:
                    self.setCurrentState(NoNetworkSplashScreenControllerStateMachine.SPLASH_SCREEN)
                    self.parent_context.showSplashScreen()
                    self.startTimer1()
                    break

                # default
                break

        finally:
            self.mInTransition = False

    def onResume(self):
        if self.mInTransition:
            raise RuntimeError("inTransition must be false. HINT: Use postOnResume.")

        self.evaluatePendingCondition()

        self.mInTransition = True

        try:
            if self.getDebugLevel() >= 2:
                print '  onResume'

            while True:
                # default
                break

        finally:
            self.mInTransition = False

    def onPause(self):
        if self.mInTransition:
            raise RuntimeError("inTransition must be false. HINT: Use postOnPause.")

        self.evaluatePendingCondition()

        self.mInTransition = True

        try:
            if self.getDebugLevel() >= 2:
                print '  onPause'

            while True:
                # default
                break

        finally:
            self.mInTransition = False

    def notifyTimer1Timeout(self):
        if not self.parent_context.isResumed():
            raise RuntimeError('Violation of the pending condition')

        if self.mInTransition:
            raise RuntimeError("inTransition must be false. HINT: Use postNotifyTimer1Timeout.")

        self.evaluatePendingCondition()

        self.mInTransition = True

        try:
            if self.getDebugLevel() >= 2:
                print '  notify_timer1_timeout'

            while True:
                if self.mCurrentState == NoNetworkSplashScreenControllerStateMachine.SPLASH_SCREEN:
                    self.cancelTimer1()
                    self.parent_context.hideSplashScreen()
                    self.setCurrentState(NoNetworkSplashScreenControllerStateMachine.READY)
                    self.parent_context.onReady()
                    break

                # default
                break

        finally:
            self.mInTransition = False

    def timer1Runner(self):
        def _():
            self.notifyTimer1Timeout()

        if not self.parent_context.isResumed():
            if self.mPendingPriority <= 0:
                self.mPendingEvent = _
                self.mPendingState = 5
                self.mPendingPriority = 0
        else:
            _()

    def startTimer1(self):
        self.parent_context.postDelayed(self.timer1Runner, 1000)

    def cancelTimer1(self):
        self.parent_context.removeCallbacks(self.timer1Runner)

    STATE_TABLE = ["ENTRY_POINT", "SPLASH_SCREEN", "READY"]
