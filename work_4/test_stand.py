import time

import pytest
import yaml
from testpage import OperationsHelper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


with open('datatest.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


def test_1(browser):
    test_page = OperationsHelper(browser, data['address'])
    test_page.go_to_site()
    test_page.enter_login('test')
    test_page.enter_pass('test')
    test_page.click_login_button()
    assert test_page.get_error_text() == data['status_error']


def test_2(browser):
    test_page = OperationsHelper(browser, data['address'])
    test_page.go_to_site()
    test_page.enter_login(data['login'])
    test_page.enter_pass(data['password'])
    test_page.click_login_button()
    assert test_page.get_check_text() == f'Home'


def test3_create_post(browser):
    test_page = OperationsHelper(browser, data['address'])

    browser.delete_all_cookies()  # Удаление cookies
    browser.execute_script("window.localStorage.clear();")  # Очистка localStorage
    browser.execute_script("window.sessionStorage.clear();")  # Очистка sessionStorage

    browser.get(data['address'])  # Навигация на стартовую страницу

    test_page.go_to_site()
    test_page.enter_login(data['login'])
    test_page.enter_pass(data['password'])
    test_page.click_login_button()

    test_page.click_new_post()
    test_page.enter_post_title(data['new_post_title'])
    test_page.enter_description(data['new_post_description'])
    test_page.enter_post_content(data['new_post_content'])
    test_page.click_add_post()

    time.sleep(3)

    assert test_page.get_check_title() == data['new_post_title']


def test_4(browser):
    test_page = OperationsHelper(browser, data['address'])

    browser.delete_all_cookies()  # Удаление cookies
    browser.execute_script("window.localStorage.clear();")  # Очистка localStorage
    browser.execute_script("window.sessionStorage.clear();")  # Очистка sessionStorage

    browser.get(data['address'])  # Навигация на стартовую страницу

    test_page.go_to_site()
    test_page.enter_login(data['login'])
    test_page.enter_pass(data['password'])
    test_page.click_login_button()

    assert test_page.get_check_text() == 'Home'
    test_page.click_contact_button()

    assert test_page.is_contact_us_page_open(), "Failed to open Contact Us page"
    test_page.enter_name('Nikita Pavlov')
    test_page.enter_email('nikpav@yandex.ru')
    test_page.enter_content('This is a test message for Contact Us form')

    # Отправляем форму
    test_page.click_submit_button()

    # Проверяем появление всплывающего alert
    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    assert "Form successfully submitted" in alert.text

    # Закрываем alert
    alert.accept()


if __name__ == '__main__':
    pytest.main(['-vv'])

