import json
from xlrelease.HttpRequest import HttpRequest as StandardHttpRequest
from controlm.HttpRequest import HttpRequest as SkipTlsVerificationHttpRequest

# get the configuration properties from the UI
params = {
    'url': configuration.url,
    'authenticationMethod': configuration.authenticationMethod,
    'username': configuration.username,
    'password': configuration.password,
    'domain': configuration.domain,
    'proxyHost': configuration.proxyHost,
    'proxyPort': configuration.proxyPort,
    'proxyUsername': configuration.proxyUsername,
    'proxyPassword': configuration.proxyPassword
}

login_uri = "/automation-api/session/login"
body = {
    "username": configuration.username,
    "password": configuration.password
}

if configuration.skipTlsVerification:
    request = SkipTlsVerificationHttpRequest(params)
else:
    request = StandardHttpRequest(params)
response = request.post(login_uri, body=json.dumps(body), contentType="application/json")

if not response.isSuccessful():
    response.errorDump()
    raise Exception(
        "Error fetching Bearer token for authentication",
        response.status,
        response.headers,
        response.response
    )