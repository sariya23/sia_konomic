from page_objects.registration_page import RegistrationPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import pytest

from tests.common.window_sizes import COMMON_WINDOW_SIZES


@pytest.mark.parametrize("window_size", COMMON_WINDOW_SIZES)
def test_username_field(driver: webdriver, window_size: tuple[int, int]):
    """
    Проверяем, что если не ввести имя пользователя, то появится прудпреждающая
    надпись.

    Как проверяем:
    1. Кликаем на поле с именем пользователя;
    2. Кликаем на любое другое поле;ш
    3. Смотрим, что под полем имя пользователя появилась надпись 'Поле не заполнено'.
    """
    _ = RegistrationPage(driver, window_size=(640, 500))
    wait = WebDriverWait(driver, 20)
    _ = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='router-link-active'])[1]")))
    shadow_host = driver.find_element(By.CSS_SELECTOR, ".remoteComponent")
    shadow_root = shadow_host.shadow_root
    username_field = shadow_root.find_element(By.CSS_SELECTOR, "#input-135")
    username_field.click()
    email_field = shadow_root.find_element(By.CSS_SELECTOR, "#username")
    email_field.click()

    warning_text = shadow_root.find_element(By.CSS_SELECTOR, "div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(1) > div > div > div.v-text-field__details > div > div > div > div > div > span") 
    assert warning_text.text == 'Поле не заполнено'