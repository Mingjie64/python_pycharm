# coding:utf-8
import unittest
from CRM.业务管理.Page_configuration.Three_template import forTest
import HTMLTestRunner
import HTMLReport



if __name__ == "__main__":


    # runner = unittest.TestSuite()
    # with open("HTMLTestRunner_Three_template.html","wb+") as f:
    #     runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="MJ的自动化测试报告O(∩_∩)O",description="三模板增删改查测试报告详情~",verbosity=2)
    #     runner.run(suite)
    #     f.close()

    suite = unittest.TestSuite()
    suite.addTest(forTest("test_1"))
    suite.addTest(forTest("test_2"))
    suite.addTest(forTest("test_3"))
    suite.addTest(forTest("test_4"))

    runner = HTMLReport.TestRunner(report_file_name="HTMLReport_Three_template.html",title="MJ的自动化测试报告O(∩_∩)O",description="三模板增删改查测试报告详情~")
    runner.run(suite)