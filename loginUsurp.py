# -*- coding: utf-8 -*-
'''
Created on 2013-03-17

@author: caojin
'''
import urllib, urllib2
import os
import parseExcepInfo
	
class LoginUsurper:
    '''
    A tool can help you to login when your account are now occupied somewhere else.
    '''
    usurp_header = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17' }
    account = ''
    passwd = ''
    path = os.getcwd()

    def __init__(self, account, pwd):
        self.account = account
        self.passwd = pwd

    def Induce(self):
        '''
        Ask and tell this progarm if the user want to usurp login.
        '''
        do_what = raw_input("要抢占登录吗？[Y/N]:") 
        if do_what == 'Y' :
            return 'usurp'
        elif do_what == 'N' :
            return 'nevermind'
	
    def kickOffAndLogin(self):
        '''
        Encode and post account info including id and passwd to server in order to usurp login.
        '''
        postdata = { 'AMKKey':'',
		             'DDDDD':self.account,
					 'upass':self.passwd }
        postdata = urllib.urlencode(postdata)
        print 'Logining...'
        req_post = urllib2.Request(url='http://202.205.80.10', 
		                      data=postdata, headers=self.usurp_header)
        result = urllib2.urlopen(req_post).read()
        result_file = file( self.path + r'\kicklogin_reult.html', 'w')
        result_file.write(result)
        result_file.close()
		
        if '您已经成功登录'.decode('utf-8').encode('gb2312') in result :
            return 0
            
        elif '用户名或密码不对'.decode('utf-8').encode('gb2312') in result :
            return 1
        else :
            return 2