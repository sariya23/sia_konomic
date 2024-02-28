import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def chrome_options() -> webdriver.ChromeOptions:
    """
    Фикстура создает и возврщает экземпляр
    класса с настройками для Chrome.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    return options


@pytest.fixture(scope="session")
def driver(chrome_options):
    driver = webdriver.ChromeOptions(chrome_options)
    yield driver
    driver.quit()