================
quicksync
================
v.1 - 2012-04-06
----------------

This is a simple command line application that aids in syncing folders using
rsync. The input is a file that contains the folders to sync. Can be setup to run
with cron.

Requirements
============

quicksync is testing with (may work with other versions):

* Python 2.7.3
* rsync 3.0.9

**Currently quicksync has only been tested in Linux. Windows and Mac support
will be comming in future releases**
    
Features (that currently work):
===============================

* Multi-folder sync

Usage
=====

Create a file called ~/folders-to-sync.qs with these contents:

::

    /path/to/folder/to/sync;/path/to/folder/to/sync/to
    /another/path/to/folder/to/sync;/another/path/to/folder/to/sync/to

Then to sync the folders, execute this:

::

    $ quicksync ~/folders-to-sync.qs

