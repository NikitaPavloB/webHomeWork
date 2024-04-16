import pytest
import requests
import yaml
import logging

logging.basicConfig(level=logging.INFO)

S = requests.Session()

with open("datatest.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)

logger = logging.getLogger(__name__)


def test1_check_post(auth_token, get_title_post):
    url = data['post_url']
    headers = {'X-Auth-Token': auth_token}
    not_my_post = {"owner": "notMe"}

    try:
        logger.info(f"Sending GET request to {url} with params: {not_my_post} and headers: {headers}")
        data_json = S.get(url=url, params=not_my_post, headers=headers).json()['data']
        res = [x['title'] for x in data_json]
        logger.info(f"Received post titles: {res}")

        assert get_title_post in res, f"Post with title '{get_title_post}' not found in received data: {res}"

    except requests.RequestException as e:
        logger.error(f"Error during GET request: {e}")
        pytest.fail(f"Failed to retrieve posts: {e}")


def test2_create_post(auth_token):
    url = data['post_url']
    headers = {'X-Auth-Token': auth_token}
    new_post_data = {
        'title': data['new_post_title'],
        'description': data['new_post_description'],
        'content': data['new_post_content']
    }

    try:
        logger.info(f"Sending POST request to {url} with data: {new_post_data} and headers: {headers}")
        response = S.post(url=url, headers=headers, json=new_post_data)
        response.raise_for_status()

        assert response.status_code == 200, f"Failed to create post. Status code: {response.status_code}"
        logger.info("Post created successfully.")

    except requests.RequestException as e:
        logger.error(f"Error during POST request: {e}")
        pytest.fail(f"Failed to create post: {e}")
