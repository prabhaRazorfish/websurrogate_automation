import time

from pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    search_button_css = "#StartSearchButton"
    captcha_xpath = "//span[@aria-checked='false' and @id='recaptcha-anchor']"
    file_search_button_css = "button#FileSearch"
    captch_green_xpath = "//span[@aria-checked='true' and @id='recaptcha-anchor']"
    iframe_xpath = "//iframe[@title='reCAPTCHA']"
    select_country_drop_down = "//select[@id='CourtSelect']"
    select_file_proceeding_drop_down = "//select[@id='SelectedProceeding']"
    date_from_text_filed = "//input[@id='txtFilingDateFrom']"
    date_to_text_filed = "//input[@id='txtFilingDateTo']"
    file_proceeding_search_button_xpath = "//button[@id='FileSearchSubmit2']"
    file_css_selector = "td button.ButtonAsLink"
    file_history_close_xpath = "//button[@id='FileHistoryClose']"
    probate_petition_xpath = "//button[contains(text(),'PROBATE PETITION')]"
    file_xpath_selection = "//tr[1] //button[@class='ButtonAsLink']"
    file_search_top_menu = "//div[@id='TopMenu'] //a[text()='File Search']"

    def click_on_search_button(self):
        self.element_click("search_button_css",self.search_button_css)

    def click_captcha(self):
        self.move_to_frame()
        self.wait_for_element_visible(self.captcha_xpath)
        self.element_click("captcha_xpath",self.captcha_xpath)
        self.wait_for_element_visible(self.captch_green_xpath)
        self.move_out_of_iframe()

    def click_file_search_button(self):
        self.element_click("name_search_button_css",self.file_search_button_css)

    def select_country_from_drop_down(self, county_name):
        self.select_by_value(self.select_country_drop_down,county_name)

    def select_file_proceeding_from_drop_down(self):
        self.select_by_value(self.select_file_proceeding_drop_down, "PROBATE PETITION")

    def enter_from_date(self, from_date):
        self.type_into_element(from_date, "from_date_xpath",self.date_from_text_filed)

    def enter_to_date(self, to_date):
        self.type_into_element(to_date, "to_date_xpath",self.date_to_text_filed)

    def click_file_proceeding_search_button(self):
        self.element_click("file_proceeding_search_button_xpath",self.file_proceeding_search_button_xpath)

    def download_probate_petition_file(self):
        file_elements = self.get_elements("file_css",self.file_css_selector)

        for i in range(1,len(file_elements)+1):
            file_name = self.retrieve_element_text("file_element_xpath", f"//tr[{i}] //button[@class='ButtonAsLink']")
            self.element_click("file_element_xpath", f"//tr[{i}] //button[@class='ButtonAsLink']")
            self.element_click("probate_petition_xpath", self.probate_petition_xpath)
            time.sleep(5)
            self.switch_to_new_window()
            print(self.get_current_url())
            self.download_pdf_file(self.get_current_url(), file_name)
            self.close_new_tab()
            self.switch_to_parent_window()
            self.element_click("file_history_xpath", self.file_history_close_xpath)
            time.sleep(5)
            break

    def get_google_key_from_iframe_src(self):
        #self.move_to_frame()
        src = self.get_element("iframe_xpath", self.iframe_xpath).get_attribute("src")
        self.move_out_of_iframe()
        return self.get_url_param_value(src, "k")

    def set_response(self, token):
        time.sleep(4)
        self.driver.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{token}'")

    def callback_fun(self, token):
        self.driver.execute_script("document.getElementById('AuthenticatePageForm').submit()")

    def delete_style(self):
        ele = self.get_element("get_captcha_response_id","g-recaptcha-response")
        self.driver.execute_script("arguments[0].style.removeProperty('display')", ele)

    def enter_token_in_textarea(self, token):
        self.type_into_element(token, "get_captcha_response_id","g-recaptcha-response")

    def click_file_search_top_menu(self):
        self.element_click("file_token_search_xpath", self.file_search_top_menu)

