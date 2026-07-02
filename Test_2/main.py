import os
import requests

# définition de l'adresse de l'API
api_address = 'api'
# port de l'API
api_port = 8000

# requête 1
r = requests.get(
    url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'test'
    }
)

output = '''
============================
    Authorization test
============================

request done at "/v1/sentiment"
| username="alice"
| password="wonderland"
| sentence="test"

Expected result = 200; 
actual result = {status_code}

==>  {test_status}
'''

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
output = output.format(status_code=status_code, test_status=test_status)
print(output)

# impression dans un fichier
if os.environ.get('LOG') == '1':
    with open('api_test.log', 'a') as file:
        file.write(output)

# requête 2
r = requests.get(
    url='http://{address}:{port}/v2/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'test'
    }
)

output = '''
============================
    Authorization test
============================

request done at "/v2/sentiment"
| username="alice"
| password="wonderland"
| sentence="test"

Expected result = 200; 
actual result = {status_code}

==>  {test_status}
'''

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
output = output.format(status_code=status_code, test_status=test_status)
print(output)

# impression dans un fichier
if os.environ.get('LOG') == '1':
    with open('api_test.log', 'a') as file:
        file.write(output)

# requête 3
r = requests.get(
    url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'bob',
        'password': 'builder',
        'sentence': 'test'
    }
)

output = '''
============================
    Authorization test
============================

request done at "/v1/sentiment"
| username="bob"
| password="builder"
| sentence="test"

Expected result = 200; 
actual result = {status_code}

==>  {test_status}
'''

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
output = output.format(status_code=status_code, test_status=test_status)
print(output)

# impression dans un fichier
if os.environ.get('LOG') == '1':
    with open('api_test.log', 'a') as file:
        file.write(output)

# requête 4
r = requests.get(
    url='http://{address}:{port}/v2/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'bob',
        'password': 'builder',
        'sentence': 'test'
    }
)

output = '''
============================
    Authorization test
============================

request done at "/v2/sentiment"
| username="bob"
| password="builder"
| sentence="test"

Expected result = 403; 
actual result = {status_code}

==>  {test_status}
'''

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 403:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
output = output.format(status_code=status_code, test_status=test_status)
print(output)

# impression dans un fichier
if os.environ.get('LOG') == '1':
    with open('api_test.log', 'a') as file:
        file.write(output)