from page_objects.registration_page import RegistrationPage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pytest

from common.usernames import incorrect_usernames 
from common.text_elements import TextElements
from common.emails import incorrect_emails
from common.passwords import incorrect_passwords


@pytest.mark.parametrize("username", incorrect_usernames)
def test_invalid_username_field(driver: webdriver, username: str):
    """
    Проверяем, что при вводе username'а неверного формата появляется
    предупреждающие сообщение.

    При вводе пустого значения, сообщение другое - Обязательное поле.

    Как проверяем:
    1. Вводим неверное значение имени пользователя;
    2. Смотрим, что надпись появилась.
    """
    page = RegistrationPage(driver, window_size=(640, 500))
    username_field = page.find_element_from_shadow_dom(By.CSS_SELECTOR, page.USER_NAME_FIELD)
    username_field.send_keys(username)
    action = ActionChains(driver)
    action.send_keys(Keys.TAB).perform()


    warning_element = page.find_element_from_shadow_dom(By.CSS_SELECTOR, page.WARNING_ELEMENT_USERNAME)
    assert warning_element.text == TextElements.WARNING_INVALID_USERNAME


@pytest.mark.parametrize("email", incorrect_emails)
def test_invalid_email_field(driver: webdriver, email: str):
    """
    Проверяем, что при вводе email'а неверного формата появляется
    предупреждающее сообщение.

    Как проверяем:
    1. Вводим неверное значение имени пользователя;
    2. Смотрим, что надпись появилась.
    """
    page = RegistrationPage(driver, window_size=(640, 500)) 
    email_field = page.find_element_from_shadow_dom(By.CSS_SELECTOR, page.EMAIL_FIELD)
    email_field.send_keys(email)
    action = ActionChains(driver)
    action.send_keys(Keys.TAB).perform()


    warning_element = page.find_element_from_shadow_dom(By.CSS_SELECTOR, page.WARNING_ELEMENT_EMAIL)
    assert warning_element.text == TextElements.WARNING_INVALID_EMAIL


@pytest.mark.parametrize("password", incorrect_passwords)
def test_invalid_password_field(driver: webdriver, password: str):
    """
    Проверяем, что при вводе email'а неверного формата появляется
    предупреждающее сообщение.

    Как проверяем:
    1. Вводим неверное значение имени пользователя;
    2. Смотрим, что надпись появилась.
    """
    page = RegistrationPage(driver, window_size=(640, 500))  
    email_field = page.find_element_from_shadow_dom(By.CSS_SELECTOR, page.PASSWORD_FIELD)
    email_field.send_keys(password)
    action = ActionChains(driver)
    action.send_keys(Keys.TAB).perform()

    if len(password) < 8:
        warning_element = page.find_element_from_shadow_dom(By.CSS_SELECTOR, page.WARNING_ELEMENT_PASSWORD)
        assert warning_element.text == TextElements.WARNING_INVALID_PASSWORD_LEN
    else:
        warning_element = page.find_element_from_shadow_dom(By.CSS_SELECTOR, page.WARNING_ELEMENT_PASSWORD)
        assert warning_element.text == TextElements.WARNING_INVALID_PASSWORD