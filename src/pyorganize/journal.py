#!/usr/bin/python
##############################################################################80
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


class Journal:
  """Journal Library
  """
  
  def __init__(self, date=datetime.date.today(), calendar=None, filename=None):
    """Creates a journal object.
    
    Args:
      date:
      calendar:
      filename:
    """
    self.date = date
    self.calendar = calendar
    self.filename = filename
  
  def GetCalendar(self, date=datetime.datetime.today(), user=None,
                  passwd=None):
    
    calendar_service = gdata.calendar.service.CalendarService()
    calendar_service.email = user
    calendar_service.password = passwd
    calendar_service.source = 'PyOrganize-0.1'
    calendar_service.ProgrammaticLogin()
    
    feed = calendar_service.GetCalendarListFeed()
    print feed.title.text
    for i, a_calendar in enumerate(feed.entry):
      print '\t%s. %s' % (i, a_calendar.title.text,)

    print 'Date range query for events on Primary Calendar: %s to %s' % (date, date,)
    query = gdata.calendar.service.CalendarEventQuery('default', 'private', 'full')
    query.start_min = date.__str__()
    query.start_max = date.__str__()
    feed = calendar_service.CalendarQuery(query)
    for i, an_event in enumerate(feed.entry):
      print '\t%s. %s' % (i, an_event.title.text,)
      for a_when in an_event.when:
        print '\t\tStart time: %s' % (a_when.start_time,)
        print '\t\tEnd time:   %s' % (a_when.end_time,)