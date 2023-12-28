
from pages.HomePage import HomePage
from tests import APICaptchaSolve
from tests.BaseTest import BaseTest
from tests.ReadConfigurations import get_county_list, read_configuration


class TestProbatePetitionPDFDownload(BaseTest):

    BASIC_INFO = "basic info"
    FROM_DATE = "fromdate"
    TO_DATE = "todate"

    def test_download_probate_petitions_pdfs(self):
        home_page = HomePage(self.driver)
        home_page.click_on_search_button()
        google_key = home_page.get_google_key_from_iframe_src()
        print("------- get google key------", google_key)
        token = APICaptchaSolve.get_final_response_OK(google_key)
        home_page.delete_style()
        home_page.set_response(token)
        county_list = get_county_list(self.BASIC_INFO)
        home_page.click_file_search_button()
        for county in county_list:
            print(county)
            home_page.select_country_from_drop_down(county)
            home_page.select_file_proceeding_from_drop_down()
            home_page.enter_from_date(read_configuration(self.BASIC_INFO, self.FROM_DATE))
            home_page.enter_to_date(read_configuration(self.BASIC_INFO, self.TO_DATE))
            home_page.click_file_proceeding_search_button()
            home_page.download_probate_petition_file()
            home_page.click_file_search_top_menu()







