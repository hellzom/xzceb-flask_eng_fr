import json
import os
from dotenv import load_dotenv
from translate import Translator

def englishToFrench(englishText):
    #write the code here
    translator= Translator(from_lang="en",to_lang="fr")
    frenchText = translator.translate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    #write the code here
    translator1= Translator(from_lang="fr",to_lang="en")
    englishText = translator1.translate(frenchText)
    return englishText
