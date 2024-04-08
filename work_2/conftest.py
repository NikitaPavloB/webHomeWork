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
