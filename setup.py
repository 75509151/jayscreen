# coding: utf-8

import sys
import os
from setuptools import setup, find_packages
import ast

NAME = 'jscreen'
DESCRIPTION = 'console user interface create for jay'
URL = 'https://github.com/75509151/jayscreen'
EMAIL = '75509151@qq.com'
AUTHOR = 'jay'
REQUIRES_PYTHON = '>=2.7.0'
VERSION = None

here = os.path.abspath(os.path.dirname(__file__))

with open('jscreen/__version__.py', 'rb') as f:
    exec(f.read())

with open('README.md') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requires = f.read()


setup(name=NAME, version=VERSION,
      author=AUTHOR,
      author_email=EMAIL,
      python_requires=REQUIRES_PYTHON,
      url=URL,
      long_description=long_description,
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      description=DESCRIPTION,
      )
