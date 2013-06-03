#__*__ coding:utf-8 __*__
'''
Created on 2013-5-31

@author: huanghu
'''
import xlrd

class OperateExcel(object):
    '''
    classdocs
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        pass;
    
    #excel
    #path excel路径
    #sheet 第几个sheet
    #row 第几行
    #col 第几列
    def operate(self , path ,sheet ,row):
        print path;
        #操作excel
        data = xlrd.open_workbook(path);
        
        #第一列中间表名称
        col = 0;
        tableName = data.sheet_by_index(sheet).cell(row ,col).value;
        
        #第二列中间表字段名称
        col = 1;
        colName = data.sheet_by_index(sheet).cell(row ,col).value;

        #第四列中间表字段类型
        col = 3;
        colType = data.sheet_by_index(sheet).cell(row ,col).value;

        #第五列中间表字段长度
        col = 4;
        colLength = data.sheet_by_index(sheet).cell(row ,col).value; 

        #第十列源表名称
        col = 9;
        sourceTableName = data.sheet_by_index(sheet).cell(row ,col).value;         
        
        #第11列源表字段名称
        col = 10;
        sourceColName = data.sheet_by_index(sheet).cell(row ,col).value;    
        
        #第13列源表字段类型
        col = 12;
        sourceColType = data.sheet_by_index(sheet).cell(row ,col).value;  
        
        #第14列源表字段长度
        col = 13;
        sourceColLength = data.sheet_by_index(sheet).cell(row ,col).value;  

        print '%s %s %s %s %s %s %s %s' %(tableName ,colName ,colType ,colLength ,sourceTableName ,sourceColName ,sourceColType ,sourceColLength)
