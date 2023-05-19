# Test for null input for french_to_english
# Test for null input for english_to_french.
# Test for the translation of the world ‘Hello’ and ‘Bonjour’.
# Test for the translation of the world ‘Bonjour’ and ‘Hello’.
# Take a screenshot of your unit tests and save it as a .jpg or .png with the filename translation_unittests.
import unittest

from translator import english_to_french, french_to_english

class Testenglish_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(""),"ERROR") # Send null and check 
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        

class Testfrench_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(""),"ERROR") # Send null and check         
        self.assertEqual(french_to_english('Bonjour'),'Hello')        
        
unittest.main()
## translation_unittests