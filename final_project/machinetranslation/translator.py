# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=trailing-newlines
# pylint: disable=trailing-whitespace
# pylint: disable=missing-final-newline
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)

## tranlator_instance
langTransltr=LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
langTransltr.set_service_url(url)
## Screen Shot translator_instance


## e2f_translator_function
def english_to_french(english_test):
    if english_test == "":
     return "ERROR"
    result=langTransltr.translate(text = english_test,model_id='en-fr').get_result()
    french_test=result["translations"][0]["translation"]
    return french_test
## e2f_translator_function

## f2e_translator_function
def french_to_english(french_test):
     if french_test == "":
      return "ERROR"
     result=langTransltr.translate(text = french_test,model_id='fr-en').get_result()
     english_test=result["translations"][0]["translation"]
     return english_test
