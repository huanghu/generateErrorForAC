#__*__ coding:utf-8 __*__
'''
Created on 2013-5-31

@author: huanghu
'''
import sys;

from operateExcel import OperateExcel

if __name__ == '__main__':
    if len(sys.argv) == 3:
        sheet = sys.argv[1];
        row = sys.argv[2];
        if sheet.isdigit() == True and row.isdigit():
            sheet = int(sheet);
            row = int(row);
            path = u"D:\京东\ERP融合数据集成项目\场景文档\供应商主数据\中间表\\2.8\\360Buy_Phase2_21_接口映射关系_供应商主数据导 入接口_20130522_V2.8.xlsx";        
            ope = OperateExcel();
            ope.operate(path, sheet, row);

