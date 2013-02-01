import unittest
import io

from quicksync import QuickSyncConfigParser

sample_ini='''
[config]
stuff=value
other=nextvalue
[folders]
/folder1;/myfolder1
/Folder2;/MyFolder2
'''

class TestConfigParser(unittest.TestCase):

    def test_get_folders(self):
        cp = QuickSyncConfigParser()
        cp.readfp(io.BytesIO(sample_ini))

        result = cp.get_folders()

        self.assertEqual(2, len(result))

        folder1 = result[0]
        self.assertEqual('/folder1', folder1[0])
        self.assertEqual('/myfolder1', folder1[1])

        folder2 = result[1]
        self.assertEqual('/Folder2', folder2[0])
        self.assertEqual('/MyFolder2', folder2[1])

    def test_get_config(self):
        cp = QuickSyncConfigParser()
        cp.readfp(io.BytesIO(sample_ini))

        result = cp.get_config()

        self.assertEqual(2, len(result.keys()))
        self.assertEqual('value', result['stuff'])
        self.assertEquals('nextvalue', result['other'])

