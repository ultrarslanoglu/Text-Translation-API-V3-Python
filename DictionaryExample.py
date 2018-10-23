# -*- coding: utf-8 -*-

# This simple app uses the '/dictionary/examples' resource to illustrate
# how terms in a dictionary are contexutalized.

# This sample runs on Python 2.7.x and Python 3.x.
# You may need to install requests and uuid.
# Run: pip install requests uuid


import os, requests, uuid, json

# Checks to see if the Translator Text subscription key is available
# as an environment variable. If you are setting your subscription key as a
# string, then comment these lines out.
if 'TRANSLATOR_TEXT_KEY' in os.environ:
    subscriptionKey = os.environ['TRANSLATOR_TEXT_KEY']
else:
    print('Environment variable for TRANSLATOR_TEXT_KEY is not set.')
    exit()
# If you want to set your subscription key as a string, uncomment the next line.
#subscriptionKey = 'put_your_key_here'

# If you encounter any issues with the base_url or path, make sure
# that you are using the latest endpoint: https://docs.microsoft.com/azure/cognitive-services/translator/reference/v3-0-dictionary-examples
base_url = 'https://api.cognitive.microsofttranslator.com'
path = '/dictionary/examples?api-version=3.0'
params = '&from=en&to=fr';
constructed_url = base_url + path + params

text = 'great'
translation = 'formidable'

headers = {
    'Ocp-Apim-Subscription-Key': subscriptionKey,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# Each object takes two key/value pairs: 'text' and 'translation'.
# Note: You can pass more than one object in body.
body = [{
    'text': 'great',
    'translation': 'formidable'
}]
request = requests.post(constructed_url, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': ')))
