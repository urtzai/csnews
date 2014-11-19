from setuptools import setup, find_packages
import sys, os

version = '1.9'

setup(name='csnews',
      version=version,
      description="Simple news module",
      long_description=open("README.md").read(),
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Urtzi Odriozola',
      author_email='uodriozola@codesyntax.com',
      url='http://www.codesyntax.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'django-photologue',
          'django-tinymce',
      ],
      entry_points="""
# -*- Entry points: -*-
""",
      )
