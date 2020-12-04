from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class NoSuchElement(object):
    def __init__(self,driver):
        self.driver = driver

    def elexpath(self,xpath,file_name):

        try:
            self.driver.find_elements_by_xpath(xpath)
        except NoSuchElementException:
            # "no_such_element.png"
            self.file_name = file_name
            self.driver.save_screenshot(self.file_name)
            self.driver.get_screenshot_as_file(self.file_name)
            raise
