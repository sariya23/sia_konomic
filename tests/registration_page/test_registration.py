from page_objects.registration_page import RegistrationPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pytest

from common.usernames import incorrect_usernames 

@pytest.mark.parametrize("username", incorrect_usernames)
def test_username_field(driver: webdriver, username: str):
    """
    Проверяем, что при вводе username'а неверного формата появляется
    предупреждающие сообщение.

    Как проверяем:
    1. Вводим неверное значение имени пользователя;
    2. Смотрим, что надпись появилась.
    """
    _ = RegistrationPage(driver, window_size=(640, 500))
    wait = WebDriverWait(driver, 20)
    _ = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='router-link-active'])[1]")))
    shadow_host = driver.find_element(By.CSS_SELECTOR, ".remoteComponent")
    shadow_root = shadow_host.shadow_root
    username_field = shadow_root.find_element(By.CSS_SELECTOR, "#input-135")
    username_field.send_keys(username)
    action = ActionChains(driver)
    action.send_keys(Keys.TAB)
    action.perform()


    warning_element = shadow_root.find_element(By.CSS_SELECTOR, "div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(1) > div > div > div.v-text-field__details > div > div > div > div > div > span")

    assert warning_element.text == "Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы"