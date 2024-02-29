from pageo import BasePage  # type: ignore
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from typing import Any

from tests.common.urls import URLs


class RegistrationPage(BasePage):
    base_url = URLs.BASE_URL
    url_suffix = URLs.REGISTRATION_SUFFIX

    SHADOW_HOST = ".remoteComponent"
    USER_NAME_FIELD = "#input-135"
    WARNING_ELEMENT_USERNAME = "div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(1) > div > div > div.v-text-field__details > div > div > div > div > div > span"
    EMAIL_FIELD = "#username"
    WARNING_ELEMENT_EMAIL = "div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(2) > div > div > div.v-text-field__details > div > div > div > div > div > span"
    PASSWORD_FIELD = "#new-password"
    WARNING_ELEMENT_PASSWORD = "div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(3) > div > div > div > div > div.v-text-field__details > div > div > div > div > div > span"
    LOGO_ELEMENT = "(//*[@class='router-link-active'])[1]"

    def __init__(self, driver: Any, base_url: str = None, url_suffix: str = None, window_size: tuple = (1920, 1080), cookies: list[dict[str, str]] = None, is_open: bool = True):  # type: ignore
        super().__init__(driver, base_url, url_suffix, window_size, cookies, is_open)
        self.shadow_host = self._find_element(By.CSS_SELECTOR, self.SHADOW_HOST)
        self.shadow_root = self.shadow_host.shadow_root

    def find_element_from_shadow_dom(self, by: str, selector: str, duration: int = 5) -> WebElement:
        return WebDriverWait(self.shadow_root, duration).until(EC.presence_of_element_located((by, selector)),
                                                          message=f"Не найден элемент со стратегией локатора {by} и с селектором {selector}")


if __name__ == "__main__":
    driver = webdriver.Chrome()
    page = RegistrationPage(driver, window_size=(640, 500))

    print(page.find_element_from_shadow_dom(By.CSS_SELECTOR, "#input-135"))

