# coding:utf-8
import unittest
from selenium import webdriver
import time
from ddt import ddt,data,unpack,file_data
import re
from selenium.common.exceptions import NoSuchElementException
from CRM.业务管理.Package.find_element import *
from CRM.业务管理.Package.NoSuchElement import NoSuchElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@ddt
class product(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
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
        cls.driver.find_element_by_xpath(
            '//*[@id="form"]/div[3]/div/div/span/button').click()
        time.sleep(3)
        print('登陆')
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        time.sleep(1)
        print('退出浏览器')
        print('tearDownClass')

    def setUp(self) -> None:
        print('setUp')

    def tearDown(self) -> None:
        print('tearDown')

    def test_1(self):
        # text_1是流量产品的增改查
        # (1)新增
        time.sleep(2)
        self.driver.find_element_by_xpath(
            "//section/aside//span[text()='业务管理']/ancestor::div[@class='ant-menu-submenu-title']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//a/span[text() = '产品管理']/parent::a/parent::li").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//label/span[text() = '流量产品管理']/parent::label").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button/span[text() = '新增']/parent::button").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@placeholder = '请输入流量产品名称']").send_keys("web自动化流量产品名称")
        self.driver.find_element_by_xpath("//label[@title = '所属基础产品']/parent::div//following-sibling::div//div[@class = 'ant-select-selection__rendered']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//li[contains(text(),'电话卡')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class = 'ant-btn ant-btn-primary']/span[text() = '确 定']/parent::button").click()
        time.sleep(1)
        self.assertEqual(self.driver.find_element_by_xpath("//span[text() = '下架']/ancestor::tr/preceding-sibling::tr[1]//button/span").text,"上架")
        time.sleep(1)
        if self.assertEqual(self.driver.find_element_by_xpath("//span[text() = '下架']/ancestor::tr/td[2]").text,"web自动化流量产品名称"):
            print("新增成功")


        self.driver.find_element_by_xpath("//button/span[text() = '新增']/parent::button").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@placeholder = '请输入流量产品名称']").send_keys("web自动化流量产品名称all")
        self.driver.find_element_by_xpath("//label[@title = '所属基础产品']/parent::div//following-sibling::div//div[@class = 'ant-select-selection__rendered']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//li[contains(text(),'电话卡')]").click()
        self.driver.find_element_by_xpath("//input[@placeholder = '请输入内部备注名称']").send_keys("MJ内部备注")
        self.driver.find_element_by_xpath("//input[@placeholder = '请输入排序']").send_keys("1")
        self.driver.find_element_by_xpath("//input[@placeholder = '请输入重要卖点']").send_keys("123")
        self.driver.find_element_by_xpath("//input[@placeholder = '请输入一般卖点']").send_keys("321")
        self.driver.find_element_by_xpath("//div[text() = '请输入标签']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[text() = '请输入标签']/parent::div//input").send_keys("标签")
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[text() = '请输入标签']/parent::div//input").send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@placeholder = '请输入ICP编号']").send_keys("ICPICP")
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class = 'ant-btn ant-btn-primary']/span[text() = '确 定']/parent::button").click()
        time.sleep(1)
        self.assertEqual(self.driver.find_element_by_xpath("//span[text() = '下架']/ancestor::tr/preceding-sibling::tr[1]//button/span").text,"上架")
        time.sleep(1)
        if self.assertEqual(self.driver.find_element_by_xpath("//span[text() = '下架']/ancestor::tr/td[2]").text,"web自动化流量产品名称all"):
            print("新增成功")

        self.driver.find_element_by_xpath("//div[@class = 'ant-select-selection__placeholder' and text() = '请选择当前状态']/parent::div").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div//ul/li[text() = '下架']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class = 'ant-select-selection__rendered']/div[text() = '请选择基础产品']/parent::div").click()
        time.sleep(10)
        self.driver.find_element_by_xpath("//div/ul/li[contains(text(),'电话卡')]").click()
        time.sleep(1)
        # 查询
        self.driver.find_element_by_xpath("//button/span[text() = '查询']/parent::button").click()
        time.sleep(1)
        self.assertEqual(self.driver.find_element_by_xpath("//tbody/tr/td[2]").text,"web自动化流量产品名称all")
        self.assertEqual(self.driver.find_element_by_xpath("//tbody/tr[2]/td[2]").text,"web自动化流量产品名称")
        time.sleep(1)

        # 修改\查询
        self.driver.find_element_by_xpath("//tbody/tr/td/span/a[text() = '修改']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div/span/input[@placeholder='请输入流量产品名称']").send_keys("\r"+"修改测试")
        self.driver.find_element_by_xpath("//div/label[@title = '所属基础产品']/parent::div/following-sibling::div//div[@class = 'ant-select-selection__rendered']/div[@title = '电话卡']/parent::div").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class = 'ant-modal']/ancestor::div/following-sibling::div//div/ul/li[contains(text(),'移动大王卡')]/ancestor::div/following-sibling::div//li[contains(text(),'移动大王卡')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div/span/input[@placeholder = '请输入内部备注名称']").send_keys("\r"+"修改测试")
        self.driver.find_element_by_xpath("//div/span/input[@placeholder = '请输入排序']").clear()
        self.driver.find_element_by_xpath("//div/span/input[@placeholder = '请输入排序']").send_keys("0")
        self.driver.find_element_by_xpath("//div/span/input[@placeholder = '请输入重要卖点']").send_keys("\r"+"修改测试")
        self.driver.find_element_by_xpath("//div/span/input[@placeholder = '请输入一般卖点']").send_keys("\r"+"修改测试")
        self.driver.find_element_by_xpath("//div/div[text() = '请输入标签']/parent::div").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div/div[text() = '请输入标签']/ancestor::div[@id = 'productTag']//li[@class = 'ant-select-search ant-select-search--inline']//input").send_keys("修改测试")
        self.driver.find_element_by_xpath("//div/div[text() = '请输入标签']/ancestor::div[@id = 'productTag']//li[@class = 'ant-select-search ant-select-search--inline']//input").send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element_by_xpath("//div/span/input[@placeholder = '请输入ICP编号']").send_keys("\r"+"修改测试")
        self.driver.find_element_by_xpath("//div/span/input[@placeholder = '请输入流量产品名称标题']").send_keys("\r"+"修改测试")
        time.sleep(1)
        self.driver.find_element_by_xpath("//div//input[@placeholder = '请输入流量产品名称标题']//ancestor::div//button[2]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath(
            "//div[@class = 'ant-select-selection__rendered']/div[text() = '请选择基础产品']/parent::div").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div/ul/li[contains(text(),'移动大王卡')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button/span[text() = '查询']/parent::button").click()
        time.sleep(3)

        self.assertIn("修改测试",self.driver.find_element_by_xpath("//tbody/tr/td[2]").text)
        self.assertIn("修改测试",self.driver.find_element_by_xpath("//tbody/tr/td[5]").text)
        self.assertIn("修改测试",self.driver.find_element_by_xpath("//tbody/tr/td[6]").text)
        self.assertIn("修改测试",self.driver.find_element_by_xpath("//tbody/tr/td[7]").text)
        self.assertIn("修改测试",self.driver.find_element_by_xpath("//tbody/tr/td[9]").text)
        self.assertIn("0",self.driver.find_element_by_xpath("//tbody/tr/td[10]").text)

        if "修改测试" in self.driver.find_element_by_xpath("//tbody/tr/td[2]").text:
            self.driver.find_element_by_xpath("//tbody/tr/td[11]/span/button/span[text() = '下架']/parent::button").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//div/div[text() = '请选择当前状态']/parent::div").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//div/ul/li[text() = '上架']").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//button/span[text() = '查询']/parent::button").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//tbody/tr/td[text() = 'web自动化流量产品名称all修改测试']/parent::tr/td/span/button").click()
            time.sleep(2)
            # 找到名字带有'修改测试'的元素才会去点击这个按钮，否则报错
            self.driver.find_element_by_xpath("//div[@class = 'ant-spin-nested-loading']/div/div[contains(text(),'修改测试')]/ancestor::div[@class = 'ant-modal-body']/following-sibling::div/div/button[2]").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@class = 'ant-message']//div/span[text() = '提交成功']")





if __name__ == '__main__':
    unittest.main()
