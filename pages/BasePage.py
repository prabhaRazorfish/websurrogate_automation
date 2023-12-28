import time
import urllib.request
from urllib.parse import urlparse
from urllib.parse import parse_qs

import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def type_into_element(self,text,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def element_click(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()

    def check_display_status_of_element(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        return element.is_displayed()

    def retrieve_element_text(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        return element.text

    def get_element(self,locator_name,locator_value):
        element = None
        if locator_name.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_name.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_name.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_name.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element

    def get_elements(self,locator_name,locator_value):
        element = None
        if locator_name.endswith("_id"):
            element = self.driver.find_elements(By.ID, locator_value)
        elif locator_name.endswith("_name"):
            element = self.driver.find_elements(By.NAME, locator_value)
        elif locator_name.endswith("_class_name"):
            element = self.driver.find_elements(By.CLASS_NAME, locator_value)
        elif locator_name.endswith("_link_text"):
            element = self.driver.find_elements(By.LINK_TEXT, locator_value)
        elif locator_name.endswith("_xpath"):
            element = self.driver.find_elements(By.XPATH, locator_value)
        elif locator_name.endswith("_css"):
            element = self.driver.find_elements(By.CSS_SELECTOR, locator_value)
        return element

    def wait_for_element_visible(self, element):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, element)))

    def move_to_frame(self):
        self.driver.switch_to.frame(self.driver.find_elements(By.TAG_NAME, "iframe")[0])

    def move_out_of_iframe(self):
        self.driver.switch_to.default_content()

    def select_by_value(self, element, value):
        selectOption = Select(self.driver.find_element(By.XPATH, element))
        selectOption.select_by_visible_text(value)

    def click_element(self, element):
        time.sleep(2)
        element.click()

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def switch_to_parent_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def close_new_tab(self):
        self.driver.close()

    def get_current_url(self):
        return self.driver.current_url


    def download_pdf_file(self, url, file_name):
        urllib.request.urlretrieve(url, f"pdfs/{file_name}.pdf")

    def get_url_param_value(self, src_url, key):
        print(src_url)
        parsed_url = urlparse(src_url)
        key_value = parse_qs(parsed_url.query)[key][0]
        print(key_value)
        return key_value