#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d

class MessageTest(unittest.TestCase):
    def setUp(self):
        super(MessageTest, self).setUp()
        #d.start_activity(action='android.intent.action.DIAL', data='tel:13581739891', flags=0x04000000)
        d.press('back')\
         .press('back')\
         .press('home')

    def tearDown(self):
        d.press('back')\
         .press('back')\
         .press('back')\
         .press('home')

    def testSendMessage1(self):
        #sys.stderr.write(str(d(text="Settings").click()))
        d.wakeup()
        #d.click(100, 200, waittime=2)
        #d.start_activity(action='android.intent.action.DIAL', data='tel:13581739891', flags=0x04000000)
        d.click('a.png', waittime=1, threshold=0.01)\
         .expect('no_msg.png')\
         .click('create_btn.png')

        if d.find('input_label.png'):
            d.click('input_label.png')\
             .click('content_label.png')
        d.expect('send_btn.png')
        #assert d.exists(text='New message')
            
    def testSendMessage2(self):
        assert d.exists(text='Messaging')
        d(text='Messaging').click()
        assert d.exists(text='No conversations')
        d.click('create_btn.png')

        if d.find('input_label.png'):
            d.click('input_label.png')\
             .click('content_label.png')

        assert d.exists(text='New message')


