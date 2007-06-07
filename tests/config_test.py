#!/usr/bin/python

__author__ = 'allen@hutchison.org (Allen Hutchison)'

import unittest
from pyorganize import config

class ConfigTest(unittest.TestCase):
  def setUp(self):
    self.config = config.Config(file='config_test_data.ini')

  def testReadGoogleCalendarUsername(self):
    self.assert_(self.config.get('GoogleCalendar', 'username') == 'foo@foo.com')

  def testReadPyorganizeBase(self):
    self.assert_(self.config.get('Pyorganize', 'base') == '/home/foo/organize')

  def testWriteNewVarToExistingSection(self):
    self.config.set('Pyorganize', 'test', 'bar')
    self.assert_(self.config.get('Pyorganize', 'test') == 'bar')

  def testWriteNewVarToNewSection(self):
    self.config.add_section('test')
    self.config.set('test', 'var', 'foo')
    self.assert_(self.config.get('test', 'var') == 'foo')

  def testOverwriteExistingVar(self):
    self.config.add_section('test')
    self.config.set('test', 'var', 'bar')
    self.assert_(self.config.get('test', 'var') == 'bar')


if __name__ == '__main__':
  unittest.main()
