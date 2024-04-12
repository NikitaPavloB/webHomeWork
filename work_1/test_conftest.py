import pytest
import requests
import yaml

S = requests.Session()

with open("config.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)

def test1_check_post(auth_token, get_title_post):
    url = data['post_url']
    headers = {'X-Auth-Token': auth_token}
    not_my_post = {"owner": "notMe"}
    data_json = S.get(url=url, params=not_my_post, headers=headers).json()['data']
    res = [x['title'] for x in data_json]
    print(res)
    assert get_title_post in res, f"Пост с заголовком '{get_title_post}' не найден среди полученных данных: {res}"

def test2_create_post(auth_token):
    url = data['post_url']
    headers = {'X-Auth-Token': auth_token}
    new_post_data = {
        'title': data['post_title'],
        'description': data['post_description'],
        'content': data['post_content']
    }
    response = S.post(url=url, headers=headers, json=new_post_data)

    assert response.status_code == 200, f"Failed to create post. Status code: {response.status_code}"

