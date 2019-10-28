import unittest
import script

class TestScript(unittest.TestCase):

    def test_list(self):
        result = script.list()
        self.assertEqual(result)