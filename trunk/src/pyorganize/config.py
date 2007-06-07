#!/usr/bin/python

__author__ = 'allen@hutchison.org (Allen Hutchison)'

import os
import ConfigParser

class Config(ConfigParser.ConfigParser):
  """Config Library
  """

  def __init__(self, file=None):
    ConfigParser.ConfigParser.__init__(self)
    self.file = self.__FindFile(file)
    self.read(self.file)

  def __FindFile(self, file):
    if file is None:
      file = os.path.join(os.path.expanduser("~"), ".pyorganize")
    return file

PYORG_CONFIG = Config()
