#!/usr/bin/python
#
__author__ = 'allen@hutchison.org (Allen Hutchison)'

import datetime
import os
from pyorganize import config
from pyorganize import todo

class TodoList:
  """Todo List
  """

  def __init__(self):
    self.todo_file = os.path.join(config.PYORG_CONFIG.get('PyOrganize', 'base'),
                                  'todo.txt')
    self.last_task_id = 0
    self.disk_sync = 0

    self.todo_list = dict()
    self.ReadTodoFile()

  def __del__(self):
    self.WriteTodoFile()

  def ReadTodoFile(self):
    if os.path.exists(self.todo_file):
      myfile = open(self.todo_file)
      for line in myfile:
        (task_id, title) = line.split(':', 1)
        self.AddTodo(task_id=task_id, title=title)
      self.disk_sync = 1

  def WriteTodoFile(self):
    if self.disk_sync is 0:
      key_list = self.todo_list.keys()
      key_list.sort()
      myfile = open(self.todo_file, 'w')
      for x in key_list:
        myfile.write('%s:%s\n' % (x, self.todo_list[x].title))
      myfile.close()

  def PrintList(self):
    key_list = self.todo_list.keys()
    key_list.sort()
    for x in key_list:
      self.todo_list[x].PrintSummary()

  def AddTodo(self, task_id=None, title=None):
    if task_id is None:
      task_id = self.GetNextTaskId()
    todo_item = todo.Todo(title=title, task_id=task_id)
    self.todo_list[todo_item.task_id] = todo_item
    if task_id > self.last_task_id: self.last_task_id = task_id
    self.disk_sync = 0
    return task_id

  def GetNextTaskId(self):
    return self.last_task_id + 1

  def Save(self):
    self.WriteTodoFile()
    self.disk_sync = 1
    for x in self.todo_list.keys():
      self.todo_list[x].WriteTodo()

  def EditTask(self, task_id):
    self.todo_list[task_id].Edit()

  def PrintTask(self, task_id):
    self.todo_list[task_id].Print()
