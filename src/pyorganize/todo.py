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

    title = title.rstrip()
    title = title.lstrip()
    self.title = title

    if creation_date is None:
      self.creation_date = datetime.datetime.today()
    else:
      self.creation_date = creation_date

    self.due_date = due_date
    self.resolution_date = resolution_date
    self.tags = tags
    self.task_id = task_id
    self.description = description

    if filename is None:
      self.filename = os.path.join(config.PYORG_CONFIG.get('PyOrganize','base'),
                                   'tasks', ("%s.txt" % self.task_id))
    else:
      self.filename = filename

  def Complete(self):
    self.resolution_date = datetime.datetime.today()
    self.WriteTodo()

  def PrintSummary(self):
    print "%s: %s" % (self.task_id, self.title)

  def WriteTodo(self):
    myfile = open(self.filename, w)
    myfile.write('task_id: %s' % (self.task_id))
    myfile.write('title: %s' % (self.title))
    myfile.write('creation_date: %s' % (self.creation_date))
    myfile.write('due_date: %s' % (self.due_date))
    myfile.write('resolution_date: %s' % (self.resolution_date))
    myfile.write('tags: %s' % (self.tags))
    myfile.write('description: %s' % (self.description))
    myfile.close()

  def ReadTodo(self):
    dispatcher = {'task_id': self.SetTaskId,
                  'title': self.SetTitle,
                  'creation_date': self.SetCreationDate,
                  'due_date': self.SetDueDate,
                  'resolution_date': self.SetResolutionDate,
                  'tags': self.SetTags,
                  'description': self.SetDescription}
    
    if os.path.exists(self.todo_file):
      myfile = open(self.todo_file)
      for line in myfile:
        (descriptor, data) = line.split(':', 1)
        if dispatcher.has_key(descriptor):
          dispatcher[descriptor](data)
    
class TodoList:
  """Todo List
  """

  def __init__(self):
    self.todo_file = os.path.join(config.PYORG_CONFIG.get('PyOrganize', 'base'),
                                  'todo.txt')
    self.todo_list = dict()
    self.ReadTodoFile()

  def ReadTodoFile(self):
    if os.path.exists(self.todo_file):
      myfile = open(self.todo_file)
      for line in myfile:
        (task_id, title) = line.split(':', 1)
        todo = Todo(title=title, task_id=task_id)
        self.todo_list[task_id] = todo

  def WriteTodoFile(self):
    key_list = self.todo_list.keys()
    key_list.sort()
    myfile = open(self.todo_file, w)
    for x in key_list:
      myfile.write('%s:%s' % (x, self.todo_list[x]))
    myfile.close()

  def PrintList(self):
    key_list = self.todo_list.keys()
    key_list.sort()
    for x in key_list:
      self.todo_list[x].PrintSummary()

  def AddTodo(self, title):
    todo = ToDo(title=title)
    self.WriteTodoFile()
