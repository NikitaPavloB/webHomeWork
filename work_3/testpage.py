from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


with open('datatest.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    # browser_name = data['browser']


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, '''//*[@id="login"]/div[1]/label/input''')
    LOCATOR_PASS_FIELD = (By.XPATH, '''//*[@id="login"]/div[2]/label/input''')
    LOCATOR_LOGIN_BIN = (By.CSS_SELECTOR, '''button''')
    LOCATOR_ERROR_FIELD = (By.XPATH, '''//*[@id="app"]/main/div/div/div[2]/h2''')
    LOCATOR_CHECK_TEXT = (By.XPATH, '''//*[@id="app"]/main/nav/a''')
    LOCATOR_CHECK_CONTACT = (By.XPATH, '''//*[@id="app"]/main/nav/ul/li[2]/a''')
    LOCATOR_CHECK_CONTACTUS = (By.XPATH, '''//*[@id="app"]/main/div/div/h1''')
    LOCATOR_CHECK_NAME = (By.XPATH, '''//*[@id="contact"]/div[1]/label/input''')
    LOCATOR_CHECK_EMAIL = (By.XPATH, '''//*[@id="contact"]/div[2]/label/input''')
    LOCATOR_CHECK_CONTENT = (By.XPATH, '''//*[@id="contact"]/div[3]/label/span/textarea''')
    LOCATOR_CONTACT_BIN = (By.XPATH, '''//*[@id="contact"]/div[4]/button''')


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f'Send {word} in {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f'Send {word} in {TestSearchLocators.LOCATOR_PASS_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info('Click login button')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BIN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f'We found text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}')
        return text

    def get_check_text(self):
        check_text = self.find_element(TestSearchLocators.LOCATOR_CHECK_TEXT, time=3)
        text = check_text.text
        logging.info(f'We found check {text} checkbox during login {TestSearchLocators.LOCATOR_CHECK_TEXT[1]}')
        return text

    # Проверка раздела Contact us!
    def click_contact_button(self):
        logging.info('Click contact button')
        self.find_element(TestSearchLocators.LOCATOR_CHECK_CONTACT).click()

    def is_contact_us_page_open(self):
        try:
            self.find_element(TestSearchLocators.LOCATOR_CHECK_CONTACTUS)
            return True
        except NoSuchElementException:
            return False

    def enter_name(self, name):
        logging.info(f'Send {name} to name field')
        name_field = self.find_element(TestSearchLocators.LOCATOR_CHECK_NAME)
        name_field.clear()
        name_field.send_keys(name)

    def enter_email(self, email):
        logging.info(f'Send {email} to email field')
        email_field = self.find_element(TestSearchLocators.LOCATOR_CHECK_EMAIL)
        email_field.clear()
        email_field.send_keys(email)

    def enter_content(self, content):
        logging.info(f'Send {content} to content field')
        content_field = self.find_element(TestSearchLocators.LOCATOR_CHECK_CONTENT)
        content_field.clear()
        content_field.send_keys(content)

    def click_submit_button(self):
        logging.info('Click contact button')

        # Ожидание, пока кнопка станет кликабельной
        contact_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(TestSearchLocators.LOCATOR_CONTACT_BIN)
        )

        # Прокрутка до кнопки (если нужно)
        self.driver.execute_script("arguments[0].scrollIntoView();", contact_btn)

        # Клик по кнопке
        contact_btn.click()

    def reset_page_state(self):
        self.driver.get(data['address'])


