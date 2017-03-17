CSNews
======

.. image:: https://badge.fury.io/py/csnews.svg
    :target: https://badge.fury.io/py/csnews
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/urtzai/csnews.svg?branch=master
    :target: https://travis-ci.org/urtzai/csnews

.. image:: https://coveralls.io/repos/github/urtzai/csnews/badge.svg?branch=master
    :target: https://coveralls.io/github/urtzai/csnews?branch=master

.. image:: https://landscape.io/github/urtzai/csnews/master/landscape.svg?style=flat
    :target: https://landscape.io/github/urtzai/csnews/master
    :alt: Code Health

.. image:: https://requires.io/github/urtzai/csnews/requirements.svg?branch=master
    :target: https://requires.io/github/urtzai/csnews/requirements/?branch=master
    :alt: Requirements Status

.. image:: https://img.shields.io/badge/python-2.7-blue.svg
    :target: https://badge.fury.io/py/csnews
    :alt: Latest Python 2 version

.. image:: https://img.shields.io/badge/python-3.5-blue.svg
    :target: https://badge.fury.io/py/csnews
    :alt: Latest Python 3 version

News module for Django

Dependencies
------------

* Django>=1.8
* django-photologue>=3.6
* django-tinymce>=2.6.0

Instalation
-----------

.. code-block:: python

    INSTALLED_APPS = [
        'csnews',
    ]

Then apply migrations: 

.. code-block::

    ./manage.py migrate csnews

Finally, add this in ``urls.py``:

.. code-block:: django

    url(r'^news/', include('csnews.urls')),

Support
-------

Should you experience any issues do not hesistate to post an issue or contribute in this project pulling requests.

Travis CI status
----------------

We use Travis to check that the unit test suite is working against various combinations of Python, Django, etc...
`Click here for the full report <http://travis-ci.org/#!/urtzai/csnews>`_.
