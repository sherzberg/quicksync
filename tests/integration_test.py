
import unittest
import uuid
import os
import sys
from quicksync import QuickSyncer


def get_uuid():
    return str(uuid.uuid4())


def write(filename, content):
    fh = open(filename, 'w')
    fh.write(content)
    fh.close()


def read(filename):
    fh = open(filename, 'r')
    content = fh.read()
    fh.close()
    return content


class IntegrationTests(unittest.TestCase):

    FOLDER_IN = os.path.join('/tmp/', get_uuid())
    FOLDER_OUT = os.path.join('/tmp/', get_uuid())
    FILENAME_1 = get_uuid() + '.txt'
    FILENAME_OUT = os.path.join(FOLDER_OUT, FILENAME_1)
    FILE_1 = os.path.join(FOLDER_IN, FILENAME_1)
    CONFIGFILE = os.path.join('/tmp/', 'config.cfg')
    INI = '''
[folders]
%s/;%s
''' % (FOLDER_IN, FOLDER_OUT)

    def setUp(self):
        os.makedirs(IntegrationTests.FOLDER_IN)
        os.makedirs(IntegrationTests.FOLDER_OUT)

        write(IntegrationTests.CONFIGFILE, IntegrationTests.INI)

    def tearDown(self):
        os.remove(IntegrationTests.FILENAME_OUT)
        os.removedirs(IntegrationTests.FOLDER_OUT)

        os.remove(IntegrationTests.FILE_1)
        os.removedirs(IntegrationTests.FOLDER_IN)

    def test_sync_happy_path(self):

        write(IntegrationTests.FILE_1, 'test')

        sys.argv = ['quicksync', '-c', IntegrationTests.CONFIGFILE]

        QuickSyncer().run()

        self.assertTrue(os.path.exists(IntegrationTests.FILENAME_OUT))
        self.assertEqual('test', read(IntegrationTests.FILENAME_OUT))
