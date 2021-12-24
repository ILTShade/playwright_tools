# 基于PLAYWRIGHT的便捷工具

## 基本流程

主体框架为基于playwright实现的一些生活、学习中的便利性工具，将生活、学习中的重复性高的网页操作等利用playwright完成，方便学习和生活。

主要包含两部分：
1. 基于playwright实现的server.py，默认运行着一个playwright browser，所有的功能均部署在server上，通过引入参数执行命令
2. 用于发送命令参数的client.py

server和client的参数通信采用socket的形式，通信的参数为\(type, args\)元组的形式，其中type由server确定，args是输入的参数

socket的端口号为：xxxx（待定）

## 基本工具和接口参数

拟支持以下若干种基本工具

1. 自动获取github网址并更改本地的host文件，便利访问github

2. 自动完成清华大学每日进出校申请

3. 自动完成实验室服务器自动联网
