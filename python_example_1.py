import requests
import logging

logging.basicConfig(filename='output.log', encoding='utf-8', level=logging.DEBUG)

hostname = 'acme.com'

user = 'MyServiceAccount'
password = 'SecurePass123!@#'

session = requests.Session()
session.auth = (user, password)

auth = session.post('https://' + hostname)
response = session.get('https://' + hostname + '/rest/applications')
