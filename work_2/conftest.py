import pytest
import yaml
from module import Site

with open('datatest.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def set_locator1():
    return '''//*[@id="login"]/div[1]/label/input'''


@pytest.fixture()
def set_locator2():
    return '''//*[@id="login"]/div[2]/label/input'''


@pytest.fixture()
def set_locator3():
    return '''button'''


@pytest.fixture()
def set_locator4():
    return '''h2'''

@pytest.fixture()
def set_locator5():
    return '''//*[@id="app"]/main/nav/a'''

@pytest.fixture()
def set_error():
    return '401'

@pytest.fixture()
def site():
    site_instance = Site(data['address'])
    yield site_instance
    site_instance.quit()


# Создание нового поста
@pytest.fixture()
def create_new_post():
    return '''/html/body/div[1]/main/div/div[2]/div[1]/button'''

@pytest.fixture
def post_title_selector():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""

@pytest.fixture
def submit_description_selector():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""

@pytest.fixture
def post_content_selector():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""

@pytest.fixture
def add_post_selector():
    return """//*[@id="create-item"]/div/div/div[7]/div/button/span"""
