"""
Author: Jishu Wang
Address: Yunnan University
Website: http://www.loveffc.cn
Contact: cswangjishu@hotmail.com
Note that: if you need use this tool, please click "Star" for my GitHub.
"""
# 获取时间的库
import datetime
# 发送邮件需要的库
import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText

# 获取审稿状态需要的库
from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
# option.add_argument('headless')  # 浏览器后台运行
chromedriver_path = 'chromedriver.exe'  # chromedriver的地址
"""
https://chromedriver.storage.googleapis.com/index.html
点击此链接，根据你Chrome(谷歌)浏览器的版本,下载对应的chromedriver,并解压,然后将chromedriver.exe放到本代码的同目录下
"""


def ScholarOne(url, username, password):  # ScholarOne投稿系统，IEEE常用
    """
    url:string, 你投稿期刊的网址
    username:string, 投稿系统的用户名
    password:string, 投稿系统的密码
    """

    driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=option)  # 导入浏览器设置
    driver.get(url)  # 设置目标网址
    time.sleep(5)  # 设置一个等待时间，保证在网络不佳情况下也能获取页面元素
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/form/div[6]/div/div/div[1]/div[1]/div[2]/fieldset/div[2]/input").send_keys(
        username)  # 输入用户名
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/form/div[6]/div/div/div[1]/div[1]/div[2]/fieldset/div[3]/div/div/input[1]").send_keys(
        password)  # 输入密码
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/form/div[6]/div/div/div[1]/div[1]/div[2]/fieldset/div[4]/a").click()  # 点击登录按钮
    time.sleep(5)
    driver.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/div/div[3]/div/ul/li[2]/a").click()  # 跳转Author页面

    time.sleep(5)
    newest_status = ""  # 之前记录的审稿状态
    current_status = driver.find_element(By.XPATH,
                                         "/html/body/div[1]/form/div[3]/div/div[2]/div[5]/div/table/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/span").text  # 本次获取的审稿状态
    if current_status != newest_status:  # 如果审稿状态发生改变,则显示最新状态
        newest_status = current_status  # 更新审稿状态
        print(newest_status, datetime.datetime.now())
        # 如果状态更新时你希望通过邮件接收的话,请不要注释这行代码，否则请注释
        # SendEmail("", "", "", "smtp.qq.com", state)  # 请自行设置参数


def EditorialManager(url, username, password):  # Editorial Manager投稿系统，Elsevier常用
    """
    url:string, 你投稿期刊的网址
    usernamexpath:string, 使用网页开发工具找到用户名输入框的XPATH,下同
    passwordxpath:string
    loginbuttonxpath:string
    statexpath:string,存放你审稿状态的元素的XPATH
    """

    driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=option)
    driver.get(url)
    time.sleep(10)  # EM系统访问较为缓慢，设置一个等待时间，从而保证获取页面元素

    driver.switch_to.frame("content")  # EM系统的登录页面使用了JS动态加载2个iframe框架的方式，因此还需要先进入iframe中才能获取页面元素
    driver.switch_to.frame("login")
    driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div/fieldset/div[2]/input[1]").send_keys(username)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div/fieldset/div[2]/input[2]").send_keys(password)
    driver.find_element(By.XPATH,
                        "/html/body/div/div[2]/form/div/fieldset/table/tbody/tr[1]/td/div/div[1]/input[1]").click()

    time.sleep(10)  # EM系统访问较为缓慢，设置一个等待时间，从而保证获取页面元素
    driver.switch_to.frame("content")  # EM系统的状态页面使用了JS动态加载1个iframe框架的方式，因此还需要先进入iframe中才能获取页面元素
    driver.find_element(By.XPATH, "/html/body/div[1]/main/form/div[3]/div[2]/div/div/div[3]/fieldset/div/a").click()

    time.sleep(10)  # EM系统访问较为缓慢，设置一个等待时间，从而保证获取页面元素
    newest_status = ""  # 之前记录的审稿状态
    current_status = driver.find_element(By.XPATH,
                                         "/html/body/main/div/fieldset/form/div/table/tbody/tr/td[7]").text
    if current_status != newest_status:  # 如果审稿状态发生改变,则显示最新状态
        newest_status = current_status
        print(newest_status, datetime.datetime.now())
        # 如果状态更新时你希望通过邮件接收的话,请不要注释这行代码，否则请注释
        # SendEmail("", "", "", "smtp.qq.com", state)  # 请自行设置


def SendEmail(fromaddress, frompassword, toaddress, mailserver, state):  # 发送最新审稿状态的邮件
    """
    fromaddress:string,发送邮件的邮箱
    frompassword:string,发送邮件的邮箱的授权码,具体获取流程请参考前文
    toaddress:string,接收审稿状态的邮箱
    mailserver:string,所使用的邮箱服务器,QQ邮箱为:smtp.qq.com
    state:string,最新的审稿状态,前一个函数中已获得
    使用邮件来发送最新审稿状态,容易存在邮件被误认为垃圾邮件的情况,因此建议使用短信发送的方法
    """

    message = MIMEText("你的文章审稿状态已更新: " + state, "plain", "utf-8")  # 邮件内容,纯文本格式,编码
    message['From'] = "ArticleStatusUpdate"  # 发送者姓名
    message["To"] = Header("你自己", "utf-8")  # 接收者姓名
    message["Subject"] = Header("审稿状态更新:" + state, "utf-8")  # 邮件名,编码

    try:
        smtpobj = smtplib.SMTP_SSL(mailserver.encode(), 465)  # 建立连接
        smtpobj.login(fromaddress, frompassword)  # 登录邮箱
        smtpobj.sendmail(fromaddress, toaddress, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("邮件发送失败")
    finally:
        smtpobj.quit()  # 关闭邮件服务器


if __name__ == '__main__':
    Option = "1"  # 1：ScholarOne，2：Editorial Manager
    # Option = input()
    # 可以默认设定，也可以手动输入来选择投稿系统

    if Option == "1":  # ScholarOne投稿系统
        while True:
            try:  # 捕捉异常，避免报错而停止运行
                ScholarOne("https://mc.manuscriptcentral.com/t-its", "用户名", "密码")  # 以IEEE TITS期刊为例
            except Exception as e:
                ScholarOne("https://mc.manuscriptcentral.com/t-its", "用户名",
                           "密码")  # 以IEEE TITS期刊为例
            time.sleep(300)  # 每隔多少秒后刷新一次状态,默认设置为5分钟(300秒)
    elif Option == "2":  # Editorial Manager投稿系统
        while True:
            try:
                EditorialManager("https://www.editorialmanager.com/knosys/default2.aspx", "用户名", "密码")  # 以KBS期刊为例
            except Exception as e:
                EditorialManager("https://www.editorialmanager.com/knosys/default2.aspx", "用户名", "密码")  # 以KBS期刊为例
            time.sleep(300)
