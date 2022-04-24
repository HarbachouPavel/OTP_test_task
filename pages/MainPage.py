from http import HTTPStatus
from typing import List
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url: str):
        self.driver.get(url)

    def get_all_urls_from_page(self) -> List[str]:
        """
        Get all urls from page
        :return: list of urls
        """
        all_urls_from_page_locator = "//a[contains(@href,'http')]"
        all_urls = []
        all_elements = WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located
                                                            ((By.XPATH, all_urls_from_page_locator)))
        for url in all_elements:
            all_urls.append(url.get_attribute('href'))
        return all_urls

    def check_exists_element_on_page(self, locator: str) -> bool:
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, locator)))
        return len(self.driver.find_elements(By.XPATH, locator)) > 0

    def check_urls_on_response_status_ok(self):
        """
        Get all urls from page and check it on response status ok
        """
        all_urls = self.get_all_urls_from_page()
        for url in all_urls:
            response = requests.get(url)
            assert response.status_code == HTTPStatus.ok, "One or more urls from page don't have status code 200"

    def check_match_elements_url_with_url_in_browser_address_bar(self):
        """
        Get all urls from page and check it on current url in browser address bar
        """
        all_urls = self.get_all_urls_from_page()
        for url in all_urls:
            self.open_page(url)
            assert url == self.driver.current_url(), "One or more urls from page don't match with browser address bar"
