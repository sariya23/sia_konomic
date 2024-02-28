from page_objects.registration_page import RegistrationPage

import time

def test_a(driver):
    page = RegistrationPage()
    time.sleep(2)

    assert False