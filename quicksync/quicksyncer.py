
import logging
import os, sys
import subprocess

from argparser import QuickSyncArgumentParser
from configparser import QuickSyncConfigParser

FOLDER_SEP = ';'
RSYNC_OPTIONS = '-v -r -a --exclude=.svn --exclude=*.qs'
RSYNC_CMD = 'rsync %(OPTIONS)s %(FROM)s %(TO)s'

class QuickSyncer():

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)
        self.config_parser = QuickSyncConfigParser()
        self.arg_parser = QuickSyncArgumentParser()

    def run(self):
        args = self.arg_parser.parse_args()

        self.config_parser.readfp(args.configfile)

        self.do_sync(self.config_parser.get_folders())

    def do_sync(self, folders):
        for tup in folders:
            f, t = tup[0], tup[1]
            logging.debug('Syncing %s to %s', f, t)
            cmd = self.build_command(f, t)
            subprocess.call(cmd, shell=True)
            logging.debug('-' * 30)

    def build_command(self, f, t):
        return RSYNC_CMD %{'FROM':f, 'TO':t, 'OPTIONS': RSYNC_OPTIONS}

