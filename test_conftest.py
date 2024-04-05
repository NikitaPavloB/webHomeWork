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

