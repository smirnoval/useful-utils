#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders
import os
from bs4 import BeautifulSoup
from urllib2 import urlopen
from fpdf import FPDF
from copy import deepcopy


BASE_NEWS_URL = 'http://ria.ru/'
FILEPATH = "/path/to/news.pdf"
SUBJECT = "News"
SEND_TO = "name@someMail.com"
USER_NAME = "yourName@someMail.com"
USER_PASSWORD = "yourPassword"
SERVER = "smtp.gmail.com"
PORT = 25

def send_email(FILEPATH, SEND_TO, SUBJECT ):
    basename = os.path.basename(FILEPATH)
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(FILEPATH,"rb").read() )
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % basename)
    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT
    msg['From'] = USER_NAME
    msg['To'] = SEND_TO
    msg.attach(part)
    s = smtplib.SMTP(SERVER, PORT)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(USER_NAME, USER_PASSWORD)
    s.sendmail(USER_NAME, SEND_TO, msg.as_string())
    s.quit()


def make_PDF(dict):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    for i in range(len(dict)):
        pdf.set_font('DejaVu', '', 40)
        pdf.cell(40, 10, '*'*30 , 0, 1)
        header_text = dict[i]['header']
        pdf.multi_cell(0, 15, header_text)
        pdf.cell(40, 10, '-'*30 , 0, 1)
        pdf.set_font('DejaVu', '', 20)
        content_text = dict[i]['text']  #.decode('utf-8')
        pdf.multi_cell(0, 10, content_text)
    pdf.output('news.pdf', 'F')


def get_news_links():
    news_links = []
    html = urlopen(BASE_NEWS_URL).read()
    soup = BeautifulSoup(html, "lxml")
    data = soup.findAll(name = "div", class_="b-index__popular-item" )
    for div in data:
        links = div.findAll('a')
        news_links += [a['href'] for a in links if a['href'] != '/lenta/']
    return news_links


def get_news_information(url):
    news_information = {}
    html = urlopen('http://ria.ru/'+url).read()
    soup = BeautifulSoup(html, "lxml")
    data = soup.find(name = "h1", class_="b-article__title" )
    news_information['header'] = data.text
    data_content = soup.find(name = "div", class_="b-article__body" )
    content = data_content.findAll("p")
    text = ''.join(i.text for i in content)
    news_information['text'] = text
    return news_information


if __name__ == '__main__':
    news_links = get_news_links()
    news_dict = {}
    a = 0
    for i in news_links:
        news_dict[a] = get_news_information(i)
        a += 1
    make_PDF(news_dict)
    send_email(FILEPATH, SEND_TO, SUBJECT)