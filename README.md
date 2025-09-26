## Review-Status-Detector

### Author: Jishu Wang
### Address: Yunnan University
### Homepage: http://www.loveffc.cn
### Contact: cswangjishu@hotmail.com
### Note that: 代码尽可能考虑到了复用，但因为实现流程稍显复杂，无法转为完全一键式的应用程序使用，因此在使用时，建议您具有一定的C#或Python编程能力，并根据自己的需要对代码进行DIY。如果您觉得该工具有所帮助，或者想要进行任何本地化的改动，请Star~，这是对我的莫大鼓励。有好的建议或问题请联系我~

-----------------------------------------------  

### 主要功能(两个语言的流程基本相同，请对照使用)
针对当前不需验证码的投稿系统，该脚本可以高效定时的获取论文的审稿状态，当前已覆盖IEEE旗下期刊主要使用的ScholarOne、Elsevier旗下期刊使用的Editorial Manager投稿系统。
### 步骤
### 1.下载Chrome浏览器
链接：https://www.google.cn/intl/zh-CN/chrome/  
Chrome浏览器默认自动更新，会导致Chromedriver无法匹配，如果您想更好的使用该脚本，请关闭Chrome浏览器的自动更新。链接：https://blog.csdn.net/weixin_37858453/article/details/126600461
### 2.下载Chrome浏览器对应版本的Chromedriver驱动程序
### 2.1 Exe版本
查看Chrome浏览器的版本：右上角设置栏 -> 帮助 -> 关于Google Chrome -> “版本 XXXX（正式版本） （64 位）”  
链接：https://sites.google.com/corp/chromium.org/driver/
（需翻墙）  或者https://github.com/dreamshao/chromedriver
（可能停止更新）。例如Chrome浏览器为105.0.5195.127，则下载105.0.5195.X版本（向下兼容的原则）的Chrome Driver。下载后将Chromedriver放置到本代码的同路径下，从而便于使用。

### 2.2 Python库
或者使用以下命令进行安装

`pip install chromedriver-binary`

并在使用时进行导入

`import chromedriver_binary`
### 3.使用浏览器的F12工具获取对应按钮的XPATH并替换程序代码中的XPATH，从而完成其它系统的文章审稿状态自动获取
### 4.开启邮箱自动发送审稿状态的邮件
当审稿状态更新时，如果你需要使用邮件进行通知，请点击该链接：（ https://blog.csdn.net/LOVEYSUXIN/article/details/124274549 ），参照该教程，将自己的邮箱（最好是QQ邮箱）开启POP服务，并且获得授权码，将授权码替换程序代码中的授权码。

-----------------------------------------------  

## Python版 版本更新日志
### 2025.09.24 Version 2.1
对代码进行重写，将在未来逐步添加更多投稿系统的论文状态自动获取。
### 2024.06.12 Version 1.2
由于邮箱和Chromedriver依赖库对于安全机制的更新，为了确保正常使用，对部分代码进行了更新。
### 2023.01.15 Version 1.1
添加了Editorial Manager（EM）投稿系统，经测试可正常使用。
### 2022.09.25 Version 1.0
目前仅实现了ScholarOne投稿系统，若您使用的是其它投稿系统，可联系我说明，或者自行DIY代码。

-----------------------------------------------  

## C# WPF版 版本更新日志
### 2022.11.23 Version 1.0
已覆盖Scholarone、Editorial Manager、MDPI三个投稿系统（但可能存在一些使用异常），已Commit第一版的可执行文件，之后将代码开源，供大家一起完善。  
### 2022.11.01 Version 0.0
正在使用C# WPF技术实现可视化的PC端桌面版本，以进一步提升使用体验与便捷程度，敬请期待。
