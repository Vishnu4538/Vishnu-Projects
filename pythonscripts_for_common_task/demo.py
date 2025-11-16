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

token="ATATT3xFfGF04kbYZD602chMvn2mEbq27yDF-90H2uvhOrYYqwvYPn7EJJpLxxUC_prnhype1dOcSy1Zh8IbO_-lbJvxVxgFJto4XdD76BdXyqDVgOrOJbaoYnc5ol99jhc3YK2k-3AHPSpMLS8FbTDAEQ9J-_a8ej2p5whq-K_QD0A7MY8KkGs=B30A91DD"
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
