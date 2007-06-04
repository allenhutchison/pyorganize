#!/usr/bin/python
##############################################################################80
__author__ = 'allen@hutchison.org (Allen Hutchison)'

import datetime

class Todo:
  """Todo library
  """
  
  def __init__(self, title=None, description=None, tags=None, task_id=None,
               creation_date=datetime.datetime.today(), resolution_date=None, 
               due_date=None, filename=None):
    """Creates a todo object.
      
    Args:
      title: 
      description: 
      creation_date:
      due_date:
      tags:
      task_id:
      resolution_date:
      filename:
    """
    
    self.title = title
    self.description = description
    self.creation_date = creation_date
    self.due_date = due_date
    self.resolution_date = resolution_date
    self.tags = tags
    self.task_id = task_id
    self.filename = filename

  def Complete(self):
    self.resolution_date = datetime.datetime.today()
  
  
