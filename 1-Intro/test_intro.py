from intro import spam
import unittest

class TestIntro(unittest.TestCase):

    def test_intro(self):
        spam('Alex')
        # import pdb; pdb.set_trace()