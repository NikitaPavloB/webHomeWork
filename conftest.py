import json
import pytest
import requests
import yaml

with open("config.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)
S = requests.Session()


@pytest.fixture()
def auth_token():
    response = S.post(url=data['login_url'], data={"username": data['username'], "password": data['password']})

    formatted_response = json.dumps(response.json(), indent=4, ensure_ascii=False)
    print("Response from server:", formatted_response)

    if response.status_code == 200:
        return response.json()['token']

@pytest.fixture()
def get_title_post():
    return 'Kek'
