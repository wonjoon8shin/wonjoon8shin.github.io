from flask import Flask, render_template, url_for, request, redirect
import csv
import email_sender
import smtplib
from email.message import EmailMessage
from string import Template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')        

@app.route('/Google_Stock_Prediction.html')
def google_stock():
    return render_template('/Google_Stock_Prediction.html')

@app.route('/<string:page>')
def webpage(page):
    return render_template(page)

@app.route('/email_sent', methods = ['POST', 'GET'])
def stocks():
    if request.method == 'POST':
        data = request.form.to_dict() 
        email_sender.send_email(data["email"])
        return render_template('/thankyou.html')   

def save_data(data):
    with open('data.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def save_data_csv(data):
    with open('data.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods = ['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_data(data)
        save_data_csv(data)
        return redirect('/thankyou.html')
    else:
        'error'
