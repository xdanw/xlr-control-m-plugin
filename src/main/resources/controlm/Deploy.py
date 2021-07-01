import json
import sys, urllib, operator
import requests # Needed for multipart
from xlrelease.HttpRequest import HttpRequest as StandardHttpRequest
from controlm.HttpRequest import HttpRequest as SkipTlsVerificationHttpRequest

# Only if requests is being used
import os
os.environ['REQUESTS_CA_BUNDLE'] = 'ca.pem';

login_uri = "/automation-api/session/login"

uri = "/automation-api/deploy"

if server["skipTlsVerification"]:
    request = SkipTlsVerificationHttpRequest(server, username, password)
    verify = False
else:
    request = StandardHttpRequest(server, username, password)
    verify = True
body = {
    "username": server["username"],
    "password": server["password"]
}
response = request.post(login_uri, body=json.dumps(body), contentType="application/json")

if response.isSuccessful():
    username = json.loads(response.getResponse())["username"]
    token = json.loads(response.getResponse())["token"]
else:
    response.errorDump()
    raise Exception(
        "Error fetching Bearer token for authentication",
        response.status,
        response.headers,
        response.response
    )

main_call_params = {
    'url': server["url"],
    'authenticationMethod': "None",
    'username': "",
    'password': "",
    'domain': "",
    'proxyHost': server["proxyHost"],
    'proxyPort': server["proxyPort"],
    'proxyUsername': server["proxyUsername"],
    'proxyPassword': server["proxyPassword"]
}

if server["skipTlsVerification"]:
    request = SkipTlsVerificationHttpRequest(main_call_params)
else:
    request = StandardHttpRequest(main_call_params)

headers = { "Authorization": "Bearer {0}".format(token) }

# Multipart file POST
files = { 'definitionsFile': definitionsFile, 'deployDescriptorFile': descriptorFile }
headers_withCt = { "Authorization": "Bearer {0}".format(token), "Content-Type", "application/json" }

# Not supported by native httprequest
# response = request.post(uri, files=files, headers=headers, contentType="application/json")
response = requests.post(uri, files=files, headers=headers_withCt, contentType="application/json", verify=verify)

if response.isSuccessful():
    print("Success.\n")
else:
    response.errorDump()
    raise Exception(response.status, response.headers, response.response)

