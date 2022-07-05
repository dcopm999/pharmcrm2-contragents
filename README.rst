=============================
PharmCRM2 Contragents
=============================

.. image:: https://badge.fury.io/py/pharmcrm2-contragents.svg
    :target: https://badge.fury.io/py/pharmcrm2-contragents

.. image:: https://travis-ci.org/dcopm999/pharmcrm2-contragents.svg?branch=master
    :target: https://travis-ci.org/dcopm999/pharmcrm2-contragents

.. image:: https://codecov.io/gh/dcopm999/pharmcrm2-contragents/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dcopm999/pharmcrm2-contragents

PharmCRM2 Contragents

Documentation
-------------

The full documentation is at https://pharmcrm2-contragents.readthedocs.io.

Quickstart
----------

Install PharmCRM2 Contragents::

    pip install pharmcrm2-contragents

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'contragents',
        ...
    )

Add PharmCRM2 Contragents's URL patterns:

.. code-block:: python

    urlpatterns = [
        ...
        path('contragents/', include('contragents.urls')),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
