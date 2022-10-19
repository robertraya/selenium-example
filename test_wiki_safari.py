import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep
import sys


@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass

class Test_URL_Safari(BasicTest):

    def test_lambdatest_todo_app(self):
        self.driver.get('https://en.wikipedia.org/wiki/Main_Page')
        time.sleep(3)
        self.driver.maximize_window()
        title = "Wikipedia, the free encyclopedia"
        assert title ==  self.driver.title
        time.sleep(3)
        search_term = "Python (programming language)"
        search_field =  self.driver.find_element(By.ID, "searchInput")
        search_field.send_keys(search_term)
        self.driver.find_element(By.ID, "searchButton").click()
        time.sleep(5)
        expected_url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
        assert expected_url == self.driver.current_url 
        time.sleep(2)