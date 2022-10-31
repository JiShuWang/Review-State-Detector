"""
Author: Jishu Wang
Address: Yunnan University
Website: http://www.loveffc.cn
Contact: cswangjishu@hotmail.com
Note that: if you need use this tool, please click "Star" for my GitHub.
"""
# 获取时间的库
import datetime
import time
# 发送邮件需要的库
import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 获取审稿状态需要的库
from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument('headless')  # 浏览器后台运行
chromedriver_path = 'chromedriver.exe'  # chromedriver的地址
"""
https://chromedriver.storage.googleapis.com/index.html
点击此链接，根据你Chrome(谷歌)浏览器的版本,下载对应的chromedriver,并解压,然后将chromedriver的文件地址替换掉上述的地址
"""

state = ""# 审稿状态

def GetArticleState(url, usernamexpath, passwordxpath, username, password, loginbuttonxpath, statexpath):  # 定时获取审稿状态
    """
    url:string, 你投稿期刊的网址
    usernamexpath:string, 使用网页开发工具找到用户名输入框的XPATH,下同
    passwordxpath:string
    loginbuttonxpath:string
    statexpath:string,存放你审稿状态的元素的XPATH
    """
    global state
    driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=option)
    driver.get(url)
    driver.find_element(By.XPATH, usernamexpath).send_keys(username)
    driver.find_element(By.XPATH, passwordxpath).send_keys(password)
    driver.find_element(By.XPATH, loginbuttonxpath).click()
    # 部分网页登录后还需要点击按钮跳转一次或多次，才能到达审稿状态页面
    driver.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/div/div[3]/div/ul/li[2]/a").click()
    # 这里写具体点击跳转元素的XPATH

    # 通过点击刚才获得的跳转按钮,实现刷新页面获取审稿状态
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/form/div[1]/div/div[3]/div/ul/li[2]/a").click()
    if driver.find_element(By.XPATH, statexpath).text != state:  # 如果审稿状态发生改变,则发送邮件通知
        state = driver.find_element(By.XPATH, statexpath).text
        print(state, datetime.datetime.now())
        # 如果每次状态更新,你希望通过邮件接收的话,否则请注释这行代码
        SendEmail("发送者邮箱", "邮箱校验码", "接收者邮箱", "smtp.qq.com", state)#发送者与接收者可为同一个


def SendEmail(fromaddress, frompassword, toaddress, mailserver, state):  # 发送最新审稿状态的邮件
    """
    fromaddress:string,发送邮件的邮箱
    frompassword:string,发送邮件的邮箱的授权码,具体获取流程请参考前文
    toaddress:string,接收审稿状态的邮箱
    mailserver:string,所使用的邮箱服务器,QQ邮箱为:smtp.qq.com
    state:string,最新的审稿状态,前一个函数中已获得
    使用邮件来发送最新审稿状态,容易存在邮件被误认为垃圾邮件的情况,因此建议使用短信发送的方法
    """
    message = MIMEText("你的文章审稿状态已更新:" + state, "plain", "utf-8")  # 邮件内容,纯文本格式,编码
    message['From'] = Header("审稿状态监控器")  # 发送者姓名
    message["To"] = Header("你自己")  # 接收者姓名
    message["Subject"] = Header("审稿状态更新:" + state, "utf-8")  # 邮件名,编码

    try:
        smtpobj = smtplib.SMTP_SSL(mailserver)  # 建立连接
        smtpobj.connect(mailserver, 465)  # 发起请求
        smtpobj.login(fromaddress, frompassword)  # 登录邮箱
        smtpobj.sendmail(fromaddress, toaddress, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("邮件发送失败")
    finally:
        smtpobj.quit()  # 关闭邮件服务器


if __name__ == '__main__':
    while True:
        try:
            GetArticleState("https://mc.manuscriptcentral.com/t-its",
                            "/html/body/div[1]/form/div[6]/div/div/div[1]/div[1]/div[2]/fieldset/div[2]/input",
                            "/html/body/div[1]/form/div[6]/div/div/div[1]/div[1]/div[2]/fieldset/div[3]/div/div/input[1]",
                            "投稿系统账号", "投稿系统密码",
                            "/html/body/div[1]/form/div[6]/div/div/div[1]/div[1]/div[2]/fieldset/div[4]/a",
                            "/html/body/div[1]/form/div[3]/div/div[2]/div[5]/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/span")  # ScholarOne投稿系统(IEEE、IET)可直接采用这个
        except Exception as e:
            GetArticleState("https://mc.manuscriptcentral.com/t-its",
                            "/html/body/div[1]/form/div[6]/div/div/div[1]/div[1]/div[2]/fieldset/div[2]/input",
                            "/html/body/div[1]/form/div[6]/div/div/div[1]/div[1]/div[2]/fieldset/div[3]/div/div/input[1]",
                            "投稿系统账号", "投稿系统密码",
                            "/html/body/div[1]/form/div[6]/div/div/div[1]/div[1]/div[2]/fieldset/div[4]/a",
                            "/html/body/div[1]/form/div[3]/div/div[2]/div[5]/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/span")  # ScholarOne投稿系统(IEEE、IET)可直接采用这个
        time.sleep(1800)  # 每隔多少秒后刷新一次状态,初始设置为30分钟(1800秒)
    # 可将函数针对不同的期刊网站(如Editorial Manager、ScholarOne等)设置不同的参数,每次具体调用即可
    # GetArticleState("")
    # GetArticleState("")
    # GetArticleState("")
