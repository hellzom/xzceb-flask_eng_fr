import unittest
from translator import frenchToEnglish, englishToFrench

class TestMethods(unittest.TestCase):
    
    def test_e2f(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') #translates eng to fr
    
    def test_f2e(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') #translates fr to en

unittest.main()