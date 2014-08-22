# 中国农业大学网关登录脚本

这是项目 [CAUgateway](https://github.com/norbour/CAUgateway) ，
欢迎访问。

## 项目介绍



## 如何使用

使用前请首先在/CAUgateway/py/路径下的LoginCAUGateway.py脚本文件中将如下位置中的学号、密码字符改为要使用的网管账户密码。
```python
	if __name__ == '__main__':
    	loginer = login.Loginer('学号', '密码')
    	login_output = loginer.login()
    	login_status = loginResultProcessor(login_output, loginer)
    	if login_status == 'Occupied' :
        	Usurper = loginUsurp.LoginUsurper('学号', '密码')
```

使用时请直接在终端用Python运行/CAUgateway/py/路径下的LoginCAUGateway.py脚本：

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