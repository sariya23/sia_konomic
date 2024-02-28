from page_objects.registration_page import RegistrationPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_a(driver):
    _ = RegistrationPage(driver, window_size=(640, 400))
    wait = WebDriverWait(driver, 10)
    _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-header"]/div[4]/div/div[2]/a/span')))
    shadow_host = driver.find_element(By.CSS_SELECTOR, ".remoteComponent")
    shadow_root = shadow_host.shadow_root
    el = shadow_root.find_element(By.CSS_SELECTOR, '#input-135')
    print(el)
    assert False