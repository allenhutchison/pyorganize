#!/usr/bin/python
#
__author__ = 'allen@hutchison.org (Allen Hutchison)'

import sys, cmd
from pyorganize import todo_list, config

class Command(cmd.Cmd):
  prompt = "PyOrganize:> "

  def __init__(self):
    cmd.Cmd.__init__(self)
    self.todo_list = todo_list.TodoList()

  def emptyline(self):
    pass

  def default(self, line):
    print "Unknown option"

  def do_exit(self, line):
    return True
  def help_exit(self):
    print "Exit PyOrganize"

  def do_task(self, line):
    if line is '':
      self.todo_list.PrintList()
    elif line.isdigit():
      self.todo_list.EditTask(line)
    else:
      task_id = self.todo_list.AddTodo(task_id=None, title=line)
      print "Task %s Added" % task_id

  def do_print(self, line):
    if line.isdigit():
      self.todo_list.PrintTask(line)

  def do_save(self, line):
    self.todo_list.Save()

def main():
  c = Command()
  c.cmdloop(intro="Welcome to PyOrganize")

if __name__ == '__main__':
  main()
