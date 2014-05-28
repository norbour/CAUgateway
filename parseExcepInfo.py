# -*- coding: utf-8 -*-
'''
Created on 2013-03-16

@author: caojin
'''
import re
import string
import os
import sys

class ExceptionInfoParser:
    '''
    To parse the returned html file and get exception info when login failed.
    '''
    except_info_str = ''

    def __init__(self, except_info_str):
        self.except_info_str = except_info_str
	
    def get_ExceptTypeCode(self):
        '''
        To get the code of exception type from returned html.
        '''
        exceptPattern = re.compile(r"Msg=(\d+);")
        exceptCode = exceptPattern.search(self.except_info_str).group(1)
        return string.atoi(exceptCode)
		
    def get_XIP(self):
        '''
        To get the code of exception type from returned html.
        '''
        xipPattern = re.compile(r";xip='(.+)';mac")
        xip = xipPattern.search(self.except_info_str).group(1)
        return xip       

    def get_ExceptInfo(self, exceptTypeCode):
        '''
        To check the exception type code and tell people what exception it is.
        '''
        if exceptTypeCode == 1:
            return '用户名或密码不对'
        elif exceptTypeCode == 2:
            return '该账号正在IP为：' + self.get_XIP() + '的机器上使用'
        elif exceptTypeCode == 4:
            return '本月超出使用限额或余额不足'
        elif exceptTypeCode == 5:
            return '本用户暂停使用'