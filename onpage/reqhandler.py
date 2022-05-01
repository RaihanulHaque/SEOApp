import requests
import base64
import json

login = "abrarnazib@gmail.com"
password = "dde01410ba2ad9e3"
encodedToken = base64.b64encode(
    f'{login}:{password}'.encode("ascii")).decode("ascii")
authorization = f'Basic {encodedToken}'


def reqhandler(input):
    url = "https://api.dataforseo.com/v3/on_page/instant_pages"

    # Creating the data field
    data = []
    payload = {}
    payload["url"] = input["url"]
    payload["enable_javascript"] = True
    payload["check_spell"] = False
    data.append(payload)
    jsondata = json.dumps(data)

    headers = {
        'Authorization': f'{authorization}',
        'Content-Type': 'application/json'
    }

    res = requests.post(url, headers=headers, data=jsondata)
    return res.json()
