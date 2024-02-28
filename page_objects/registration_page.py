from pageo import BasePage
from tests.common.urls import URLs

class RegistrationPage(BasePage):
    base_url = URLs.BASE_URL
    url_suffix = URLs.REGISTRATION_SUFFIX
