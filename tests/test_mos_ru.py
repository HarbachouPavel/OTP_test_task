from dataclasses import dataclass
import allure


@dataclass
class Data:
    URL = 'https://www.mos.ru/'
    HEADER_LOCATOR = '//div[@id="mos-header"]'
    FOOTER_LOCATOR = '//div[@id="mos_footer"]'


class TestMosRu:
    def test_header_and_footer_are_exist(self, main_page):
        main_page.open_page(Data.URL)
        with allure.step('checking header and footer are exist'):
            assert main_page.check_exists_element_on_page(Data.HEADER_LOCATOR) and\
                   main_page.check_exists_element_on_page(Data.FOOTER_LOCATOR), \
                   "Header or Footer doesn't exist on the page"

    def test_check_all_urls_on_response_status_ok(self, main_page):
        main_page.open_page(Data.URL)
        with allure.step('checking urls for response code == 200'):
            main_page.check_urls_on_response_status_ok()

    def test_check_all_urls_on_right_browser_url(self, main_page):
        main_page.open_page(Data.URL)
        with allure.step('checking of all urls for right browser url'):
            main_page.check_match_elements_url_with_url_in_browser_address_bar()
