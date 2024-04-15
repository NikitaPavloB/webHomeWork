from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml

with open('datatest.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, data['LOGIN_FIELD'])
    LOCATOR_PASS_FIELD = (By.XPATH, data['PASS_FIELD'])
    LOCATOR_LOGIN_BIN = (By.CSS_SELECTOR, data['LOGIN_BIN'])
    LOCATOR_ERROR_FIELD = (By.XPATH, data['ERROR_FIELD'])
    LOCATOR_CHECK_TEXT = (By.XPATH, data['CHECK_TEXT'])
    LOCATOR_CHECK_CONTACT = (By.XPATH, data['CHECK_CONTACT'])
    LOCATOR_CHECK_CONTACTUS = (By.XPATH, data['CHECK_CONTACTUS'])
    LOCATOR_CHECK_NAME = (By.XPATH, data['CHECK_NAME'])
    LOCATOR_CHECK_EMAIL = (By.XPATH, data['CHECK_EMAIL'])
    LOCATOR_CHECK_CONTENT = (By.XPATH, data['CHECK_CONTENT'])
    LOCATOR_CONTACT_BIN = (By.XPATH, data['CONTACT_BIN'])
    LOCATOR_NEW_POST = (By.XPATH, data['new_post'])
    LOCATOR_POST_TITLE = (By.XPATH, data['post_title'])
    LOCATOR_DESCRIPTION_SELECTOR = (By.XPATH, data['description_selector'])
    LOCATOR_POST_CONTENT = (By.XPATH, data['post_content'])
    LOCATOR_ADD_POST = (By.XPATH, data['add_post'])
    LOCATOR_CHECK_TITLE = (By.XPATH, data['check_title'])


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

    def click_new_post(self):
        logging.info('Click new post button')
        self.find_element(TestSearchLocators.LOCATOR_NEW_POST).click()

    def enter_post_title(self, title):
        logging.info(f'Send {title} to title field')
        title_field = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE)
        title_field.clear()
        title_field.send_keys(title)

    def enter_description(self, description):
        logging.info(f'Send {description} to description field')
        description_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION_SELECTOR)
        description_field.clear()
        description_field.send_keys(description)

    def enter_post_content(self, post):
        logging.info(f'Send {post} to post field')
        post_field = self.find_element(TestSearchLocators.LOCATOR_POST_CONTENT)
        post_field.clear()
        post_field.send_keys(post)

    def click_add_post(self):
        logging.info('Click add_post button')
        self.find_element(TestSearchLocators.LOCATOR_ADD_POST).click()

    def get_check_title(self):
        check_title = self.find_element(TestSearchLocators.LOCATOR_CHECK_TITLE, time=3)
        new_title = check_title.text
        logging.info(f'We found check {new_title} checkbox for creating a post {TestSearchLocators.LOCATOR_CHECK_TITLE[1]}')
        return new_title
