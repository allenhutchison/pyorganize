#!/usr/bin/python
##############################################################################80
__author__ = 'allen@hutchison.org (Allen Hutchison)'

import datetime
import os
from pyorganize import config

class Todo:
  """Todo library
  """

  def __init__(self, title=None, description=None, tags=None, task_id=None,
               creation_date=datetime.date.today(), resolution_date=None,
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

    title = title.rstrip()
    title = title.lstrip()
    self.title = title

    if creation_date is None:
      self.creation_date = datetime.date.today()
    else:
      self.creation_date = creation_date

    self.due_date = due_date
    self.resolution_date = resolution_date
    self.tags = tags
    self.task_id = task_id
    self.description = description
    self.disk_sync = 0

    if filename is None:
      self.filename = os.path.join(config.PYORG_CONFIG.get('PyOrganize','base'),
                                   'tasks', ("%s.txt" % self.task_id))
    else:
      self.filename = filename

    self.Print()
    self.ReadTodo()
    self.Print()

  def __del__(self):
    self.WriteTodo()

  def Complete(self):
    self.resolution_date = datetime.datetime.today()

  def PrintSummary(self):
    print "%s: %s" % (self.task_id, self.title)

  def Print(self):
    print "task_id: %s" % self.task_id
    print "title: %s" % self.title
    print "creation_date: %s" % self.creation_date
    print "due_date: %s" % self.due_date
    print "resolution_date: %s" % self.resolution_date
    print "tags: %s" % self.tags
    print "description: %s" % self.description

  def WriteTodo(self):
    if self.disk_sync is 0:
      myfile = open(self.filename, 'w')
      myfile.write('creation_date: %s\n' % (self.creation_date))
      myfile.write('due_date: %s\n' % (self.due_date))
      myfile.write('resolution_date: %s\n' % (self.resolution_date))
      myfile.write('tags: %s\n' % (self.tags))
      myfile.write('description: %s\n' % (self.description))
      myfile.close()

  def ReadTodo(self):
    if os.path.exists(self.filename):
      myfile = open(self.filename)
      for line in myfile:
        (descriptor, data) = line.split(':', 1)
        if hasattr(self, descriptor):
          self.Set(descriptor, data)
        else:
          print "%s doesn't exist" % descriptor

  def Set(self, var, val):
    val = val.rstrip()
    val = val.lstrip()
    self.var = val

  def Edit(self):
    command = "%s %s" % (config.PYORG_CONFIG.get('PyOrganize', 'editor'),
                         self.filename)
    self.WriteTodo()
    os.system(command)
    self.ReadTodo()
    self.disk_sync = 1
