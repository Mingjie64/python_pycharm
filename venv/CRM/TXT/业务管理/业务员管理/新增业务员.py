# coding:utf-8
import unittest
from selenium import webdriver
import time
from ddt import ddt,data,unpack,file_data
from selenium.common.exceptions import NoSuchElementException
import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from  import *
import random


def readFile():
    params = []
    file = open(r'C:\Users\zengjiangshan\.PyCharmCE2019.2\config\scratches\CRM\TXT\login.csv', "r", encoding="utf-8")
    for line in file.readlines():
        params.append(line.strip('\n').split(','))
    return params

# 测试环境

@ddt
class forTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 登陆
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('http://admin-test.dm-cube.com/#/user/login?redirect=%2F')
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
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        time.sleep(1)
        print('tearDownClass')

    def setUp(self) -> None:

        print('setUp')


    def tearDown(self) -> None:

        print('tearDown')

    def test_1(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(
            "//section/aside//span[text()='业务管理']/ancestor::div[@class='ant-menu-submenu-title']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//span[text()='业务员管理']/parent::a").click()
        time.sleep(1)
        page = self.driver.find_elements_by_xpath("//*[@class='ant-pagination-total-text']")
        page = page[0]
        page = page.text
        page1 = re.search('[0-9]+(?=条)', page).group()
        print("第一次判断数据条数：",page1)
        time.sleep(1)
        self.driver.find_element_by_xpath("//span[text()='新增']/parent::button").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[text()='请选择']/parent::div").click()
        time.sleep(1)
        # 经理
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        # # 业务员
        # ActionChains(self.driver).send_keys(Keys.DOWN,Keys.ENTER).perform()
        time.sleep(1)
        # name = input("姓名:")
        # phone = input("手机:")
        # id_card = input("身份证:")
        # if len(phone) != 11:
        #     phone = input("请输入十一位手机号码:")
        # if len(id_card) != 18:
        #     id_card = input("请输入十八位身份证号码:")
        # time.sleep(3)

        person = {"phone3": "", "name3": "", "id_card3": ""}
        person["phone3"]=phone3()
        person["name3"]=name3()
        person["id_card3"]=id_card3()
        self.driver.find_element_by_xpath("//input[@id='name']").send_keys(person["name3"])
        zhiwei = self.driver.find_element_by_xpath("//div[@title='经理']").text

        if zhiwei == "业务员":
            self.driver.find_element_by_xpath("//button[@class='ant-btn ant-input-search-button']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//span[@class='ant-input-search ant-input-affix-wrapper']/input").send_keys("下划线一")
            time.sleep(1)
            self.driver.find_element_by_xpath("//span[@class='ant-input-search ant-input-affix-wrapper']/span/i").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//label[@class='ant-radio-wrapper']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "//span[@class='ant-input-search ant-input-affix-wrapper']/ancestor::div[@class='ant-modal-body']/following-sibling::div//button[@class='ant-btn ant-btn-primary']").click()


        self.driver.find_element_by_xpath("//input[@placeholder='请输入电话号码']").send_keys(person["phone3"])
        self.driver.find_element_by_xpath("//input[@placeholder='请输入身份证号码']").send_keys(person["id_card3"])
        self.driver.find_element_by_xpath("//div[@title='在职']/parent::div[@class='ant-select-selection__rendered']").click()
        time.sleep(1)
        # 在职状态
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        # 离职状态
        # ActionChains(self.driver).send_keys(Keys.DOWN,Keys.ENTER).perform()
        time.sleep(1)
        if zhiwei == "经理":
            self.driver.find_element_by_xpath("//input[@placeholder='请选择区域']/parent::span/i").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//li[@title='华南地区']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//li[text()='广州']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//li[text()='广州一公司']").click()
            time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='ant-modal-footer']//button[@class='ant-btn ant-btn-primary']").click()
        time.sleep(1)
        ass = self.driver.find_element_by_xpath("//div[@class='ant-message']//span[contains(text(),'操作成功')]")
        self.assertIn("操作成功",ass.text)
        aaa =self.driver.find_element_by_xpath("//tr[@class='ant-table-row ant-table-row-level-0']/td[2]")
        self.assertEqual(self.driver.find_element_by_xpath("//tr[@class='ant-table-row ant-table-row-level-0']/td[2]").text,person["phone3"])
        time.sleep(1)
        self.assertEqual(self.driver.find_element_by_xpath("//tr[@class='ant-table-row ant-table-row-level-0']/td[3]").text,person["name3"])
        time.sleep(1)
        self.assertEqual(self.driver.find_element_by_xpath("//tr[@class='ant-table-row ant-table-row-level-0']/td[4]").text,person["id_card3"])
        time.sleep(1)

        page = self.driver.find_elements_by_xpath("//*[@class='ant-pagination-total-text']")
        page = page[0]
        page = page.text
        page2 = re.search('[0-9]+(?=条)', page).group()
        print("第二次判断数据条数：",page2)
        self.assertTrue(int(page2) - int(page1) == 1)


if __name__ == '__main__':
    unittest.main()