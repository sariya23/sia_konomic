from page_objects.registration_page import RegistrationPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pytest

from common.usernames import incorrect_usernames 
from common.text_elements import TextElements
from common.css_locators import CSSLocators
from common.xpath_locators import XPATHLocators


@pytest.mark.tags('mobile', 'tablet', 'desktop')
@pytest.mark.parametrize("username", incorrect_usernames)
def test_username_field(driver: webdriver, username: str):
    """
    Проверяем, что при вводе username'а неверного формата появляется
    предупреждающие сообщение.

    При вводе 'ничего', сообщение другое

    Как проверяем:
    1. Вводим неверное значение имени пользователя;
    2. Смотрим, что надпись появилась.
    """
    _ = RegistrationPage(driver, window_size=(640, 500))
    wait = WebDriverWait(driver, 20)
    wait.until(EC.element_to_be_clickable((By.XPATH, XPATHLocators.LOGO_ELEMENT)))
    shadow_host = driver.find_element(By.CSS_SELECTOR, CSSLocators.SHADOW_HOST)
    shadow_root = shadow_host.shadow_root
    username_field = shadow_root.find_element(By.CSS_SELECTOR, CSSLocators.USER_NAME_FIELD)
    username_field.send_keys(username)
    action = ActionChains(driver)
    action.send_keys(Keys.TAB).perform()


    warning_element = shadow_root.find_element(By.CSS_SELECTOR, CSSLocators.WARNING_ELEMENT_USERNAME)
    assert warning_element.text == TextElements.WARNING_INVALID_USERNAME