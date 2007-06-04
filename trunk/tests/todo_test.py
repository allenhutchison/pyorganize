#!/usr/bin/python

__author__ = 'allen@hutchison.org (Allen Hutchison)'

import datetime
import unittest
from pyorganize import todo

class TodoTest(unittest.TestCase):
  
  def setUp(self):
    self.todo = todo.Todo()
  
  def testEmptyTitle(self):
    self.assert_(self.todo.title is None)
  
  def testEmptyDescription(self):
    self.assert_(self.todo.description is None)
  
  def testEmptyTags(self):
    self.assert_(self.todo.tags is None)
  
  def testEmptyTaskId(self):
    self.assert_(self.todo.task_id is None)
  
  def testEmptyResolutionDate(self):
    self.assert_(self.todo.resolution_date is None)
  
  def testEmptyDueDate(self):
    self.assert_(self.todo.due_date is None)

  def testCreationDate(self):
    today = datetime.datetime.today()
    self.assert_(self.todo.creation_date.date() == today.date())

  def testComplete(self):
    today = datetime.datetime.today()
    self.todo.Complete()
    self.assert_(self.todo.resolution_date.date() == today.date())
  
  
if __name__ == '__main__':
  unittest.main()
