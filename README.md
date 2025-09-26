## Review-State-Detector

### Author: Jishu Wang
### Address: Yunnan University
### Blog (Website): http://www.loveffc.cn
### Contact: cswangjishu@hotmail.com
### Note that: 如果您要使用该工具，或者进行任何本地化的改动，请记得点亮Star，这是对我的莫大鼓励。有好的建议或在使用过程中发现Bug请联系我~

-----------------------------------------------  

### 主要功能(两个语言的流程基本相同，请对照使用)
针对当前不需验证码的投稿系统，该脚本可以高效定时的获取论文的审稿状态，包括IEEE与IET使用的ScholarOne、Elsevier与Spring使用的Editorial Manager、MDPI、Hindawi等投稿系统。
### 步骤
### 1.下载Chrome浏览器
链接：https://www.google.cn/intl/zh-CN/chrome/  
Chrome浏览器默认自动更新，会导致Chromedriver无法匹配，如果您想更好的使用该脚本，请关闭Chrome浏览器的自动更新。链接：https://blog.csdn.net/weixin_37858453/article/details/126600461
### 2.下载Chrome浏览器对应版本的Chromedriver驱动程序
查看Chrome浏览器的版本：右上角设置栏 -> 帮助 -> 关于Google Chrome -> “版本 XXXX（正式版本） （64 位）”  
链接：https://sites.google.com/corp/chromium.org/driver/（需翻墙）  
例如Chrome浏览器为105.0.5195.127，则下载105.0.5195.X版本（向下兼容的原则）的Chrome Driver。

或者使用以下命令进行安装
'''pip install chromedriver-binary
并在使用时进行导入
'''import chromedriver_binary
### 3.将Chrome Driver放置到本代码的同路径下
### 4.使用浏览器的F12工具获取对应按钮的XPATH并替换程序代码中的XPATH
### 5.开启邮箱自动发送审稿状态的邮件
当审稿状态更新时，如果你需要使用邮件进行通知，请点击该链接：（ https://blog.csdn.net/LOVEYSUXIN/article/details/124274549 ），参照该教程，将自己的邮箱（最好是QQ邮箱）开启POP服务，并且获得授权码，将授权码替换程序代码中的授权码。
#有任何问题，欢迎使用邮箱或者访问我的个人博客留言联系我。
#该代码尽可能考虑到了复用，但因为所实现功能较为复杂，无法完全转为可执行程序使用，因此您在使用该脚本时，建议具有一定的C#或Python编程能力，并根据自己的需要对代码进行DIY。

-----------------------------------------------  

## Python版 版本更新日志
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
