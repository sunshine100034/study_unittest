#!__author__ = "yf"
"""
pycharm
"""
import unittest
from  HTMLTestRunner_PY3 import HTMLTestRunner

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        print("test_upper")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("test_isupper")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print("test_split")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

print(__name__)


if __name__ == '__main__':
    # 1 全部测试方法
    # unittest.main()

    # 2、 指定测试用例，讲用例放到测试套件中
    # suit = unittest.TestSuite()
    # suit.addTest(TestStringMethods("test_upper"))
    # runner = unittest.TextTestRunner()
    # runner.run(suit)

    # 3. 同时测试多个类
    # suit = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    # unittest.TextTestRunner().run(suit)

    # 4加载目录下的所有用例
    # test = "./"
    # discover = unittest.defaultTestLoader.discover(test)
    # unittest.TextTestRunner(verbosity=2).run(discover)


    # 使用htmlTestRunner生成测试报告
    suits = unittest.TestSuite()
    cases = [TestStringMethods("test_upper"), TestStringMethods("test_isupper"),TestStringMethods("test_split")]
    suits.addTests(cases)

    report_file = "./result.html"
    report_tilte = "fy report"
    desc = "fy description"
    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_tilte, description=desc)
        runner.run(suits)