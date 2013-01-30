import argparse
from argparse import ArgumentParser

#_parser = argparse.ArgumentParser(description='This program will sync two folders.')
#_parser.add_argument('inputfile', help='input file to read the sync information from')
#_parser.add_argument('--simulate', action='store_true', help='Simulates the sync, does not actually do anything')

#args = _parser.parse_args()

class QuickSyncArgumentParser(ArgumentParser):

    def __init__(self):
        ArgumentParser.__init__(self, description='''This program will sync one
        folder to another''')

        self.add_argument(
                '-c',
                '--configfile',
                type=argparse.FileType('r'),
                default='quicksync.cfg',
                help='''config file to read sync info from'''
                )
        self.add_argument(
                '-s',
                '--simulate',
                action='store_true',
                help='''Simulates the sync, does not actually do folder
                syncing'''
                )


