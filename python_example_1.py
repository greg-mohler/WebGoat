import requests
import logging

logging.basicConfig(filename='output.log', encoding='utf-8', level=logging.DEBUG)

user = 'MyServiceAccount'
password = 'SecurePass123!@#'

session = requests.Session()
session.auth = (user, password)

auth = session.post('http://' + hostname)
response = session.get('http://' + hostname + '/rest/applications')



