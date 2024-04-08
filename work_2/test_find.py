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
