#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import unittest
# from assets.stub_android import stub_api_model
from assets.stub_android import stub_android
import camera_controller


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


class TestDialogController(unittest.TestCase):
    def setUp(self):
        super(TestDialogController, self).setUp()
        self.pending_tasks = []
        self.timer_tasks = []
        self.stub_camera = stub_android.StubCamera()
        self.camera_factory = stub_android.CameraFactory(self.stub_camera)
        self.savedInstanceState = {}
        self.activityA = stub_android.StubActivity()
        self.activityA.delegate_instance = \
            camera_controller.CameraController(self.activityA,
                                               self.pending_tasks, self.timer_tasks, self.camera_factory)
        self.activityB = stub_android.StubActivity()
        self.activityB.delegate_instance = \
            camera_controller.CameraController(self.activityB,
                                               self.pending_tasks, self.timer_tasks, self.camera_factory)

    def tearDown(self):
        super(TestDialogController, self).tearDown()

    def _run_timer_tasks(self):
        timer_tasks = list(self.timer_tasks)
        self.timer_tasks[:] = []

        for task in timer_tasks:
            task()  # Maybe added into self.timer_tasks

    def setCameraUnavailable(self):
        self.stub_camera.camera_unavailable = True

    def setCameraAvailable(self):
        self.stub_camera.camera_unavailable = False

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

    @run_pending_tasks
    def onPauseB(self):
        self.activityB.onPause()

    @run_pending_tasks
    def takePictureA(self):
        self.activityA.delegate_instance.takePicture()

    @run_pending_tasks
    def surfaceCreatedA(self):
        self.activityA.delegate_instance.surfaceCreated()

    @run_pending_tasks
    def surfaceDestroyedA(self):
        self.activityA.delegate_instance.surfaceDestroyed()

    @run_pending_tasks
    def takePictureB(self):
        self.activityB.delegate_instance.takePicture()

    @run_pending_tasks
    def surfaceCreatedB(self):
        self.activityB.delegate_instance.surfaceCreated()

    @run_pending_tasks
    def surfaceDestroyedB(self):
        self.activityB.delegate_instance.surfaceDestroyed()

    def expectCameraReleased(self):
        self.assertTrue(self.stub_camera.is_released())

    # %%

    #
    # 以下の行は自動生成されているので直接編集しないでください。
    #
    # Generated by Test Case Generator
    # https://rubygems.org/gems/test_case_generator
    #

    @print_patterns(['onCreateA', 'onResumeA', 'takePictureA', 'onPauseA', 'expectCameraReleased', 'onSaveInstanceStateA', 'onCreateB', 'onResumeB', 'onPauseB', 'expectCameraReleased'])
    def test_onCreateA_onResumeA_takePictureA_onPauseA_expectCameraReleased_onSaveInstanceStateA_onCreateB_onResumeB_onPauseB_expectCameraReleased(self):
        self.onCreateA()
        self.onResumeA()
        self.takePictureA()
        self.onPauseA()
        self.expectCameraReleased()
        self.onSaveInstanceStateA()
        self.onCreateB()
        self.onResumeB()
        self.onPauseB()
        self.expectCameraReleased()

    @print_patterns(['onCreateA', 'onResumeA', 'surfaceCreatedA', 'takePictureA', 'onPauseA', 'expectCameraReleased', 'onSaveInstanceStateA', 'surfaceDestroyedA', 'onCreateB', 'onResumeB', 'onPauseB', 'expectCameraReleased'])
    def test_onCreateA_onResumeA_surfaceCreatedA_takePictureA_onPauseA_expectCameraReleased_onSaveInstanceStateA_surfaceDestroyedA_onCreateB_onResumeB_onPauseB_expectCameraReleased(self):
        self.onCreateA()
        self.onResumeA()
        self.surfaceCreatedA()
        self.takePictureA()
        self.onPauseA()
        self.expectCameraReleased()
        self.onSaveInstanceStateA()
        self.surfaceDestroyedA()
        self.onCreateB()
        self.onResumeB()
        self.onPauseB()
        self.expectCameraReleased()

    @print_patterns(['onCreateA', 'onResumeA', 'takePictureA', 'surfaceCreatedA', 'onPauseA', 'expectCameraReleased', 'onSaveInstanceStateA', 'surfaceDestroyedA', 'onCreateB', 'onResumeB', 'onPauseB', 'expectCameraReleased'])
    def test_onCreateA_onResumeA_takePictureA_surfaceCreatedA_onPauseA_expectCameraReleased_onSaveInstanceStateA_surfaceDestroyedA_onCreateB_onResumeB_onPauseB_expectCameraReleased(self):
        self.onCreateA()
        self.onResumeA()
        self.takePictureA()
        self.surfaceCreatedA()
        self.onPauseA()
        self.expectCameraReleased()
        self.onSaveInstanceStateA()
        self.surfaceDestroyedA()
        self.onCreateB()
        self.onResumeB()
        self.onPauseB()
        self.expectCameraReleased()

    @print_patterns(['setCameraUnavailable', 'onCreateA', 'onResumeA', 'surfaceCreatedA', 'takePictureA', 'onPauseA', 'expectCameraReleased', 'onSaveInstanceStateA', 'surfaceDestroyedA', 'setCameraAvailable', 'onCreateB', 'onResumeB', 'surfaceCreatedB', 'takePictureB', 'onPauseB', 'surfaceDestroyedB', 'expectCameraReleased'])
    def test_setCameraUnavailable_onCreateA_onResumeA_surfaceCreatedA_takePictureA_onPauseA_expectCameraReleased_onSaveInstanceStateA_surfaceDestroyedA_setCameraAvailable_onCreateB_onResumeB_surfaceCreatedB_takePictureB_onPauseB_surfaceDestroyedB_expectCameraReleased(self):
        self.setCameraUnavailable()
        self.onCreateA()
        self.onResumeA()
        self.surfaceCreatedA()
        self.takePictureA()
        self.onPauseA()
        self.expectCameraReleased()
        self.onSaveInstanceStateA()
        self.surfaceDestroyedA()
        self.setCameraAvailable()
        self.onCreateB()
        self.onResumeB()
        self.surfaceCreatedB()
        self.takePictureB()
        self.onPauseB()
        self.surfaceDestroyedB()
        self.expectCameraReleased()

    @print_patterns(['setCameraUnavailable', 'onCreateA', 'onResumeA', 'takePictureA', 'surfaceCreatedA', 'onPauseA', 'expectCameraReleased', 'onSaveInstanceStateA', 'surfaceDestroyedA', 'setCameraAvailable', 'onCreateB', 'onResumeB', 'surfaceCreatedB', 'takePictureB', 'onPauseB', 'surfaceDestroyedB', 'expectCameraReleased'])
    def test_setCameraUnavailable_onCreateA_onResumeA_takePictureA_surfaceCreatedA_onPauseA_expectCameraReleased_onSaveInstanceStateA_surfaceDestroyedA_setCameraAvailable_onCreateB_onResumeB_surfaceCreatedB_takePictureB_onPauseB_surfaceDestroyedB_expectCameraReleased(self):
        self.setCameraUnavailable()
        self.onCreateA()
        self.onResumeA()
        self.takePictureA()
        self.surfaceCreatedA()
        self.onPauseA()
        self.expectCameraReleased()
        self.onSaveInstanceStateA()
        self.surfaceDestroyedA()
        self.setCameraAvailable()
        self.onCreateB()
        self.onResumeB()
        self.surfaceCreatedB()
        self.takePictureB()
        self.onPauseB()
        self.surfaceDestroyedB()
        self.expectCameraReleased()

    @classmethod
    def checkSanity(cls):
        sane = True
        msg = []
        for method in ['onCreateA', 'onResumeA', 'takePictureA', 'onPauseA', 'expectCameraReleased', 'onSaveInstanceStateA', 'onCreateB', 'onResumeB', 'onPauseB', 'surfaceCreatedA', 'surfaceDestroyedA', 'setCameraUnavailable', 'setCameraAvailable', 'surfaceCreatedB', 'takePictureB', 'surfaceDestroyedB']:
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
    TestDialogController.checkSanity()
    unittest.main()
