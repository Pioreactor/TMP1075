#!/usr/bin/env python

from distutils.core import setup

with open("requirements.txt") as f:
    REQUIREMENTS = f.read().splitlines()

with open("README.md") as f:
    LONG_DESCRIPTION, LONG_DESC_TYPE = f.read(), "text/markdown"


setup(name='TMP1075',
      version='0.1',
      description='A python wrapper for interacting with the TMP1075',
      author='Cam Davidson-Pilon',
      author_email='cam@pioreactor.com',
      url='https://github.com/Pioreactor/TMP1075',
      packages=['TMP1075'],
      license="MIT",
      python_requires=">=3.6",
      install_requires=REQUIREMENTS,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
     )