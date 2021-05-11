import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
import requests
from bs4 import BeautifulSoup


def send_email(e_address):
    response = requests.get("https://finance.yahoo.com/quote/GOOG/", timeout = 240)
    stock_content = BeautifulSoup(response.content,"html.parser")
    price = stock_content.find(class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").text
    price_change = stock_content.find(class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)").text
    message = price + ", " + price_change

    p = Path('templates\stock_sender.html')
    html = Template(p.read_text())
    email = EmailMessage()
    email['from'] = 'wonjoon8shin@gmail.com'
    email['to'] = e_address
    email['subject'] = "Today's Google Stocks"

    email.set_content(message)

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('wonjoon8shin@gmail.com', 'tlsdnjswns1~')
        smtp.send_message(email)
        print('done')