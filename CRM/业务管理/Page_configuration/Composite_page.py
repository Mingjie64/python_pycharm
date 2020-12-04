# coding:utf-8
import unittest
from selenium import webdriver
import time


class page(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://admin-dev.dm-cube.com/#/user/login?redirect=%2F")
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
        print('登陆成功')
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        print('退出浏览器')

    def setUp(self) -> None:
        print("setUp")

    def tearDown(self) -> None:
        print("tearDown")

    # test_1至test_x为单页面测试用例


    def test_1(self):

        # 新增
        self.driver.find_element_by_xpath("//span[text() = '业务管理']/ancestor::li").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[text() = '页面模板管理']/parent::a/parent::li").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//span[text() = '新增']/ancestor::button").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[text() = '确 定']/ancestor::button").click()
        time.sleep(1)
        self.assertEqual(self.driver.find_element_by_xpath("//div[text() = '请输入页面名称!']").text , "请输入页面名称!")
        self.assertEqual(self.driver.find_element_by_xpath("//div[text() = '请输入渠道说明!']").text , "请输入渠道说明!")
        self.assertEqual(self.driver.find_element_by_xpath("//div[text() = '请输入备注!']").text , "请输入备注!")
        self.assertEqual(self.driver.find_element_by_xpath("//div[text() = '请选择渲染模板类型']").text , "请选择渲染模板类型")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@placeholder = '请输入页面名称']").send_keys("web自动化单页面名称")
        self.driver.find_element_by_xpath("//input[@placeholder = '请输入渠道说明']").send_keys("web自动化单页面渠道")
        self.driver.find_element_by_xpath("//input[@placeholder = '请输入备注说明']").send_keys("web自动化单页面备注")
        self.driver.find_element_by_xpath("//input[@type = 'radio' and @value = '1']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//span[text() = '确 定']/parent::button").click()
        time.sleep(3)
        self.assertEqual(self.driver.find_element_by_xpath("//tbody/tr/td").text , "web自动化单页面名称")
        self.assertEqual(self.driver.find_element_by_xpath("//tbody/tr/td[2]").text, "web自动化单页面渠道")
        self.assertEqual(self.driver.find_element_by_xpath("//tbody/tr/td[3]").text, "web自动化单页面备注")
        self.assertEqual(self.driver.find_element_by_xpath("//tbody/tr/td[7]").text, "首页")

    def test_2(self):

        # 编辑-修改必填属性
        self.driver.find_element_by_xpath("//span[text() = '编 辑']/parent::button").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder = '请输入页面名称']").send_keys("编辑")
        self.driver.find_element_by_xpath("//input[@placeholder = '请输入渠道说明']").send_keys("编辑")
        self.driver.find_element_by_xpath("//input[@placeholder = '请输入备注说明']").send_keys("编辑")
        self.driver.find_element_by_xpath("//input[@type = 'radio' and @value = '2']").click()
        self.driver.find_element_by_xpath("//span[text() = '确 定']/parent::button").click()
        time.sleep(3)
        self.assertEqual(self.driver.find_element_by_xpath("//tbody/tr/td").text , "web自动化单页面名称编辑")
        self.assertEqual(self.driver.find_element_by_xpath("//tbody/tr/td[2]").text, "web自动化单页面渠道编辑")
        self.assertEqual(self.driver.find_element_by_xpath("//tbody/tr/td[3]").text, "web自动化单页面备注编辑")
        self.assertEqual(self.driver.find_element_by_xpath("//tbody/tr/td[7]").text, "首页")
        time.sleep(1)

        # 编辑-选填属性填写
        self.driver.find_element_by_xpath("//span[text() = '编 辑']/parent::button").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//label[@title = '弹窗名称']/ancestor::div[@class = 'ant-row ant-form-item']//div[text() = '请选择']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//li[text() = '饿了么基础产品弹窗模板']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//label[@title = '浮窗名称']/ancestor::div[@class = 'ant-row ant-form-item']//div[text() = '请选择']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//li[text() = '饿了么基础产品悬浮窗模板']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//label[@title = '跑马灯名称']/ancestor::div[@class = 'ant-row ant-form-item']//div[text() = '请选择']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//li[text() = '饿了么基础产品跑马灯模板']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[text() = '确 定']/parent::button").click()
        time.sleep(3)
        self.assertEqual(self.driver.find_element_by_xpath("//tbody/tr/td[1]").text, "web自动化单页面名称编辑")
        self.assertEqual(self.driver.find_element_by_xpath("//tbody/tr/td[2]").text, "web自动化单页面渠道编辑")
        self.assertEqual(self.driver.find_element_by_xpath("//tbody/tr/td[3]").text, "web自动化单页面备注编辑")
        self.assertEqual(self.driver.find_element_by_xpath("//tbody/tr/td[4]").text, "饿了么基础产品弹窗模板")
        self.assertEqual(self.driver.find_element_by_xpath("//tbody/tr/td[5]").text, "饿了么基础产品悬浮窗模板")
        self.assertEqual(self.driver.find_element_by_xpath("//tbody/tr/td[6]").text, "饿了么基础产品跑马灯模板")
        self.assertEqual(self.driver.find_element_by_xpath("//tbody/tr/td[7]").text, "首页")

    def test_3(self):

        # 复制另存
        self.driver.find_element_by_xpath("//tbody/tr/td[text() = 'web自动化单页面名称编辑']")
        self.driver.find_element_by_xpath("//span[text() = '复制另存']/parent::button").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder = '请输入页面名称']/parent::div/input").send_keys("1")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@placeholder = '请输入页面名称']/parent::div/following-sibling::div//button[2]").click()
        time.sleep(2)
        self.assertEqual(self.driver.find_element_by_xpath("//div[text() = '页面模型配置为空，无需复制！']").text,"页面模型配置为空，无需复制！")
        time.sleep(1)

        # 新增-配置页面产品
        self.driver.find_element_by_xpath("//span[text() = '配置页面']/parent::button").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//span[contains(text() , '新增Banner')]/parent::button").click()
        time.sleep(2)
        self.driver.find_element_by_xpath\
            ("//span[contains(text() , '新增Banner')]//ancestor::div[@class = 'ant-drawer ant-drawer-right ant-drawer-open']/parent::div/following-sibling::div//span[text() = '确 定']/parent::button").click()
        time.sleep(3)
        self.assertEqual(self.driver.find_element_by_xpath("//div[text() = '请选择配置类型!']").text,'请选择配置类型!')
        self.assertEqual(self.driver.find_element_by_xpath("//div[text() = '请选择产品级别!']").text,'请选择产品级别!')
        self.assertEqual(self.driver.find_element_by_xpath("//div[@class = 'ant-form-explain' and text() = '请选择产品类型']").text,'请选择产品类型')
        self.assertEqual(self.driver.find_element_by_xpath("//div[@class = 'ant-form-explain' and text() = '请输入页面模型配置名称!']").text,'请输入页面模型配置名称!')
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[text() = '请选择配置类型!']/parent::div//div[contains(text() , '请选择')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//ul/li[text() = 'banner']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[text() = '请选择产品级别!']/parent::div//div[@class = 'ant-select-selection__rendered']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//ul/li[text() = '基础产品']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//label[@title = '产品类型']/parent::div/following-sibling::div//div[@class = 'ant-select-selection__rendered']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//ul/li[text() = '信用卡']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//label[@title = '产品名称']/parent::div/following-sibling::div//div[@class = 'ant-select-selection__rendered']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//ul/li[contains(text() , '工商银行')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@placeholder = '请输入名称']").clear()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@placeholder = '请输入名称']").send_keys("自动化banner")
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class = 'ant-modal-title' and text() = '新增']/ancestor::div//span[text() = '确 定']/parent::button").click()
        time.sleep(5)
        for i in range(1, 13):
            if i == 6 or 7:
                i = 8
            elif i == 9:
                break
            LIST1 = ['banner','自动化banner','工商银行','基础产品','信用卡']
            self.assertIn(self.driver.find_element_by_xpath("//tbody/tr/td[text() = 'banner']/parent::tr/td[{}]".format(i)).text,LIST1)
        time.sleep(2)
        self.driver.find_element_by_xpath("//button/i[@class = 'anticon anticon-close']").click()
        time.sleep(2)

        # 复制另存
        self.driver.find_element_by_xpath("//tbody/tr/td[text() = 'web自动化单页面名称编辑']")
        self.driver.find_element_by_xpath("//span[text() = '复制另存']/parent::button").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder = '请输入页面名称']/parent::div/input").send_keys("1")
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "//input[@placeholder = '请输入页面名称']/parent::div/following-sibling::div//button[2]").click()
        time.sleep(2)
        LIST2 = []
        for i in range(1,8):

            LIST2.append(self.driver.find_element_by_xpath("//tbody/tr/td[{}]".format(i)).text)

        LIST3 = ['编辑复件1','渠道编辑','备注编辑','弹窗模板','浮窗模板','跑马灯模板','首页']
        for list in range(0,len(LIST3)):
            self.assertIn(LIST3[list],LIST2[list])


if __name__ == '__main__':
    unittest.main()
