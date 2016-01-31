#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import copy


class IllegalStateException(RuntimeError):
    pass


class StubDialog(object):
    def __init__(self, activity, tag):
        super(StubDialog, self).__init__()
        self.activity = activity
        self.tag = tag

    def dismiss(self):
        if self.activity.onSaveInstanceState_called:
            raise IllegalStateException()

        self.activity.dialog_shown = False
        name = self.activity.back_stack.pop()
        if name != self.tag:
            raise IllegalStateException()
        self.activity.remove_fragment(self.tag)


# class StubFragment(object):
#     def __init__(self, activity):
#         super(StubFragment, self).__init__()
#         self.activity = activity


class StubActivity(object):
    def __init__(self):
        super(StubActivity, self).__init__()
        self.delegate_instance = None
        self.dialog_shown = False
        self.onSaveInstanceState_called = False
        self.fragments = {}
        self.current_fragment = None
        self.back_stack = []
        self.resumed = False

    def show_dialog(self, tag):
        if self.dialog_shown:
            raise IllegalStateException("Already a dialog has been open.")

        if self.onSaveInstanceState_called:
            raise IllegalStateException("Must not show_dialog after onSaveInstanceState is called.")

        dialog = StubDialog(self, tag)
        self.dialog_shown = True
        self.fragments[tag] = "_dialog"
        self.back_stack.append(tag)
        return dialog

    def add_fragment(self, name):
        if self.onSaveInstanceState_called:
            raise IllegalStateException("Must not add_fragment after onSaveInstanceState is called.")

        if name in self.fragments:
            raise IllegalStateException("The fragment '%s' has been already added." % name)

        self.fragments[name] = name
        self.back_stack.append(name)

    def pop_back(self):
        name = self.back_stack.pop()
        self.remove_fragment(name)

    def replace_fragment(self, name):
        if self.onSaveInstanceState_called:
            raise IllegalStateException("Must not replace_fragment after onSaveInstanceState is called.")

        if self.current_fragment:
            del self.fragments[self.current_fragment]

        self.fragments[name] = name
        self.current_fragment = name

    def find_fragment_by_tag(self, name):
        fragment = self.fragments[name]
        if fragment == "_dialog":
            return StubDialog(self, name)
        else:
            return fragment

    def is_fragment_shown(self, name):
        return name in self.fragments

    def remove_fragment(self, name):
        if self.onSaveInstanceState_called:
            raise IllegalStateException("Must not remove_fragment after onSaveInstanceState is called.")

        del self.fragments[name]

    def onCreate(self, saved_instance_state):
        if saved_instance_state is not None:
            if "_dialog_shown" in saved_instance_state:
                self.dialog_shown = saved_instance_state["_dialog_shown"]
            if "_fragments" in saved_instance_state:
                self.fragments = copy.deepcopy(saved_instance_state["_fragments"])
            if "_backstack" in saved_instance_state:
                self.back_stack = copy.deepcopy(saved_instance_state["_backstack"])

        self.onSaveInstanceState_called = False
        self.delegate_instance.onCreate(saved_instance_state)

    def onStart(self):
        self.onSaveInstanceState_called = False
        self.delegate_instance.onStart()

    def onResume(self):
        self.resumed = True
        self.delegate_instance.onResume()

    def onPause(self):
        self.resumed = False
        self.delegate_instance.onPause()

    def isResumed(self):
        return self.resumed

    def onSaveInstanceState(self, out_instance_state):
        self.delegate_instance.onSaveInstanceState(out_instance_state)
        if self.dialog_shown:
            out_instance_state["_dialog_shown"] = True
        out_instance_state["_fragments"] = copy.deepcopy(self.fragments)
        out_instance_state["_backstack"] = copy.deepcopy(self.back_stack)
        self.onSaveInstanceState_called = True

    def onStop(self):
        self.onSaveInstanceState_called = True
        self.delegate_instance.onStop()

    def onDestroy(self):
        self.onSaveInstanceState_called = True
        self.delegate_instance.onStop()


class StubCamera(object):
    def __init__(self, camera_unavailable=False):
        super(StubCamera, self).__init__()
        self.camera_unavailable = camera_unavailable
        self.counter = 0
        self.surface_holder = None
        self.previewing = False

    def open(self):
        if self.camera_unavailable:
            raise CameraException()

        self.counter += 1
        if self.counter >= 2:
            raise IllegalStateException("counter = %d" % self.counter)
        return self

    def release(self):
        self.counter -= 1
        if self.counter < 0:
            raise IllegalStateException("counter = %d" % self.counter)
        return self

    def setPreviewDisplay(self, surface_holder):
        if self.is_released():
            raise IllegalStateException("Camera is not open")
        self.surface_holder = surface_holder

    def startPreview(self):
        if self.is_released():
            raise IllegalStateException("Camera is not open")
        self.previewing = True

    def stopPreview(self):
        if self.is_released():
            raise IllegalStateException("Camera is not open")
        self.previewing = False

    def takePicture(self):
        if self.is_released():
            raise IllegalStateException("Camera is not open")
        if self.surface_holder is None:
            raise IllegalStateException("No surface")
        if not self.is_previewing():
            raise IllegalStateException("Does not start preview")

    def is_released(self):
        return self.counter == 0

    def is_previewing(self):
        return self.previewing


class CameraFactory(object):

    def __init__(self, stub_camera):
        super(CameraFactory, self).__init__()
        self.stub_camera = stub_camera

    def open(self):
        return self.stub_camera.open()


class CameraException(RuntimeError):
    pass
