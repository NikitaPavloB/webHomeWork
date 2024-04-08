import time

import yaml
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from module import Site

with open('datatest.yaml') as f:
    data = yaml.safe_load(f)

site = Site(data['address'])


def test_1(site, set_locator1, set_locator2, set_locator3, set_locator4, set_error):
    selector1 = set_locator1
    input1 = site.find_element('xpath', selector1)
    input1.send_keys('kto')
    selector2 = set_locator2
    input2 = site.find_element('xpath', selector2)
    input2.send_keys('lox')
    selector3 = set_locator3
    input3 = site.find_element('css', selector3)
    input3.click()
    selector4 = set_locator4
    find1 = site.find_element('css', selector4)
    assert find1.text == set_error


def test_2_login(site, set_locator1, set_locator2, set_locator3, set_locator4, set_locator5, set_error):
    selector1 = set_locator1
    input1 = site.find_element('xpath', selector1)
    input1.send_keys(data['login'])
    selector2 = set_locator2
    input2 = site.find_element('xpath', selector2)
    input2.send_keys(data['password'])
    selector3 = set_locator3
    input3 = site.find_element('css', selector3)
    input3.click()

    try:
        # Используем явное ожидание для появления элемента для успешной авторизации
        wait = WebDriverWait(site.driver, 10)
        logged_in_element = wait.until(EC.presence_of_element_located((By.XPATH, set_locator5)))
        print("Авторизация прошла успешно!")
    except TimeoutException:
        # В случае неудачной авторизации выводим сообщение об ошибке
        print("Ошибка: Элемент для успешной авторизации не найден на странице.")


def test_add_post(site, login_with_credentials, set_locator3, create_new_post, post_title_selector, submit_description_selector, post_content_selector, add_post_selector):
    selector3 = set_locator3
    input3 = site.find_element('css', selector3)
    input3.click()

    new_post = site.find_element(By.XPATH, create_new_post)
    new_post.click()

    # Вводим заголовок и содержимое поста
    post_title = site.find_element(By.XPATH, post_title_selector)
    post_title.send_keys('Домашнее задание №2')

    post_description = site.find_element(By.XPATH, submit_description_selector)
    post_description.send_keys('Тестовый пост')

    post_content = site.find_element(By.XPATH, post_content_selector)
    post_content.send_keys('Выполненное второе домашнее задание')

    # Нажимаем кнопку отправки поста
    submit_post = site.find_element(By.XPATH, add_post_selector)
    # print("Элемент для клика найден:", submit_post.is_displayed())
    submit_post.click()

    time.sleep(data['sleep_time'])

    # Добавляем явное ожидание для проверки появления названия поста на странице
    wait = WebDriverWait(site.driver, 10)
    try:
        post_title_on_page = wait.until(EC.presence_of_element_located((By.XPATH, post_title_selector)))
        assert post_title_on_page.text == 'Домашнее задание №2'
    except TimeoutException:
        print("Название поста не найдено на странице")
