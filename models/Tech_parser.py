# https://docs.glassnode.com/basic-api/endpoints/indicators 

import json
import requests
import pandas as pd


API_KEY = '2HVedwJjsaCECXieJCYpu2qfhw9'


res = requests.get('https://api.glassnode.com/v1/metrics/indicators/sopr',
    params={'a': 'BTC', 'api_key': API_KEY})
