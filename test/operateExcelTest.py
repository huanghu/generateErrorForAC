#__*__ coding:utf-8 __*__
'''
Created on 2013-5-31

@author: huanghu
'''
import unittest
from com.operateExcel import OperateExcel 

class Test(unittest.TestCase):

    def testName(self):
        path = u"D:\京东\ERP融合数据集成项目\场景文档\供应商主数据\中间表\\2.8\\360Buy_Phase2_21_接口映射关系_供应商主数据导 入接口_20130522_V2.8.xlsx";
        sheet = 0;
        self.opreate = OperateExcel();
        self.opreate.operate(path, sheet);
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()