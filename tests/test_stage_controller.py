#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import unittest
from assets.stub_android import stub_api_model
from assets.stub_android import stub_android
from stage_controller import print_task_status

import stage_controller


def print_patterns(patterns):
    def wrapper(fn):
        def _(self):
            print
            print "<<TEST>> %s" % (", ".join(patterns))
            fn(self)
        return _
    return wrapper


def run_pending_tasks(fn):
    def _(self):
        fn(self)

        while len(self.pending_tasks) > 0:
            # http://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list-in-python
            # Use instead of a weird syntax new_list = old_list[:]
            pending_tasks = list(self.pending_tasks)
            self.pending_tasks[:] = []

            for task in pending_tasks:
                task()  # Maybe added into self.pending_tasks

    return _


class TestStageController(unittest.TestCase):
    def setUp(self):
        super(TestStageController, self).setUp()
        self.instance_index = -1
        self.pending_tasks = []
        self.timer_tasks = []
        self.savedInstanceState = {}
        self.activityA = stub_android.StubActivity()
        self.activityA.delegate_instance = \
            stage_controller.StageController(self.activityA,
                                               self.pending_tasks, self.timer_tasks)
        self.activityB = stub_android.StubActivity()
        self.activityB.delegate_instance = \
            stage_controller.StageController(self.activityB,
                                               self.pending_tasks, self.timer_tasks)

    def tearDown(self):
        super(TestStageController, self).tearDown()

    @print_task_status("_run_timer_tasks")
    def _run_timer_tasks(self):
        timer_tasks = list(self.timer_tasks)
        self.timer_tasks[:] = []

        for task in timer_tasks:
            task()  # Maybe added into self.timer_tasks

    @run_pending_tasks
    def onCreateA(self):
        self.activityA.onCreate(None)

    @run_pending_tasks
    def onResumeA(self):
        self.activityA.onResume()

    @run_pending_tasks
    def onPauseA(self):
        self.activityA.onPause()

    @run_pending_tasks
    def onSaveInstanceStateA(self):
        self.activityA.onSaveInstanceState(self.savedInstanceState)

    @run_pending_tasks
    def onCreateB(self):
        self.activityB.onCreate(self.savedInstanceState)

    @run_pending_tasks
    def onResumeB(self):
        self.activityB.onResume()
        self._run_timer_tasks()

    @run_pending_tasks
    def notifyTimedOut(self):
        self._run_timer_tasks()

    @run_pending_tasks
    def onPauseB(self):
        self.activityB.onPause()

    @run_pending_tasks
    def clickA(self):
        self.activityA.delegate_instance.click()

    @run_pending_tasks
    def clickB(self):
        self.activityB.delegate_instance.click()

    @run_pending_tasks
    def notifyTimer1TimeoutA(self):
        self._run_timer_tasks()

    @run_pending_tasks
    def notifyTimer1TimeoutB(self):
        self._run_timer_tasks()

    @run_pending_tasks
    def closeDialogA(self):
        self.activityA.delegate_instance.closeDialog()

    @run_pending_tasks
    def closeDialogB(self):
        self.activityB.delegate_instance.closeDialog()

    def expectInGameOverState(self):
        self.assertEqual('GAME_OVER', self.activityB.delegate_instance.state_machine.getCurrentStateName())

    # %%

    #
    # 以下の行は自動生成されているので直接編集しないでください。
    #
    # Generated by Test Case Generator
    # https://rubygems.org/gems/test_case_generator
    #

    @print_patterns(['onCreateA', 'onResumeA', 'clickA', 'onPauseA', 'onSaveInstanceStateA', 'onCreateB', 'onResumeB', 'clickB', 'closeDialogB', 'onPauseB', 'expectInGameOverState'])
    def test_onCreateA_onResumeA_clickA_onPauseA_onSaveInstanceStateA_onCreateB_onResumeB_clickB_closeDialogB_onPauseB_expectInGameOverState(self):
        self.onCreateA()
        self.onResumeA()
        self.clickA()
        self.onPauseA()
        self.onSaveInstanceStateA()
        self.onCreateB()
        self.onResumeB()
        self.clickB()
        self.closeDialogB()
        self.onPauseB()
        self.expectInGameOverState()

    @print_patterns(['onCreateA', 'onResumeA', 'clickA', 'notifyTimer1TimeoutA', 'onPauseA', 'onSaveInstanceStateA', 'onCreateB', 'onResumeB', 'notifyTimer1TimeoutB', 'notifyTimer1TimeoutB', 'closeDialogB', 'onPauseB', 'expectInGameOverState'])
    def test_onCreateA_onResumeA_clickA_notifyTimer1TimeoutA_onPauseA_onSaveInstanceStateA_onCreateB_onResumeB_notifyTimer1TimeoutB_notifyTimer1TimeoutB_closeDialogB_onPauseB_expectInGameOverState(self):
        self.onCreateA()
        self.onResumeA()
        self.clickA()
        self.notifyTimer1TimeoutA()
        self.onPauseA()
        self.onSaveInstanceStateA()
        self.onCreateB()
        self.onResumeB()
        self.notifyTimer1TimeoutB()
        self.notifyTimer1TimeoutB()
        self.closeDialogB()
        self.onPauseB()
        self.expectInGameOverState()

    @print_patterns(['onCreateA', 'onResumeA', 'notifyTimer1TimeoutA', 'notifyTimer1TimeoutA', 'notifyTimer1TimeoutA', 'clickA', 'notifyTimer1TimeoutA', 'onPauseA', 'onSaveInstanceStateA', 'onCreateB', 'onResumeB', 'notifyTimer1TimeoutB', 'notifyTimer1TimeoutB', 'closeDialogB', 'onPauseB', 'expectInGameOverState'])
    def test_onCreateA_onResumeA_notifyTimer1TimeoutA_notifyTimer1TimeoutA_notifyTimer1TimeoutA_clickA_notifyTimer1TimeoutA_onPauseA_onSaveInstanceStateA_onCreateB_onResumeB_notifyTimer1TimeoutB_notifyTimer1TimeoutB_closeDialogB_onPauseB_expectInGameOverState(self):
        self.onCreateA()
        self.onResumeA()
        self.notifyTimer1TimeoutA()
        self.notifyTimer1TimeoutA()
        self.notifyTimer1TimeoutA()
        self.clickA()
        self.notifyTimer1TimeoutA()
        self.onPauseA()
        self.onSaveInstanceStateA()
        self.onCreateB()
        self.onResumeB()
        self.notifyTimer1TimeoutB()
        self.notifyTimer1TimeoutB()
        self.closeDialogB()
        self.onPauseB()
        self.expectInGameOverState()

    @classmethod
    def checkSanity(cls):
        sane = True
        msg = []
        for method in ['onCreateA', 'onResumeA', 'clickA', 'onPauseA', 'onSaveInstanceStateA', 'onCreateB', 'onResumeB', 'clickB', 'closeDialogB', 'onPauseB', 'expectInGameOverState', 'notifyTimer1TimeoutA', 'notifyTimer1TimeoutB']:
            if not hasattr(cls, method):
                msg += [
                    '    def %s(self):' % method,
                    '        pass',
                    '',
                ]
                sane = False

        if not sane:
            print cls.__name__ + ' must implement following method(s):'
            print
            print "\n".join(msg)
            raise SystemExit(1)


if __name__ == '__main__':
    TestStageController.checkSanity()
    unittest.main()
