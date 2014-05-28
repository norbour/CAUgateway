# -*- coding: utf-8 -*-
'''
Created on 2013-03-12

@author: caojin
'''
import urllib, urllib2
import re
import sys
import os
import login
import loginUsurp
import parseInfo
import parseExcepInfo

def loginResultProcessor(login_output, loginer):
    '''
    Parse returned html and figure out status info after a login action.
    '''
    if login_output == 0 :
        print 'Login successfully!'
        info_str = loginer.get_account_info() 
        InfoParser = parseInfo.AccountInfoParser(info_str)
        InfoParser.show_account_info()
        #sys.exit()
        return 'OK'
    elif login_output == 1 :
        print 'Sorry, login failed.'
		#POST登录失败时从服务器返回的html包含异常信息，直接读取并解析
        excep_file = file(os.getcwd() + '\login_reult.html')
        except_info_str = excep_file.read()
        excep_file.close()
        ExcepInfoParser = parseExcepInfo.ExceptionInfoParser(except_info_str)
        exceptTypeCode = ExcepInfoParser.get_ExceptTypeCode()
        print ExcepInfoParser.get_ExceptInfo(exceptTypeCode)
        if exceptTypeCode == 2 :
            return 'Occupied'
        else :
            return 'OK'
    elif login_output == 2 :
        print "Shit! Don't know what's happening. Try to run this script again. "
        print "If that doesn't help, try to contact me and report this bug. "
        print "E-mail addr: caojincau@qq.com "
        #sys.exit()
        return 'OK'

if __name__ == '__main__':
    loginer = login.Loginer('学号', '密码')
    login_output = loginer.login()
    login_status = loginResultProcessor(login_output, loginer)
    if login_status == 'Occupied' :
        Usurper = loginUsurp.LoginUsurper('学号', '密码')
        what_todo = Usurper.Induce()
        if what_todo == 'usurp' :
            usurp_output = Usurper.kickOffAndLogin()
            loginResultProcessor(usurp_output, loginer)
        else :
            sys.exit()
    else :
        sys.exit()