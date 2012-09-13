from intro import spam
import unittest


class TestIntro(unittest.TestCase):

    def test_intro(self):

        self.assertEqual(spam('Alex'), 'Hello world, Alex')
        # Check out http://docs.python.org/library/unittest.html#assert-methods for more assert methods

        # Uncomment the line below to use the pdb (interactive python debugger)
        # import pdb; pdb.set_trace()
