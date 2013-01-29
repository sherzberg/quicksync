================
quicksync
================
v.1 - 2012-04-06
----------------

This is a simple command line wrapper application that aids in syncing folders using
rsync. The input is a file that contains the folders to sync. Folders must
be mounted locally. The current testing environment syncs local folders to
smb mounted shares.

Can be setup to run with cron.

Requirements
============

quicksync is tested with (may work with other versions):

* Python 2.7.3
* rsync 3.0.9

**Currently quicksync has only been tested in Linux. Windows and Mac support
will be comming in future releases**
    
Features (that currently work):
===============================

* Multi-folder sync (locally mounted folders only)

Usage
=====

The configuration file is like an INI file. More to come later 
Create a file called ~/folders-to-sync.qs with these contents:

::

    [folders]
    /path/to/folder/to/sync;/path/to/folder/to/sync/to
    /another/path/to/folder/to/sync;/another/path/to/folder/to/sync/to

Then to sync the folders, execute this:

::

    $ bin/quicksync ~/folders-to-sync.qs

