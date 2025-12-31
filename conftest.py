import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from curl import Url



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Url.main_site)
    yield driver
    driver.quit()