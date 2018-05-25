# -*- coding: UTF-8 -*-       
import smtplib  
import sys  
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formatdate
import datetime
import uniout
encoding = 'utf-8'  

def tosend(to_list,start,end,tomail):
    if to_list is None or len(to_list)==0:
        print 'result is null'
        return

    #发送邮件的相关信息
    smtpHost = 'smtp.qq.com'  
    smtpPort = '25'  
    sslPort  = '465'   
    fromMail = '730530507@qq.com'  
    toMail   = tomail  
    username = '730530507@qq.com'  
    password = 'yiuthnszusifbbdj'  
    #解决中文问题  
    reload(sys)  
    sys.setdefaultencoding('utf-8')  
    
    #邮件标题和内容  

    subject  = '秋刀鱼来啦:7个交易日内十字星放量,今天是:'+ datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    body     = format(to_list,start,end)

    #初始化邮件  
    
    mail = MIMEText(body.encode(encoding),'html',encoding)  
    mail['Subject'] = Header(subject,encoding)  
    mail['From'] = fromMail  
    mail['To'] = toMail
    mail['Date'] = formatdate()  

    #连接smtp服务器，明文/SSL/TLS三种方式，根据你使用的SMTP支持情况选择一种  
    #普通方式，通信过程不加密  
    #smtp = smtplib.SMTP(smtpHost,smtpPort)  
    #smtp.ehlo()  
    #smtp.login(username,password)  

    #tls加密方式，通信过程加密，邮件数据安全，使用正常的smtp端口  
    #smtp = smtplib.SMTP(smtpHost,smtpPort)  
    #smtp.ehlo()  
    #smtp.starttls()  
    #smtp.ehlo()  
    #smtp.login(username,password)  

    #纯粹的ssl加密方式，通信过程加密，邮件数据安全  
    smtp = smtplib.SMTP_SSL(smtpHost,sslPort)  
    smtp.ehlo()  
    smtp.login(username,password)  

    #发送邮件  
    smtp.sendmail(fromMail,toMail,mail.as_string())  
    smtp.close()  
    print 'OK'  

def format(to_list,start,end):
    value=''
    for temp in to_list.index:
        temp=to_list.loc[temp]
        value+=  '''<tr>
                        <td class='x25'>%s</td>
                        <td class=x24>%s</td>
                        <td class=x24>%s</td>
                        <td class=x24>%s</td>
                        <td class=x24>%s</td>
                        <td class=x24>%s</td>
                        <td class=x241>%s</td>
                        <td class=x30><a href="%s">点击查看k线</a></td>
                    </tr>'''%(temp.code,temp.tname,temp.pe,temp.turnover,temp.nowprice,temp.change,temp.tip,temp.kline)
    print value
    return '''<html>
            <head>
                <style>
                    .x21 {
                        mso-style-parent: style0;
                        mso-number-format: General;
                         text-align: center;
                        vertical-align: middle;
                        white-space: nowrap;
                        background: auto;
                        mso-pattern: auto;
                        color: #000000;
                        font-size: 11pt;
                        font-weight: 400;
                        font-style: normal;
                        font-family: "宋体", "sans-serif";
                        border: none;
                        mso-protection: locked visible;
                    }
                    a.one:hover{
                        width: 100%;
                        height:100%;
                    }
                    .x22 {
                        mso-style-parent: style0;
                        mso-number-format: General;
                         text-align: center;
                        vertical-align: middle;
                        white-space: nowrap;
                        mso-char-indent-count: 1;
                        padding-left: 8px;
                        background: auto;
                        mso-pattern: auto;
                        color: #000000;
                        font-size: 11pt;
                        font-weight: 400;
                        font-style: normal;
                        font-family: "宋体", "sans-serif";
                        border: none;
                        mso-protection: locked visible;
                    }

                    .x23 {
                        mso-style-parent: style0;
                        mso-number-format: "\@";
                        text-align: center;
                        vertical-align: middle;
                        white-space: nowrap;
                        background: auto;
                        mso-pattern: auto;
                        font-size: 10pt;
                        font-weight: 400;
                        font-style: normal;
                        font-family: "宋体", "sans-serif";
                        border-top: 1px solid #808080;
                        border-right: 1px solid #A6A6A6;
                        border-bottom: 1px solid #BFBFBF;
                        border-left: none;
                        mso-diagonal-down: none;
                        mso-diagonal-up: none;
                        mso-protection: locked visible;
                    }

                    .x24 {
                        mso-style-parent: style0;
                        mso-number-format: General;
                        text-align: center;
                        vertical-align: middle;
                        white-space: nowrap;
                        mso-char-indent-count: 1;
                        padding-left: 7px;
                        background: auto;
                        mso-pattern: auto;
                        font-size: 10pt;
                        font-weight: 400;
                        font-style: normal;
                        font-family: "宋体", "monospace";
                        border-top: 1px solid #808080;
                        border-right: 1px solid #BFBFBF;
                        border-bottom: 1px solid #BFBFBF;
                        border-left: 1px solid #BFBFBF;
                        mso-diagonal-down: none;
                        mso-diagonal-up: none;
                        mso-protection: locked visible;
                    }
                      .x241 {
                        mso-style-parent: style0;
                        mso-number-format: General;
                        text-align: right;
                        padding-right:5px;
                        vertical-align: middle;
                        white-space: nowrap;
                        mso-char-indent-count: 1;
                        padding-left: 7px;
                        color:#FF0000;
                        background: auto;
                        mso-pattern: auto;
                        font-size: 10pt;
                        font-weight: 400;
                        font-style: normal;
                        font-family: "宋体", "monospace";
                        border-top: 1px solid #808080;
                        border-right: 1px solid #BFBFBF;
                        border-bottom: 1px solid #BFBFBF;
                        border-left: 1px solid #BFBFBF;
                        mso-diagonal-down: none;
                        mso-diagonal-up: none;
                        mso-protection: locked visible;
                    }
                    .x26_left{
                        border-left: 1px solid #A6A6A6;
                    }
                     .x24_left{
                        border-left: 1px solid #BFBFBF;
                    }
                    .x25 {
                        mso-style-parent: style0;
                        mso-number-format: General;
                        text-align: center;
                        vertical-align: middle;
                        white-space: nowrap;
                        background: auto;
                        mso-pattern: auto;
                        font-size: 10pt;
                        font-weight: 400;
                        font-style: normal;
                        font-family: "宋体", "monospace";
                        border-top: 1px solid #808080;
                        border-right: 1px solid #BFBFBF;
                        border-bottom: 1px solid #BFBFBF;
                        border-left: 1px solid #A6A6A6;
                        mso-diagonal-down: none;
                        mso-diagonal-up: none;
                        mso-protection: locked visible;
                    }

                    .x26 {
                        mso-style-parent: style0;
                        mso-number-format: General;
                        text-align: center;
                        vertical-align: middle;
                        white-space: nowrap;
                        background: #EBF6FF;
                        mso-pattern: auto none;
                        font-size: 10pt;
                        font-weight: 400;
                        font-style: normal;
                        font-family: "宋体", "monospace";
                        border-top: 1px solid #808080;
                        border-right: 1px solid #A6A6A6;
                        border-bottom: 1px solid #808080;
                        border-left: 1px solid #808080;
                        mso-diagonal-down: none;
                        mso-diagonal-up: none;
                        mso-protection: locked visible;
                    }

                    .x27 {
                        mso-style-parent: style0;
                        mso-number-format: General;
                        text-align: center;
                        vertical-align: middle;
                        white-space: nowrap;
                        background: #EBF6FF;
                        mso-pattern: auto none;
                        font-size: 10pt;
                        font-weight: 400;
                        font-style: normal;
                        font-family: "宋体", "monospace";
                        border-top: 1px solid #808080;
                        border-right: 1px solid #808080;
                        border-bottom: 1px solid #808080;
                        border-left: 1px solid #A6A6A6;
                        mso-diagonal-down: none;
                        mso-diagonal-up: none;
                        mso-protection: locked visible;
                    }

                    .x28 {
                        mso-style-parent: style0;
                        mso-number-format: General;
                        text-align: center;
                        vertical-align: middle;
                        white-space: nowrap;
                        background: #EBF6FF;
                        mso-pattern: auto none;
                        font-size: 10pt;
                        font-weight: 400;
                        font-style: normal;
                        font-family: "宋体", "monospace";
                        border-top: 1px solid #808080;
                        border-right: 1px solid #808080;
                        border-bottom: 1px solid #808080;
                        border-left: 1px solid #808080;
                        mso-diagonal-down: none;
                        mso-diagonal-up: none;
                        mso-protection: locked visible;
                    }

                    .x29 {
                        mso-style-parent: style0;
                        mso-number-format: General;
                        text-align: right;
                        padding-right:5px;
                        vertical-align: middle;
                        white-space: nowrap;
                        background: auto;
                        mso-pattern: auto;
                        font-size: 10pt;
                        font-weight: 400;
                        font-style: normal;
                        font-family: "宋体", "monospace";
                        border-top: 1px solid #808080;
                        border-right: 1px solid #BFBFBF;
                        border-bottom: 1px solid #BFBFBF;
                        border-left: 1px solid #BFBFBF;
                        mso-diagonal-down: none;
                        mso-diagonal-up: none;
                        mso-protection: locked visible;
                    }

                    .x30 {
                        mso-style-parent: style0;
                        mso-number-format: "0\.000_ ";
                        vertical-align: middle;
                        white-space: nowrap;
                        mso-char-indent-count: 1;
                        padding-left: 7px;
                        background: auto;
                        mso-pattern: auto;
                        color: #FF0000;
                        font-size: 10pt;
                        font-weight: 400;
                        font-style: normal;
                        font-family: "宋体", "monospace";
                        border-top: 1px solid #808080;
                        border-right: 1px solid #BFBFBF;
                        border-bottom: 1px solid #BFBFBF;
                        border-left: 1px solid #BFBFBF;
                        mso-diagonal-down: none;
                        mso-diagonal-up: none;
                        mso-protection: locked visible;
                    }
                </style>
            </head>

            <body>
                <table border=0 cellpadding=0 cellspacing=0 style='border-collapse: 
            collapse;table-layout:fixed;'>
                    <tr height=20 style='mso-height-source:userset;height:12pt' id='r0'>
                        <td height=20 class='x26 x26_left' width=85 style='height:12pt;width:63.75pt;'>证券代码</td>
                        <td class=x27 width=85 >证券名称</td>
                        <td class=x28 width=85 >市盈率</td>
                        <td class=x28 width=85 >换手率</td>
                        <td class=x28 width=85 >当前价格</td>
                        <td class=x28 width=85 >当日涨幅</td>
                        <td class=x28 width=85 >提醒</td>
                        <td class=x28 >日线</td>
                    </tr>
                   '''+value+'''
                </table>
                <br/>
                <br/>
                <br/>
                <br/>
                <br/>
                <span><h3>©2018 秋刀鱼出品</h3></span>
                <br/>
                <span><h4>小姐姐有空约会吧~</h4></span>
            </body>

</html>'''

