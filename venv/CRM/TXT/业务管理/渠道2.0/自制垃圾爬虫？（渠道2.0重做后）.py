# coding:utf-8
import unittest
from selenium import webdriver
import time
from ddt import ddt,data,unpack,file_data
from selenium.common.exceptions import NoSuchElementException
import re


@ddt
class forTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 登陆
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('http://admin-dev.dm-cube.com/#/user/login?redirect=%2F')
        time.sleep(3)
        cls.driver.find_element_by_id('username').send_keys("admin")
        time.sleep(1)
        cls.driver.find_element_by_id('password').send_keys("123456")
        time.sleep(1)
        cls.driver.find_element_by_id('captcha').send_keys("123456")
        time.sleep(1)
        cls.driver.find_element_by_xpath('//*[@id="form"]/div[3]/div/div/span/button').click()
        time.sleep(3)
        print('登陆成功')
        cls.driver.find_element_by_xpath("//span[text()='业务管理']").click()
        time.sleep(3)
        cls.driver.find_element_by_xpath('//a[@href="#/employee/Source2"]').click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        time.sleep(1)
        print('tearDownClass')

    def setUp(self) -> None:

        print('setUp')


    def tearDown(self) -> None:

        print('tearDown')

    # 自制爬虫？（渠道2.0重做）
    # 开发环境
    def test_1(self):
        n=0
        for l in range(1,11):
            for m in range(1,11):
                a=self.driver.find_element_by_xpath("//tr[{}]/td[2]".format(m)).text
                b=self.driver.find_element_by_xpath("//tr[{}]/td[3]".format(m)).text
                c=self.driver.find_element_by_xpath("//tr[{}]/td[4]".format(m)).text
                d=self.driver.find_element_by_xpath("//tr[{}]/td[5]".format(m)).text
                e=self.driver.find_element_by_xpath("//tr[{}]/td[6]".format(m)).text
                f=self.driver.find_element_by_xpath("//tr[{}]/td[7]".format(m)).text
                g=self.driver.find_element_by_xpath("//tr[{}]/td[8]".format(m)).text
                h=self.driver.find_element_by_xpath("//tr[{}]/td[9]".format(m)).text
                i=self.driver.find_element_by_xpath("//tr[{}]/td[10]".format(m)).text
                j=self.driver.find_element_by_xpath("//tr[{}]/td[11]".format(m)).text
                m=m+n
                k=str(m)+','+a+','+b+','+c+','+d+','+e+','+f+','+g+','+h+','+i+','+j
                print(k)
            n=n+10
            time.sleep(1)
            self.driver.find_element_by_xpath("//a[@class='ant-pagination-item-link']/i[@class='anticon anticon-right']").click()
            time.sleep(1)

if __name__ == '__main__':
    unittest.main()