import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.MainPage import MainPage


@pytest.fixture()
def chromedriver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.close()


@pytest.fixture()
def main_page(chromedriver):
    return MainPage(chromedriver)
