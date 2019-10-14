from flask import Flask, render_template, request, make_response
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "hi"

@app.route('/api', methods=['POST'])
def index():
    print (request.form['param'])
    response = make_response(json.dumps('Done!'))
    response.headers['Access-Control-Allow-Origin'] = '*'
    sendMail(request.form['param'])
    return(response)

import smtplib, ssl
from email.message import EmailMessage
def sendMail(name):
    # print('Yo we got here', name)
    smtp_server = "smtp.mail.yahoo.com"
    sender_email = ""
    receiver_email = ''
    password = ''

    message = EmailMessage()
    message['Subject'] = '[vitadesignsco.com] - Contact Inquiry: #0001 Greetings!'
    message['From'] = sender_email
    message['To'] = receiver_email
    message.set_content('This is plain text content. (If this is ever seen there is a major problem.')
    message.add_alternative(f"""A customer has just contacted you from vitadesignsco.com. Here is the contents of their message:<br><br>
        Full Name: {name}<br>
        Email Address: <br>
        Phone Number: <br>
        Company: <br>
        Project Description: <br><br>
        [This is an automated e-mail from vitadesignsco.com.]""", subtype='html')
    try:
        with smtplib.SMTP_SSL(smtp_server, 465) as smtp:
            smtp.login(sender_email, password)
            smtp.send_message(message)
    except Exception as e:
        print(e)
    return

# sendMail('X')

if __name__ == "__main__":
    app.run()