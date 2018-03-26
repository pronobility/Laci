import requests
import json

headerInfo = {'content-type': 'application/json' }
payload = {'text': 'okay!!!', 'auth_token': 'aasdasdasdasd'}
jLoad = json.dumps(payload)

r = requests.post('http://example.com:3030/widgets/init', headers=headerInfo, data=jLoad)
print (r.text)
print (r.status_code)
