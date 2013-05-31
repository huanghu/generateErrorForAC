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
    
    ##����excel
    #path excel路径
    #sheet 第几个sheet
    def operate(self , path ,sheet):
        #操作excel
        print "path " + path
        data = xlrd.open_workbook(path);
        print data.sheet_by_index(sheet);