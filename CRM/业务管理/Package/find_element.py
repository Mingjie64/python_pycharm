
class driverClass(object):
    def __init__(self, driver):
        self.driver = driver


    def id(self, find_element_by_id1):

        id = self.driver.find_element_by_id(find_element_by_id1)
        return id

    def xpath(self, find_element_by_xpath1):

        xpath = self.driver.find_element_by_xpath(find_element_by_xpath1)
        return xpath

    def xpaths(self, find_elements_by_xpath1):

        xpaths = self.driver.find_elements_by_xpath(find_elements_by_xpath1)
        return xpaths