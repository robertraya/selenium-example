import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def driver_init(request):
    web_driver = webdriver.Safari()
    request.cls.driver = web_driver
    yield
    web_driver.close()