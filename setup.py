#!/usr/bin/python
#
#
from distutils.core import setup

setup(name='pypim',
      version='0.1',
      description="Python PIM Application",
      author='Allen Hutchison',
      author_email='allen@hutchison.org',
      license='Apache 2.0',
      url='http://code.google.com/p/pypim/',
      packages=['pyorganize'],
      package_dir={'pyorganize':'src/pyorganize'}
      )
