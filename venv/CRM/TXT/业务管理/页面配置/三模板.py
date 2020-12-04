# coding:utf-8
import unittest
from selenium import webdriver
import time
from ddt import ddt,data,unpack,file_data
from selenium.common.exceptions import NoSuchElementException
import re


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

    # test_1:（普通页面模板）新增表格、编辑表格、删除表格、字符串格式
    def test_1(self):
        time.sleep(5)
        self.driver.find_element_by_xpath("//section/aside//span[text()='业务管理']/ancestor::div[@class='ant-menu-submenu-title']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//a[@href="#/employee/page"]/parent::li').click()
        time.sleep(2)

        # 普通页面模板
        gong = self.driver.find_element_by_xpath('//li[@class="ant-pagination-total-text"][contains(text(),"共")]').text
        print(gong)
        rr = re.search('[0-9]+(?=条)',gong)
        print("正则：",rr.group())
        time.sleep(1)

        # 新增
        self.driver.find_element_by_xpath("//div[2]/button[@class='ant-btn ant-btn-primary']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="modelName"]').send_keys('123!@#$%^&*()_+|-=、】【；‘、。，{}|“：？》《·~/*-+.中文')
        self.driver.find_element_by_xpath('//*[@id="sourceDesc"]').send_keys('123!@#$%^&*()_+|-=、】【；‘、。，{}|“：？》《·~/*-+.中文')
        self.driver.find_element_by_xpath('//*[@id="modelDesc"]').send_keys('123!@#$%^&*()_+|-=、】【；‘、。，{}|“：？》《·~/*-+.中文')
        time.sleep(2)
        # 确定
        self.driver.find_element_by_xpath('//div[@class="ant-modal-footer"]/div/button[contains(@class,"ant-btn-primary")]').click()
        time.sleep(2)
        a = self.driver.find_element_by_xpath('//span[text()="提交成功"]')
        self.assertEqual(a.text,"提交成功")

        # gongb = self.driver.find_elements_by_xpath('//li[@class="ant-pagination-total-text"][contains(text(),"共")]').text
        # print(gongb)
        # rb = re.search("[0-9]+(?=条)",gongb)
        # print(str(rb))
        # # self.assertNotEqual(r,rb)
        # print(str(r)+str(rb))

        # time.sleep(1)
        # aa = self.driver.find_element_by_xpath('//li[@class="ant-pagination-total-text"][contains(text(),"共")]')
        # bb = str(aa.split(' '))
        # cc = bb[1]
        # dd = cc.sprit('共条')
        # print(d,dd)
        # assert(int(d+1),int(dd))
        time.sleep(1)
        print('test_1:新增模板"提交成功"')

        # “编辑”测试
        # 只会选择第一条的“编辑”按钮，有待改善
        # 修改列表第一项并点击确定
        self.driver.find_element_by_xpath("//span/button[@class='linkBtn ant-btn ant-btn-primary']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='modelName']").clear()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='modelName']").send_keys("123!@#$%^&*()_+|-=、】【；‘、。，{}|“：？》《·~/*-+.中文1")
        time.sleep(1)
        # 点击“确定”按钮
        self.driver.find_element_by_xpath("//div[@class='ant-modal-footer']/div/button[2]").click()
        time.sleep(1)
        # 只是判定文案是否是“提交成功”，存在一定的漏洞，有待改进
        self.assertEqual(self.driver.find_element_by_xpath("//div[@class='ant-message-notice-content']/div/span[text()='提交成功']").text,"提交成功")
        time.sleep(2)

        # ----------

        # 修改列表第二项并点击确定
        self.driver.find_element_by_xpath("//span/button[@class='linkBtn ant-btn ant-btn-primary']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="sourceDesc"]').clear()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="sourceDesc"]').send_keys("123!@#$%^&*()_+|-=、】【；‘、。，{}|“：？》《·~/*-+.中文2")
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='ant-modal-footer']/div/button[2]").click()
        time.sleep(1)
        # 只是判定文案是否是“提交成功”，存在一定的漏洞，有待改进
        assert self.driver.find_element_by_xpath("//div[@class='ant-message-notice-content']/div/span[text()='提交成功']").text =="提交成功"
        time.sleep(2)

        # ----------

        # 修改列表第三项并点击确定
        self.driver.find_element_by_xpath("//span/button[@class='linkBtn ant-btn ant-btn-primary']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="modelDesc"]').clear()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="modelDesc"]').send_keys("123!@#$%^&*()_+|-=、】【；‘、。，{}|“：？》《·~/*-+.中文3")
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='ant-modal-footer']/div/button[2]").click()
        time.sleep(1)
        # 只是判定文案是否是“提交成功”，存在一定的漏洞，有待改进
        self.assertEqual(self.driver.find_element_by_xpath("//div[@class='ant-message-notice-content']/div/span[text()='提交成功']").text,"提交成功")
        time.sleep(2)

        t = self.driver.find_element_by_xpath("//tr[@class='ant-table-row ant-table-row-level-0']/td[1]").text
        print(t)

        self.assertEqual(
            self.driver.find_element_by_xpath("//tr[@class='ant-table-row ant-table-row-level-0']/td[1]").text,
            "123!@#$%^&*()_+|-=、】【；‘、。，{}|“：？》《·~/*-+.中文1")
        self.assertEqual(
            self.driver.find_element_by_xpath("//tr[@class='ant-table-row ant-table-row-level-0']/td[2]").text,
            "123!@#$%^&*()_+|-=、】【；‘、。，{}|“：？》《·~/*-+.中文2")
        self.assertEqual(
            self.driver.find_element_by_xpath("//tr[@class='ant-table-row ant-table-row-level-0']/td[3]").text,
            "123!@#$%^&*()_+|-=、】【；‘、。，{}|“：？》《·~/*-+.中文3")

        # 删除
        self.driver.find_element_by_xpath('//tbody/tr/td[4]/span/a').click()
        time.sleep(1)
        # 确定
        self.driver.find_element_by_xpath('//div[@class="ant-modal-confirm-btns"]/button[2]').click()
        time.sleep(1)
        # self.driver.find_element_by_xpath('//div[contains(@class,"ant-message-info")]').click()
        # time.sleep(1)
        self.assertEqual(self.driver.find_element_by_xpath('//span[text()="删除成功"]').text,"删除成功")
        time.sleep(2)

    # test_2:（弹窗模板）新增表格、编辑表格、删除表格、字符串格式
    def test_2(self):
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class=' ant-tabs-tab'][text()='弹窗模板配置']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='ant-tabs-tabpane ant-tabs-tabpane-active']//button/span[text()='新增']/parent::button").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='productUrl']").send_keys("http://www.baidu.com")
        self.driver.find_element_by_xpath("//input[@id='modelName' and @placeholder='请输入名称']").send_keys("弹窗名称自动化")
        self.driver.find_element_by_xpath("//input[@id='modelDesc' and @placeholder='请输入文案备注']").send_keys("弹窗文案自动化")
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='ant-message']//following-sibling::div//button[@class='ant-btn ant-btn-primary']").click()
        time.sleep(1)
        self.assertEqual(self.driver.find_element_by_xpath("//div[@class='ant-message-notice']//span[text()='提交成功']").text,"提交成功")
        time.sleep(1)
        self.assertEqual(self.driver.find_element_by_xpath("//th[@key='imageUrl']//ancestor::table//td").text,"弹窗名称自动化")
        self.assertEqual(self.driver.find_element_by_xpath("//th[@key='imageUrl']//ancestor::table//td[2]").text,"")
        self.assertEqual(self.driver.find_element_by_xpath("//th[@key='imageUrl']//ancestor::table//td[3]").text,"http://www.baidu.com")
        self.assertEqual(self.driver.find_element_by_xpath("//th[@key='imageUrl']//ancestor::table//td[4]").text,"弹窗文案自动化")
        # 编辑
        self.driver.find_element_by_xpath("//th[@key='imageUrl']//ancestor::table//button").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='productUrl']").clear()
        self.driver.find_element_by_xpath("//input[@id='productUrl']").send_keys("http://www.taobao.com")
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='ant-message']//following-sibling::div//button[@class='ant-btn ant-btn-primary']").click()
        time.sleep(1)
        self.assertEqual(self.driver.find_element_by_xpath("//div[@class='ant-message-notice']//span[text()='提交成功']").text,"提交成功")
        time.sleep(1)
        self.assertEqual(self.driver.find_element_by_xpath("//th[@key='imageUrl']//ancestor::table//td[3]").text,"http://www.taobao.com")
        time.sleep(1)

        self.driver.find_element_by_xpath("//th[@key='imageUrl']//ancestor::table//button").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='modelName' and @placeholder='请输入名称']").clear()
        self.driver.find_element_by_xpath("//input[@id='modelName' and @placeholder='请输入名称']").send_keys("弹窗名称自动化r")
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='ant-message']//following-sibling::div//button[@class='ant-btn ant-btn-primary']").click()
        time.sleep(1)
        self.assertEqual(
            self.driver.find_element_by_xpath("//div[@class='ant-message-notice']//span[text()='提交成功']").text, "提交成功")
        self.assertEqual(
            self.driver.find_element_by_xpath("//th[@key='imageUrl']//ancestor::table//td[3]").text,"弹窗名称自动化r")
        time.sleep(1)

        self.driver.find_element_by_xpath("//th[@key='imageUrl']//ancestor::table//button").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='modelDesc' and @placeholder='请输入文案备注']").clear()
        self.driver.find_element_by_xpath("//input[@id='modelDesc' and @placeholder='请输入文案备注']").send_keys("弹窗文案自动化r")
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='ant-message']//following-sibling::div//button[@class='ant-btn ant-btn-primary']").click()
        time.sleep(1)
        self.assertEqual(
            self.driver.find_element_by_xpath("//div[@class='ant-message-notice']//span[text()='提交成功']").text, "提交成功")
        self.assertEqual(
            self.driver.find_element_by_xpath("//th[@key='imageUrl']//ancestor::table//td[4]").text, "弹窗文案自动化r")
        time.sleep(5000)

    # test_3:（悬浮窗模板）新增表格、编辑表格、删除表格、字符串格式
    def test_3(self):
        self.driver.find_element_by_xpath("//div[@class=' ant-tabs-tab'][text()='悬浮窗模板配置']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='ant-tabs-tabpane ant-tabs-tabpane-active']//button/span[text()='新增']/parent::button").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='ant-message']/following-sibling::div[2]//input[@placeholder='请输入自定义链接']").send_keys("http://www.baidu.com")
        self.driver.find_element_by_xpath("//div[@class='ant-message']/following-sibling::div[2]//input[@placeholder='请输入名称']").send_keys("悬浮窗名称自动化")
        self.driver.find_element_by_xpath("//div[@class='ant-message']/following-sibling::div[2]//input[@placeholder='请输入文案备注']").send_keys("悬浮窗文案自动化")
        time.sleep(1)
        # 点击确定
        self.driver.find_element_by_xpath("//div[@class='ant-message']/following-sibling::div[2]//button[@class='ant-btn ant-btn-primary']").click()
        time.sleep(1)




    # test_4:复制另存
    def test_4(self):
        # 新增
        time.sleep(5000)
        self.driver.find_element_by_xpath("//div[2]/button[@class='ant-btn ant-btn-primary']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="modelName"]').send_keys('复制另存测试')
        # time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="sourceDesc"]').send_keys('复制另存测试')
        # time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="modelDesc"]').send_keys('复制另存测试')
        time.sleep(1)
        # 确定
        self.driver.find_element_by_xpath('//div[@class="ant-modal-footer"]/div/button[contains(@class,"ant-btn-primary")]').click()
        time.sleep(2)

        a = self.driver.find_element_by_xpath('//span[text()="提交成功"]')
        self.assertEqual(a.text,"提交成功")
        time.sleep(1)

        # 点击“复制另存按钮”
        self.driver.find_element_by_xpath("//td[@class='ant-table-row-cell-break-word']/span/button[3]").click()
        time.sleep(2)

        # 点击“确定”
        self.driver.find_element_by_xpath("//div[@class='ant-message']/following-sibling::div//button[@class='ant-btn ant-btn-primary']").click()
        time.sleep(2)

        # 再次点击“复制另存模板”
        self.driver.find_element_by_xpath("//td[@class='ant-table-row-cell-break-word']/span/button[3]").click()
        time.sleep(2)
        # 点击“取消”关闭页面
        self.driver.find_element_by_xpath("//div[@class='ant-message']/following-sibling::div//button[@class='ant-btn']").click()
        time.sleep(1)
        assert self.driver.find_element_by_xpath("//tr[@class='ant-table-row ant-table-row-level-0']/td[1]").text == "复制另存测试"
        # assert self.driver.find_element_by_xpath(
        #     "//tr[@class='ant-table-row ant-table-row-level-0']/td[1]").text == self.driver.find_element_by_xpath(
        #     "//tr[2][@class='ant-table-row ant-table-row-level-0']/td[1]").text
        time.sleep(1)

        # # 点击“复制另存按钮”
        # self.driver.find_element_by_xpath("//td[@class='ant-table-row-cell-break-word']/span/button[3]").click()
        # time.sleep(3)
        # # 点击“x”关闭页面
        # self.driver.find_element_by_xpath('//button[@class="ant-modal-close"]/span/i').click()
        # time.sleep(3)
        # assert self.driver.find_element_by_xpath("//tr[@class='ant-table-row ant-table-row-level-0']/td[1]").text == "复制另存测试"
        # assert self.driver.find_element_by_xpath(
        #     "//tr[@class='ant-table-row ant-table-row-level-0']/td[1]").text == self.driver.find_element_by_xpath(
        #     "//tr[2][@class='ant-table-row ant-table-row-level-0']/td[1]").text
        # time.sleep(1)

        # 如果第一行的页面名称含有“复制另存测试”的字符串则删除该模板
        if self.driver.find_element_by_xpath("//tr[@class='ant-table-row ant-table-row-level-0']/td[1]").text in '复制另存测试':
            time.sleep(1)
            self.driver.find_element_by_xpath("//td[@class='ant-table-row-cell-break-word']/span/a").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//div[@class='ant-modal-confirm-body-wrapper']/div[@class='ant-modal-confirm-btns']/button[2]").click()
            time.sleep(1)
        # 如果第二行的页面名称含有“复制另存测试”的字符串则删除该模板
        if self.driver.find_element_by_xpath("//tr[2][@class='ant-table-row ant-table-row-level-0']/td[1]").text in '复制另存测试':
            time.sleep(1)
            self.driver.find_element_by_xpath("//td[@class='ant-table-row-cell-break-word']/span/a").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "//div[@class='ant-modal-confirm-body-wrapper']/div[@class='ant-modal-confirm-btns']/button[2]").click()
            time.sleep(1)



if __name__ == '__main__':
    unittest.main()
