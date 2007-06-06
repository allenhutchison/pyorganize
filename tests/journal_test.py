#!/usr/bin/python

__author__ = 'allen@hutchison.org (Allen Hutchison)'

import datetime
import unittest
from pyorganize import journal

class JournalTest(unittest.TestCase):
  
  def setUp(self):
    self.journal = journal.Journal()

  def testEmptyCalendar(self):
    self.assert_(self.journal.calendar is None)
  
  def testEmptyFilename(self):
    self.assert_(self.journal.filename is None)
    
  def testDefaultDate(self):
    today = datetime.date.today()
    self.assert_(self.journal.date == today)
  
  def testGetCalendarForToday(self):
    today = datetime.date.today()
    self.journal.GetCalendar(date=today)
  

if __name__ == '__main__':
  unittest.main()
