# Reviewer-State-Detector
使用Python实现的审稿状态监测器。
等待论文的审稿状态是煎熬且期待的，对于很多的研究人员来说，投稿之后，其每天都会花费时间进入投稿系统查看自己论文的审稿状态进入到哪一步，这样的工作是重复性且枯燥的，更致命的一点是，许多时候，研究人员无法第一时间知悉审稿状态的变化，例如10月1日审稿状态变为了“Awaiting Reviewer Scores”，但研究人员10月3日才登录系统，因此其很难知道这个状态是哪一天改变的。
基于此，我使用Python编写了一个审稿状态检测器。
# 主要功能
针对当前不需验证码的投稿系统，该脚本可以高效定时的获取论文的审稿状态，包括IEEE与IET使用的ScholarOne、Elsevier与Spring使用的Editorial Manager等投稿系统。
# 性能
一次打开，即可一直保持状态的监测，尽可能地降低了内存占用。
# 步骤
## 1.下载Chrome浏览器
链接：https://www.google.cn/intl/zh-CN/chrome/
## 2.下载Chrome浏览器对应版本的Chromedriver驱动程序
查看Chrome浏览器的版本：右上角设置栏 -> 帮助 -> 关于Google Chrome -> “版本 XXXX（正式版本） （64 位）”
链接：https://registry.npmmirror.com/binary.html?path=chromedriver/
例如Chrome浏览器为105.0.5195.127，则下载105.0.5195.X版本（向下兼容的原则）的Chrome Driver。
## 3.将Chrome Driver放置到本代码的同路径下
## 4.使用浏览器的F12工具获取对应按钮的XPATH并替换程序代码中的XPATH
## 5.开启邮箱自动发送审稿状态的邮件
当审稿状态更新时，如果你需要使用邮件进行通知，请点击该链接：（https://blog.csdn.net/LOVEYSUXIN/article/details/124274549），参照该教程，将自己的邮箱（最好是QQ邮箱）开启POP服务，并且获得授权码，将授权码替换程序代码中的授权码。
## ————谢谢————
#有任何问题，欢迎使用邮箱或者访问我的个人博客留言联系我。
#该代码尽可能考虑到了复用，但因为所实现功能较为复杂，无法完全转为可执行程序使用，因此您在使用该脚本时，建议具有一定的Python编程能力，并根据自己的需要对代码进行DIY。