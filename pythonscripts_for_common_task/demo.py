<<<<<<< HEAD
import devops_module as dev
import sys

nuk=int(sys.argv[1])

path=sys.argv[2]


dev.update_image(nuk,path)


=======
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://edlavishnu2000.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth("edlavishnu2000@gmail.com", token)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(response.text)

output=json.loads(response.text)

print(output[0][""])
>>>>>>> 45587dd (resolved)
