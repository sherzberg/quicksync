import unittest
import uuid
import argparse

from quicksync import QuickSyncArgumentParser

class QuickSyncArgumentParserTest(unittest.TestCase):
  
    def setUp(self):
        self.fname = '/tmp/%s.cfg' % uuid.uuid4()

    def tearDown(self):
        pass

    def test_parse_args_success(self):
        parser = QuickSyncArgumentParser()

        fh = open(self.fname, 'w')
        fh.write('hi')
        fh.close()

        result = parser.parse_args(['-c', self.fname])

        self.assertEqual('hi', result.configfile.read())

