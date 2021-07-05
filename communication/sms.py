# Response:
# [ { "id":"TS-27", "status":"Success", "errorMessage":"None", "recipient":"254XXXXXXXXX" } ]
import requests
import json
SENDERID="Bismart Insurance"
sms_parameters={ "username":"bismartinsurance", "api":"f7158eae8e50", "phone":"+2540741131667", "from":SENDERID, "message": "Test one" }
resp = requests.get("https://sandbox.teleskytech.com/api/sendsms",json=json.dumps(sms_parameters))
if resp.status_code != 200:
    # This means something went wrong.
    pass
for items in resp.json():
    print(items)