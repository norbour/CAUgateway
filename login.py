# -*- coding: utf-8 -*-
'''
Created on 2013-03-12

@author: caojin
'''
import urllib, urllib2
import re
import sys
import os

import parseInfo
import parseExcepInfo

class Loginer:
    '''
    A simple script to login the gateway CAU campus-network.
	'''
    login_header = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17',
	                 'Content-Type':'application/x-www-form-urlencoded' }
    getinfo_header = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17' }
    account = ''
    passwd = ''
    path = os.getcwd()

    def __init__(self, account, pwd):
        self.account = account
        self.passwd = pwd
        
    def login(self):
        '''
        Encode and post account info including id and passwd to server in order to login.
        '''
        postdata = { '0MKKey':'login',
		             'DDDDD':self.account,
					 'upass':self.passwd }
        postdata = urllib.urlencode(postdata)
        print 'Logining...'
        req_post = urllib2.Request(url='http://202.205.80.10', 
		                      data=postdata, headers=self.login_header)
        result = urllib2.urlopen(req_post).read()
        #result = str(result).decode('utf-8').encode('gbk')
        result_file = file( self.path + r'\login_reult.html', 'w')
        result_file.write(result)
        result_file.close()


        
        if '您已经成功登录'.decode('utf-8').encode('gb2312') in result :
            return 0
            
        elif '用户名或密码不对'.decode('utf-8').encode('gb2312') in result :
            return 1
        else :
            return 2
			
    def get_account_info(self):
        '''
        To get the html file which containing user info when login successfully, then save it \
        under current path and return it in a string.
        '''
        print 'Getting your account info...'
        #用POST方法登陆成功后，服务器直接返回的html里并不包含账户用量信息 \
		#需要再用GET方法向服务器请求账户用量信息
        req_get = urllib2.Request(url='http://202.205.80.10', headers=self.getinfo_header)
        result = urllib2.urlopen(req_get).read()
        result_file = file( self.path + r'\account_info.html', 'w')
        result_file.write(result)
        result_file.close()
        return str(result)