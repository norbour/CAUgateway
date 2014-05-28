# -*- coding: utf-8 -*-
'''
Created on 2013-03-14

@author: caojin
'''
import re
import string
import os
import sys

class AccountInfoParser:
    '''
    To parse the user_info html file and get every item of
    user account status info.
    '''
    info_str = ''

    def __init__(self, info_str):
        self.info_str = info_str
	
    def parse_name(self):
        '''
        To get the user's name from returned html.
        '''
        namePattern = re.compile(r"NID='(.+)';")
        name = namePattern.search(self.info_str).group(1)
        return name

    def parse_id(self):
        '''
        To get the user's id from returned html.
        '''
        idPattern = re.compile(r"uid='(.+)';pwd")
        id = idPattern.search(self.info_str).group(1)
        return id

    def parse_time(self):
        '''
        To get the length of time this account has been used from returned html.
        '''
        timePattern = re.compile(r"time='(\d*)\s*';")
        time = timePattern.search(self.info_str).group(1)
        return time

    def parse_flow(self):
        '''
        To get the quantity of flow this account has been used from returned html.
        '''
        flowPattern = re.compile(r";flow='(\d*)\s*';")
        flow = flowPattern.search(self.info_str).group(1)
        flow = string.atoi(flow)
        flow0 = flow%1024
        flow1 = flow-flow0
        flow0 = flow0*1000
        flow0 = flow0-flow0%1024
        flow3 = '.'
        if flow0/1024 < 10 :
            flow3='.00' 
        elif flow0/1024 < 100 :
            flow3='.0'
        return str(flow1/1024) + flow3 + str(flow0/1024)

    def parse_fee(self):
        '''
        To get the amount of money this account remains from returned html.
        '''
        feePattern = re.compile(r"fee='(\d*)\s*';")
        fee = feePattern.search(self.info_str).group(1)
        fee = string.atoi(fee)
        return str((fee-fee%100)/10000)

    def parse_l_ip(self):
        '''
        To get the IP address where this account was used last time from returned html.
        '''
        lipPattern = re.compile(r"lip='(.+)';stime")
        lip = lipPattern.search(self.info_str).group(1)
        return lip

    def parse_start_time(self):
        '''
        To get the login time when this account was used last time from returned html.
        '''
        stimePattern = re.compile(r"stime='(.+)';etime")
        stime = stimePattern.search(self.info_str).group(1)
        return stime

    def parse_end_time(self):
        '''
        To get the logout time when this account was used last time from returned html.
        '''
        etimePattern = re.compile(r"etime='(.+)';")
        etime = etimePattern.search(self.info_str).group(1)
        return etime

    def parse_remain_flow(self):
        '''
        To get the quantity of flow this account remains from returned html.
        '''
        olflowPattern = re.compile(r";olflow=(\d*);")
        olflow = olflowPattern.search(self.info_str).group(1)
        olflow = string.atoi(olflow)
        olflow0=olflow%1024
        olflow1=olflow-olflow0
        olflow0=olflow0*1000
        olflow0=olflow0-olflow0%1024
        olflow3='.'
        if olflow0/1024 < 10 :
            olflow3='.00'
        elif olflow0/1024 < 100 :
            olflow3='.0'
        return str(olflow1/1024) + olflow3 + str(olflow0/1024)

    def show_account_info(self):
        '''
        To show the account info when login successfully.
        '''
        print self.parse_name().decode('gb2312').encode('utf-8') + '(' + self.parse_id() + ')'
        print '已使用时间： ' + self.parse_time() + ' Min'
        print '已使用流量： ' + self.parse_flow() + ' MB'
        print '账户余额： ' + self.parse_fee()
        print '上次登录IP： ' + self.parse_l_ip()
        print '上次登录时间： ' + self.parse_start_time()
        print '上次注销时间： ' + self.parse_end_time()
        print '本月剩余流量： ' + self.parse_remain_flow() + ' MB'		