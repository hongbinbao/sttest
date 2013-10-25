#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest, sys, ConfigParser
#import device
from uiautomator import device
from os.path import dirname, abspath, join, exists, splitext, split 
import copy, sys, os, datetime, string, argparse, collections, time, sys

import imgcomparision 
#import isMatch, getMatchedCenterOffset

def _getTestSuiteFromFile(self,plan_file_path):
    '''
    Return a test object list from the given plan file. we called it TestSuites. Python unittest 
    A unittest.TestCase instance only contain the target method to be run.
    @rtype: []
    @return: list of instances of unittest.TestCase specified by plan file
    '''
    section_name = 'tests'
    tests = []
    names = []
    loader = unittest.TestLoader()
    parser = ConfigParser.ConfigParser(dict_type=OrderedDict)
    parser.optionxform = lambda x: x
    parser.read(plan_file_path)
    tests = parser.items(section_name)
    for (k,v) in tests:
        for i in range(int(v)):
            names.append(k)
    suite = loader.loadTestsFromNames(names) 
    return suite

TIME_STAMP_FORMAT = '%Y-%m-%d_%H:%M:%S'
_WORKSPACE = dirname(abspath(__file__))
_SCRIPT_WORKSPACE = join(dirname(_WORKSPACE), 'scripts')

def environment(*dpendcy):
    '''
    a wrapper to force checking test environment.
    '''
    def check_environment(func):
        for d in dpendcy: assert getoutput('%s %s' %('which', d)), '%s not found!' % d
        def wrapper(*argv, **argvs):
            func(*argv, **argvs)
        return wrapper
    return check_environment


class MessageTest(unittest.TestCase):
    def setUp(self):
        super(MessageTest, self).setUp()
        device.screen.on()
        device.watcher("AUTO_FC").when(text="OK").click(text="OK")
        #print self.device
        #print device.watchers
        #print dir(self)
        #print 'directory', self.__module__

    def tearDown(self):
        device.press.back()

    def doCleanups(self):
        pass

    def testSendMessage1(self):
        i = 0
        while 1:
            import time
            device.screen.on()
            time.sleep(3)
            device.screen.off()
            import sys
            sys.stderr.write('case is running %s \n' % str(i))
            sys.stderr.flush()
            i = i + 1
        #if device.exists(text="BugTrigger"):
        #    device(text="BugTrigger").click()
        #    time.sleep(3)
        #self.assertTrue(device.exists(text="ForceClose"))
        #src_name = 'launch_ok.png'
        #src_path = join(join(_WORKSPACE, self._testMethodName), src_name)
        #device.screenshot(src_path)
        #unused
        #imgcomparision.isMatch()
        #screenshot = 
        #expect(text='')
        #expect(pic='')


    @unittest.skipIf(sys.platform.startswith("win"), "not supported")
    def testSendMessage2(self):
        if device.exists(text="BugTrigger"):
            device(text="BugTrigger").click()
            time.sleep(3)
        self.assertTrue(device.exists(text="ForceClose"))


