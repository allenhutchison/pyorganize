#!/usr/bin/python
#
__author__ = 'allen@hutchison.org (Allen Hutchison)'

import sys, cmd
from pyorganize import todo, journal, config

class Command(cmd.Cmd):
  prompt = "PyOrganize:> "

  def __init__(self):
    cmd.Cmd.__init__(self)
    self.todo_list = todo.TodoList()

  def emptyline(self):
    pass

  def default(self, line):
    print "Unknown option"

  def do_x(self, line):
    print "x is the spot: %s" % line

  def do_exit(self, line):
    return True
  def help_exit(self):
    print "Exit PyOrganize"

  def do_task(self, line):
    if line is '':
      self.todo_list.PrintList()
    elif line.isdigit():
      print "edit existing task"
    else:
      task_id = self.todo_list.AddTodo(line)
      print "Task %s Added" % task_id

  def help_task(self):
    print "Enter a new task or edit an existing task"

def main():
  c = Command()
  c.cmdloop(intro="Welcome to PyOrganize")

if __name__ == '__main__':
  main()
