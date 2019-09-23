# 案例10
from email.mime.text import MIMEText
from email.header import Header

msg = MIMEText("Hello wold",  "plain", "utf-8")
# 下面代码故意写错，说明，所谓的发送者的地址，只是从一个Header的第一个参数作为字符串构建的内容
# 用utf8编码是因为很可能内容包含非英文字符
header_from = Header("xingming<123456@qq.com>")
msg['From'] = header_from

# 填写接受者信息
header_to = Header("he.x.m123@163.com,499942031@qq.com,423424@sina.cn")
msg['To'] = header_to

header_sub = Header("hello world", 'utf-8')
msg['Subject'] = header_sub


# 构建发送者地址和登录信息
from_addr = "499942031@qq.com"
# 此处密码是经过申请设置后的授权码，不是不是不是你的qq邮箱密码
from_pwd = "jiyytuqgfhdqbjcd"


# 收件人信息
# 此处使用qq邮箱，我给自己发送
to_addr = "he.x.m123@163.com"

smtp_srv = "smtp.qq.com"


try:
    import smtplib

    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)

    srv.login(from_addr, from_pwd)
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    srv.quit()

except Exception as e:
    print(e)