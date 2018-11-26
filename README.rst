##############
mini-project-2
##############

.. image:: https://travis-ci.org/CMPUT291PROJECTF18/Mini-Project-2.svg?branch=master
    :target: https://travis-ci.org/CMPUT291PROJECTF18/Mini-Project-2
    :alt: Build Status

.. image:: https://readthedocs.org/projects/mini-project-2/badge/?version=latest
    :target: https://CMPUT291PROJECTF18-mini-project-2.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://codecov.io/gh/CMPUT291PROJECTF18/Mini-Project-2/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/severb/graypy
    :alt: Code Coverage


Requirements
============

* Python 3.4+
* libdb4.8-dev
* libdb4.8++-dev
* db-util


Overview
========

mini-project-2 is a...

TODO: finish


Installation
============

To install the Berkeley DB dependencies for mini-project-2 on Ubuntu run the
following commands:

.. code-block:: bash

    sudo add-apt-repository ppa:bitcoin/bitcoin
    sudo apt-get update
    sudo apt-get install libdb4.8-dev libdb4.8++-dev
    sudo apt-get install db-util -y

This should install the required libraries to install `bsddb3` from
`pip`, thus, allowing mini-project-2 to be properly installed.

mini-project-2 can then be installed from source by running:

.. code-block:: bash

    pip install .

Within the same directory as mini-project-2's ``setup.py`` file.


Usage
=====

After installing mini-project-2's additional usage help on starting
mini-project-2 can be obtained by running the following console command:

.. code-block:: bash

    mini-project-2 --help
