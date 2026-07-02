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
        'sentence': 'life is beautiful'
    }
)

output = '''
============================
    Content test
============================

request done at "/v1/sentiment"
| username="alice"
| password="wonderland"
| sentence="life is beautiful"

Expected result > 0; 
actual result = {score}

==>  {test_status}
'''

# résultat de la requête
score = r.json()['score']

# affichage des résultats
if score > 0:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
output = output.format(score=score, test_status=test_status)
print(output)

# impression dans un fichier
if os.environ.get('LOG') == '1':
    with open('api_test.log', 'a') as file:
        file.write(output)

# requête 2
r = requests.get(
    url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'that sucks'
    }
)

output = '''
============================
    Content test
============================

request done at "/v1/sentiment"
| username="alice"
| password="wonderland"
| sentence="that sucks"

Expected result < 0; 
actual result = {score}

==>  {test_status}
'''

# résultat de la requête
score = r.json()['score']

# affichage des résultats
if score < 0:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
output = output.format(score=score, test_status=test_status)
print(output)

# impression dans un fichier
if os.environ.get('LOG') == '1':
    with open('api_test.log', 'a') as file:
        file.write(output)

# requête 3
r = requests.get(
    url='http://{address}:{port}/v2/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'life is beautiful'
    }
)

output = '''
============================
    Content test
============================

request done at "/v2/sentiment"
| username="alice"
| password="wonderland"
| sentence="life is beautiful"

Expected result > 0; 
actual result = {score}

==>  {test_status}
'''

# résultat de la requête
score = r.json()['score']

# affichage des résultats
if score > 0:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
output = output.format(score=score, test_status=test_status)
print(output)

# impression dans un fichier
if os.environ.get('LOG') == '1':
    with open('api_test.log', 'a') as file:
        file.write(output)

# requête 4
r = requests.get(
    url='http://{address}:{port}/v2/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'that sucks'
    }
)

output = '''
============================
    Content test
============================

request done at "/v2/sentiment"
| username="alice"
| password="wonderland"
| sentence="that sucks"

Expected result < 0; 
actual result = {score}

==>  {test_status}
'''

# résultat de la requête
score = r.json()['score']

# affichage des résultats
if score < 0:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
output = output.format(score=score, test_status=test_status)
print(output)

# impression dans un fichier
if os.environ.get('LOG') == '1':
    with open('api_test.log', 'a') as file:
        file.write(output)
