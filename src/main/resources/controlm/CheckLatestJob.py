import json
from xlrelease.HttpRequest import HttpRequest as StandardHttpRequest
from controlm.HttpRequest import HttpRequest as SkipTlsVerificationHttpRequest

login_uri = "/automation-api/session/login"
query_parameters = {
    "jobname": jobname,
    "folder": folder,
    "ctm": ctm,
    "application": application,
    "subApplication": subApplication,
    "description": description,
    "jobid": jobid
}
query_parameters = ["{}={}".format(key, query_parameters[key]) for key in query_parameters.keys() if query_parameters[key] not in [None, ""]]

uri = "/automation-api/run/jobs/status?{0}".format("&".join(query_parameters))

if server["skipTlsVerification"]:
    request = SkipTlsVerificationHttpRequest(server, username, password)
else:
    request = StandardHttpRequest(server, username, password)
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
response = request.get(uri, body="", headers=headers, contentType="application/json")

if response.isSuccessful():
    try:
        latest_job = json.loads(response.getResponse())["statuses"][0]
    except KeyError:
        print("The specified job has never been run\n")
        raise Exception(response.status, response.headers, response.response)
else:
    response.errorDump()
    raise Exception(response.status, response.headers, response.response)

status = latest_job["status"]
if status == "Ended OK":
    print(
        "Job: {0} ({1})\n".format(latest_job["name"], latest_job["jobId"]) + \
        "Status: {0}\n".format(status) + \
        "Output: [{0}]({0})\n".format(latest_job["outputURI"]) + \
        "Log: [{0}]({0})\n".format(latest_job["logURI"])
    )
    task.setStatusLine("{0}".format(status))
elif status == "Ended Not OK" or status == "Status Unknown":
    print(
        "Job: {0} ({1})\n".format(latest_job["name"], latest_job["jobId"]) + \
        "Status: {0}\n".format(status) + \
        "Output: [{0}]({0})\n".format(latest_job["outputURI"]) + \
        "Log: [{0}]({0})\n".format(latest_job["logURI"])
    )
    raise Exception("Job Has Status Failed or Unknown: {0} ({1})".format(latest_job["name"], latest_job["jobId"]))
else:
    task.setStatusLine("{0}".format(status))
    task.schedule("controlm/CheckLatestJob.py", pollFrequency)

jobidOutput = latest_job["jobId"]
status = status
outputURI = latest_job["outputURI"]
logURI = latest_job["logURI"]