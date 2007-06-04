#!/usr/bin/python
##############################################################################80
__author__ = 'allen@hutchison.org (Allen Hutchison)'

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
  
