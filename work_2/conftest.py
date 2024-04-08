import pytest
import yaml

from module import Site

with open('datatest.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def login_with_credentials(site, set_locator1, set_locator2):
    # Вводим логин
    selector1 = set_locator1
    input1 = site.find_element('xpath', selector1)
    input1.send_keys(data['login'])
    # Вводим пароль
    selector2 = set_locator2
    input2 = site.find_element('xpath', selector2)
    input2.send_keys(data['password'])


@pytest.fixture(scope='module')
def site():
    site_instance = Site(data['address'])
    yield site_instance
    site_instance.quit()


# Ввести пароль
@pytest.fixture()
def set_locator1():
    return '''//*[@id="login"]/div[1]/label/input'''


# Ввести логин
@pytest.fixture()
def set_locator2():
    return '''//*[@id="login"]/div[2]/label/input'''


# Нажать кнопку логин
@pytest.fixture()
def set_locator3():
    return '''button'''


# Проверка отображения ошибки
@pytest.fixture()
def set_locator4():
    return '''h2'''


# Проверка слова "Home"
@pytest.fixture()
def set_locator5():
    return '''//*[@id="app"]/main/nav/a'''


# Проверка ошибки
@pytest.fixture()
def set_error():
    return '401'


# Создание нового поста
# Нажать на кнопку создать новый пост
@pytest.fixture()
def create_new_post():
    return '''/html/body/div[1]/main/div/div[2]/div[1]/button'''


# Ввод титула
@pytest.fixture
def post_title_selector():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


# Ввод описания
@pytest.fixture
def submit_description_selector():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


# Ввод текста
@pytest.fixture
def post_content_selector():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""


# Нажать на кнопку сохранить
@pytest.fixture
def add_post_selector():
    return """//*[@id="create-item"]/div/div/div[7]/div/button/span"""
