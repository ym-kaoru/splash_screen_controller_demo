#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import unittest


class CreateStartResumePauseStopDestroy(unittest.TestCase):
    def setUp(self):
        super(CreateStartResumePauseStopDestroy, self).setUp()

    def tearDown(self):
        super(CreateStartResumePauseStopDestroy, self).tearDown()

# %%

    #
    # 以下の行は自動生成されているので直接編集しないでください。
    #
    # Generated by Test Case Generator
    # https://rubygems.org/gems/test_case_generator
    #

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onStopA_onDestroyA_onCreateB_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onStopA()
        self.onDestroyA()
        self.onCreateB()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onStopA_onCreateB_onDestroyA_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onStopA()
        self.onCreateB()
        self.onDestroyA()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onStopA_onCreateB_onDestroyB_onDestroyA(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onStopA()
        self.onCreateB()
        self.onDestroyB()
        self.onDestroyA()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStopA_onDestroyA_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStopA()
        self.onDestroyA()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStopA_onDestroyB_onDestroyA(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStopA()
        self.onDestroyB()
        self.onDestroyA()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onDestroyB_onStopA_onDestroyA(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onDestroyB()
        self.onStopA()
        self.onDestroyA()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onStopA_onDestroyA_onCreateB_onStartB_onStopB_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onStopA()
        self.onDestroyA()
        self.onCreateB()
        self.onStartB()
        self.onStopB()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onStopA_onCreateB_onDestroyA_onStartB_onStopB_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onStopA()
        self.onCreateB()
        self.onDestroyA()
        self.onStartB()
        self.onStopB()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onStopA_onCreateB_onStartB_onDestroyA_onStopB_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onStopA()
        self.onCreateB()
        self.onStartB()
        self.onDestroyA()
        self.onStopB()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onStopA_onCreateB_onStartB_onStopB_onDestroyA_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onStopA()
        self.onCreateB()
        self.onStartB()
        self.onStopB()
        self.onDestroyA()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onStopA_onCreateB_onStartB_onStopB_onDestroyB_onDestroyA(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onStopA()
        self.onCreateB()
        self.onStartB()
        self.onStopB()
        self.onDestroyB()
        self.onDestroyA()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStopA_onDestroyA_onStartB_onStopB_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStopA()
        self.onDestroyA()
        self.onStartB()
        self.onStopB()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStopA_onStartB_onDestroyA_onStopB_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStopA()
        self.onStartB()
        self.onDestroyA()
        self.onStopB()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStopA_onStartB_onStopB_onDestroyA_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStopA()
        self.onStartB()
        self.onStopB()
        self.onDestroyA()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStopA_onStartB_onStopB_onDestroyB_onDestroyA(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStopA()
        self.onStartB()
        self.onStopB()
        self.onDestroyB()
        self.onDestroyA()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStartB_onStopA_onDestroyA_onStopB_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStartB()
        self.onStopA()
        self.onDestroyA()
        self.onStopB()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStartB_onStopA_onStopB_onDestroyA_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStartB()
        self.onStopA()
        self.onStopB()
        self.onDestroyA()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStartB_onStopA_onStopB_onDestroyB_onDestroyA(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStartB()
        self.onStopA()
        self.onStopB()
        self.onDestroyB()
        self.onDestroyA()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStartB_onStopB_onStopA_onDestroyA_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStartB()
        self.onStopB()
        self.onStopA()
        self.onDestroyA()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStartB_onStopB_onStopA_onDestroyB_onDestroyA(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStartB()
        self.onStopB()
        self.onStopA()
        self.onDestroyB()
        self.onDestroyA()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStartB_onStopB_onDestroyB_onStopA_onDestroyA(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStartB()
        self.onStopB()
        self.onDestroyB()
        self.onStopA()
        self.onDestroyA()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onStopA_onDestroyA_onCreateB_onStartB_onResumeB_onPauseB_onStopB_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onStopA()
        self.onDestroyA()
        self.onCreateB()
        self.onStartB()
        self.onResumeB()
        self.onPauseB()
        self.onStopB()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onStopA_onCreateB_onDestroyA_onStartB_onResumeB_onPauseB_onStopB_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onStopA()
        self.onCreateB()
        self.onDestroyA()
        self.onStartB()
        self.onResumeB()
        self.onPauseB()
        self.onStopB()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onStopA_onCreateB_onStartB_onDestroyA_onResumeB_onPauseB_onStopB_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onStopA()
        self.onCreateB()
        self.onStartB()
        self.onDestroyA()
        self.onResumeB()
        self.onPauseB()
        self.onStopB()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onStopA_onCreateB_onStartB_onResumeB_onDestroyA_onPauseB_onStopB_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onStopA()
        self.onCreateB()
        self.onStartB()
        self.onResumeB()
        self.onDestroyA()
        self.onPauseB()
        self.onStopB()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onStopA_onCreateB_onStartB_onResumeB_onPauseB_onDestroyA_onStopB_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onStopA()
        self.onCreateB()
        self.onStartB()
        self.onResumeB()
        self.onPauseB()
        self.onDestroyA()
        self.onStopB()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onStopA_onCreateB_onStartB_onResumeB_onPauseB_onStopB_onDestroyA_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onStopA()
        self.onCreateB()
        self.onStartB()
        self.onResumeB()
        self.onPauseB()
        self.onStopB()
        self.onDestroyA()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onStopA_onCreateB_onStartB_onResumeB_onPauseB_onStopB_onDestroyB_onDestroyA(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onStopA()
        self.onCreateB()
        self.onStartB()
        self.onResumeB()
        self.onPauseB()
        self.onStopB()
        self.onDestroyB()
        self.onDestroyA()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStopA_onDestroyA_onStartB_onResumeB_onPauseB_onStopB_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStopA()
        self.onDestroyA()
        self.onStartB()
        self.onResumeB()
        self.onPauseB()
        self.onStopB()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStopA_onStartB_onDestroyA_onResumeB_onPauseB_onStopB_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStopA()
        self.onStartB()
        self.onDestroyA()
        self.onResumeB()
        self.onPauseB()
        self.onStopB()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStopA_onStartB_onResumeB_onDestroyA_onPauseB_onStopB_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStopA()
        self.onStartB()
        self.onResumeB()
        self.onDestroyA()
        self.onPauseB()
        self.onStopB()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStopA_onStartB_onResumeB_onPauseB_onDestroyA_onStopB_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStopA()
        self.onStartB()
        self.onResumeB()
        self.onPauseB()
        self.onDestroyA()
        self.onStopB()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStopA_onStartB_onResumeB_onPauseB_onStopB_onDestroyA_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStopA()
        self.onStartB()
        self.onResumeB()
        self.onPauseB()
        self.onStopB()
        self.onDestroyA()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStopA_onStartB_onResumeB_onPauseB_onStopB_onDestroyB_onDestroyA(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStopA()
        self.onStartB()
        self.onResumeB()
        self.onPauseB()
        self.onStopB()
        self.onDestroyB()
        self.onDestroyA()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStartB_onStopA_onDestroyA_onResumeB_onPauseB_onStopB_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStartB()
        self.onStopA()
        self.onDestroyA()
        self.onResumeB()
        self.onPauseB()
        self.onStopB()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStartB_onStopA_onResumeB_onDestroyA_onPauseB_onStopB_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStartB()
        self.onStopA()
        self.onResumeB()
        self.onDestroyA()
        self.onPauseB()
        self.onStopB()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStartB_onStopA_onResumeB_onPauseB_onDestroyA_onStopB_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStartB()
        self.onStopA()
        self.onResumeB()
        self.onPauseB()
        self.onDestroyA()
        self.onStopB()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStartB_onStopA_onResumeB_onPauseB_onStopB_onDestroyA_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStartB()
        self.onStopA()
        self.onResumeB()
        self.onPauseB()
        self.onStopB()
        self.onDestroyA()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStartB_onStopA_onResumeB_onPauseB_onStopB_onDestroyB_onDestroyA(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStartB()
        self.onStopA()
        self.onResumeB()
        self.onPauseB()
        self.onStopB()
        self.onDestroyB()
        self.onDestroyA()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStartB_onResumeB_onStopA_onDestroyA_onPauseB_onStopB_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStartB()
        self.onResumeB()
        self.onStopA()
        self.onDestroyA()
        self.onPauseB()
        self.onStopB()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStartB_onResumeB_onStopA_onPauseB_onDestroyA_onStopB_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStartB()
        self.onResumeB()
        self.onStopA()
        self.onPauseB()
        self.onDestroyA()
        self.onStopB()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStartB_onResumeB_onStopA_onPauseB_onStopB_onDestroyA_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStartB()
        self.onResumeB()
        self.onStopA()
        self.onPauseB()
        self.onStopB()
        self.onDestroyA()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStartB_onResumeB_onStopA_onPauseB_onStopB_onDestroyB_onDestroyA(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStartB()
        self.onResumeB()
        self.onStopA()
        self.onPauseB()
        self.onStopB()
        self.onDestroyB()
        self.onDestroyA()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStartB_onResumeB_onPauseB_onStopA_onDestroyA_onStopB_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStartB()
        self.onResumeB()
        self.onPauseB()
        self.onStopA()
        self.onDestroyA()
        self.onStopB()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStartB_onResumeB_onPauseB_onStopA_onStopB_onDestroyA_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStartB()
        self.onResumeB()
        self.onPauseB()
        self.onStopA()
        self.onStopB()
        self.onDestroyA()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStartB_onResumeB_onPauseB_onStopA_onStopB_onDestroyB_onDestroyA(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStartB()
        self.onResumeB()
        self.onPauseB()
        self.onStopA()
        self.onStopB()
        self.onDestroyB()
        self.onDestroyA()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStartB_onResumeB_onPauseB_onStopB_onStopA_onDestroyA_onDestroyB(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStartB()
        self.onResumeB()
        self.onPauseB()
        self.onStopB()
        self.onStopA()
        self.onDestroyA()
        self.onDestroyB()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStartB_onResumeB_onPauseB_onStopB_onStopA_onDestroyB_onDestroyA(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStartB()
        self.onResumeB()
        self.onPauseB()
        self.onStopB()
        self.onStopA()
        self.onDestroyB()
        self.onDestroyA()

    def test_onCreateA_onStartA_onResumeA_onPauseA_onSaveInstanceState_onCreateB_onStartB_onResumeB_onPauseB_onStopB_onDestroyB_onStopA_onDestroyA(self):
        self.onCreateA()
        self.onStartA()
        self.onResumeA()
        self.onPauseA()
        self.onSaveInstanceState()
        self.onCreateB()
        self.onStartB()
        self.onResumeB()
        self.onPauseB()
        self.onStopB()
        self.onDestroyB()
        self.onStopA()
        self.onDestroyA()

    @classmethod
    def checkSanity(cls):
        sane = True
        msg = []
        for method in ['onStopA', 'onDestroyA', 'onCreateB', 'onDestroyB', 'onStartB', 'onStopB', 'onResumeB', 'onPauseB']:
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
    CreateStartResumePauseStopDestroy.checkSanity()
    unittest.main()
