# 中国农业大学网关登录脚本

这是项目 [CAUgateway](https://github.com/norbour/CAUgateway) ，
欢迎访问。

## 项目介绍

做这个这个项目的起因，是有一段时间农大校内出现了“上不了网”的现象。这个其实是因为大家平时在校内上外网，通常需要到网络综合服务平台`http://netcenter.cau.edu.cn/`这个网关登录页面去填写自己的账号密码，然后才能登录网关账户。之所以“上不了网”是因为上边说的网页不能访问了，大家相当于没了登录网关的入口，而实际上负责管理网关的服务器`202.205.80.10`是已然正常工作的。所以，只要绕开[网络综合服务平台页面](http://netcenter.cau.edu.cn/)直接去访问网关登录服务器就可以了。

说起来也简单，就是用`post`方法向`http://202.205.80.10/`提交表单数据。字段如下：`0MKKey=login&DDDDD=网关帐号&upass=网关密码`。需要注意的是，直接在URL后面加这些是没有用的，网关服务器只接受post数据。写网页的话可以做个表单，method设置成post。

本项目是基于`Python 2.7`实现的。

## 如何使用

使用前请首先在`/CAUgateway/py/`路径下的`LoginCAUGateway.py`脚本文件中将如下位置中的学号、密码字符改为要使用的网关账户密码。
```python
if __name__ == '__main__':
    loginer = login.Loginer('学号', '密码')
    login_output = loginer.login()
    login_status = loginResultProcessor(login_output, loginer)
    if login_status == 'Occupied' :
        Usurper = loginUsurp.LoginUsurper('学号', '密码')
```

使用时请直接在终端用Python运行`/CAUgateway/py/`路径下的`LoginCAUGateway.py`脚本：

	$ python /CAUgateway/py/LoginCAUGateway.py

## 版本库地址

这个项目的版本库是 **Git格式** ，在 Windows、Linux、Mac OS X
平台都有客户端工具可以访问。虽然版本库只提供Git一种格式，
但是你还是可以用其他用其他工具访问，如 ``svn`` 和 ``hg`` 。

支持三种访问协议：

* HTTP协议: `https://github.com/gotgithub/CAUgateway.git` 。
* Git协议: `git://github.com/gotgithub/CAUgateway.git` 。
* SSH协议: `ssh://git@github.com/gotgithub/CAUgateway.git` 。

## 克隆版本库

操作示例：

    $ git clone git://github.com/gotgithub/CAUgateway.git