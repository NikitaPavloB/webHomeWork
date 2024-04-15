import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from send_email import EmailSender

with open('datatest.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    browser_name = data['browser']


@pytest.fixture(scope='session')
def browser():
    if browser_name == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)

    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope='session', autouse=True)
def send_email_after_tests():
    # инициализация EmailSender с данными
    email_sender = EmailSender(
        fromaddr='izmaylov.zhenya@list.ru',
        toaddr='izmaylov.zhenya@list.ru',
        password='77BMFcRQicQaxYCz9K1b',
        reportname='log.txt'
    )
    # выполнение отправки email после всех тестов
    yield

    # выполнение отправки email
    email_sender.send_email()

