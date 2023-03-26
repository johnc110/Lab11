import requests
import json
from getpass import getpass

USER = import("Enter your username DNAC: ")
PASS = getpass("Enter your password DNAC: ")

BASEURL = 'https://sandboxdnac.cisco.com'
authAPI = "/dna/system/api/v1/auth/token"
deviceListAPI = "/dna/system/api/v1/auth/network-token"

authPayload={}
authHeaders = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
}

dnaAuth = BASEURL + authAPI

authResponse = requests.post(dnaAuth, auth=HTTPBasicAuth(USER, PASS), headers=authheaders, data=authPayload

tokenJSON = response.json()

TOKEN = tokenJSON['Token']

print("Your token was successfully generated. The value of your token is:\n" + TOKEN)

dnaDeviceList = BASEURL + deviceListAPI

getPayload={}
getHeaders = {}
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'X-Auth-Token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGVjNGU0ZjRjYTdmOTIyMmM4MmRhNjYiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4ZSJdLCJ0ZW5hbnRJZCI6IjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4NyIsImV4cCI6MTY3OTg1OTM3NiwiaWF0IjoxNjc5ODU1Nzc2LCJqdGkiOiIwMWU1YjU5ZS0wZjM5LTRmZWItYjNkMy1hNjdiZDFlYjE3MDEiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.T3Xf4MK02a-YZJ2I8GfRavmqf4urJaB8vlyqnRiYLIdqHj1Yesjcihno-byI5LOPvZKxvvDl-u7ri2IcZBi_nUMwaHv8xXDKlLRyWdc-3oq1nkPWKgGcRv0vS4300n2rYzDCKmSVUmoXLY480gWPGxIVEY_xMiKuj-3piU99YhlwVIQTlytrbG_oLrPf-mwPdo0MP2grLwcpYHeCePlBLq0NIbIAWk6CsOs9clgR62ydR9LHczam72RYON2lv37i61d4Lmvo7LZAHWZvd-K9R4dxwtTRJMY3aPQ2NFLPefkdBOcYpfNrAwyxN1zumGoSGL0hxqp8CVDfTsF61hCQhw'
}

getResponse = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
