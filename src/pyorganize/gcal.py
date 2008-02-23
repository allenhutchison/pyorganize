#!/usr/bin/python

__author__ = 'allen@hutchison.org (Allen Hutchison)'

try:
  from xml.etree import ElementTree # for Python 2.5 users
except ImportError:
  from elementtree import ElementTree
import gdata.calendar.service
import gdata.service
import atom.service
import gdata.calendar
import atom
import getopt
import sys
import string
import time
import datetime
import getpass
import logging

class GCal:
  """Calendar class to talk to Google Calendar
  """
  def __init__(self, user=None, passwd=None):
    cal_service = gdata.calendar.service.CalendarService()
    cal_service.email = user
    cal_service.password = passwd
    cal_service.source = 'PyOrganize-0.1'
    cal_service.ProgrammaticLogin()
    self.cal_service = cal_service

  def GetCalendars(self):
    self.cal_feed = self.cal_service.GetAllCalendarsFeed()
  
  def PrintCalendars(self):
    if not hasattr(self, 'cal_feed'):
      self.GetCalendars()
    print self.cal_feed.title.text
    for i, a_calendar in enumerate(self.cal_feed.entry):
      print '\t%s. %s' % (i, a_calendar.title.text,)
  
  def GetEventsOnDate(self, start_date=None, end_date=None):
    query = gdata.calendar.service.CalendarEventQuery('default',
                                                      'private',
                                                      'full')
    query.start_min = start_date
    query.start_max = end_date
    query.orderby = 'starttime'
    query.sortorder = 'ascending'
    query.singleevents = 'true'
    return(self.cal_service.CalendarQuery(query))
  
  def PrintEvents(self, start_date=None, end_date=None):
    event_feed = self.GetEventsOnDate(start_date=start_date, end_date=end_date)
    for i, an_event in enumerate(event_feed.entry):
      print '\t%s. %s' % (i, an_event.title.text,)
      for a_when in an_event.when:
        print '\t\tStart time: %s' % (a_when.start_time,)
        print '\t\tEnd time:   %s' % (a_when.end_time,)
  
if __name__ == '__main__':
  user = str(raw_input("Email Address: "))
  passwd = getpass.getpass()
  c = GCal(user=user, passwd=passwd)
  c.PrintEvents(start_date=str(datetime.date.today()), 
                end_date=str(datetime.date.today() + datetime.timedelta(days=1)))