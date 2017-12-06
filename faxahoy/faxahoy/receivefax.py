#!/usr/bin/env python
"""Fax snippet."""

from faxahoy import app
from flask import render_template, Flask, Response, request
from flask_mail import Mail, Message
from datetime import datetime
import requests

mail=Mail(app)

time = datetime.now().strftime("%Y%m%d_%I%M%p")

def ext7706(url, frm, fid):
    sender = frm
    incoming = url
    faxsid = fid
    fax = requests.get(incoming)
    media = 'media_' + time + '.pdf'
    path = 'fax/inbox7706/'
    with open('faxahoy/fax/inbox7706/' + media, 'wb') as f:
        f.write(fax.content)
    msg = Message(
            'Faxahoy!!!',
            sender='augustqmoney@gmail.com',
            recipients=['a.money@uspm.us'])
    msg.body = "You have received a fax from " + sender + "\n\n\n" + faxsid
    with app.open_resource(path + media) as fp:
        msg.attach(media, "application/pdf", fp.read())
    mail.send(msg)
    print(sender + "-> 7706")
    return 'sent...'

def ext7721(url, frm, fid):
    sender = frm
    incoming = url
    faxsid = fid
    fax = requests.get(incoming)
    media = 'media_' + time + '.pdf'
    path = 'fax/inbox7721/'
    with open('faxahoy/fax/inbox7721/' + media, 'wb') as f:
        f.write(fax.content)
    msg = Message(
            'Faxahoy!!!',
            sender='augustqmoney@gmail.com',
            recipients=['a.money@uspm.us'])
    msg.body = "You have received a fax from " + sender + "\n\n\n" + faxsid
    with app.open_resource(path + media) as fp:
        msg.attach(media, "application/pdf", fp.read())
    mail.send(msg)
    print(sender + "-> 7721")
    return 'sent...'

def ext7722(url, frm, fid):
    sender = frm
    incoming = url
    faxsid = fid
    fax = requests.get(incoming)
    media = 'media_' + time + '.pdf'
    path = 'fax/inbox7722/'
    with open('faxahoy/fax/inbox7722/' + media, 'wb') as f:
        f.write(fax.content)
    msg = Message(
            'Faxahoy!!!',
            sender='augustqmoney@gmail.com',
            recipients=['a.money@uspm.us'])
    msg.body = "You have received a fax from " + sender + "\n\n\n" + faxsid
    with app.open_resource(path + media) as fp:
        msg.attach(media, "application/pdf", fp.read())
    mail.send(msg)
    print(sender + "-> 7722")
    return 'sent...'

def ext7743(url, frm, fid):
    sender = frm
    incoming = url
    faxsid = fid
    fax = requests.get(incoming)
    media = 'media_' + time + '.pdf'
    path = 'fax/inbox7743/'
    with open('faxahoy/fax/inbox7743/' + media, 'wb') as f:
        f.write(fax.content)
    msg = Message(
            'Faxahoy!!!',
            sender='augustqmoney@gmail.com',
            recipients=['a.money@uspm.us'])
    msg.body = "You have received a fax from " + sender + "\n\n\n" + faxsid
    with app.open_resource(path + media) as fp:
        msg.attach(media, "application/pdf", fp.read())
    mail.send(msg)
    print(sender + "-> 7743")
    return 'sent...'

def ext7768(url, frm, fid):
    sender = frm
    incoming = url
    faxsid = fid
    fax = requests.get(incoming)
    media = 'media_' + time + '.pdf'
    path = 'fax/inbox7768/'
    with open('faxahoy/fax/inbox7768/' + media, 'wb') as f:
        f.write(fax.content)
    msg = Message(
            'Faxahoy!!!',
            sender='augustqmoney@gmail.com',
            recipients=['a.money@uspm.us'])
    msg.body = "You have received a fax from " + sender + "\n\n\n" + faxsid
    with app.open_resource(path + media) as fp:
        msg.attach(media, "application/pdf", fp.read())
    mail.send(msg)
    print(sender + "-> 7768")
    return 'sent...'

def ext7799(url, frm, fid):
    sender = frm
    incoming = url
    faxsid = fid
    fax = requests.get(incoming)
    media = 'media_' + time + '.pdf'
    path = 'fax/inbox7799/'
    with open('faxahoy/fax/inbox7799/' + media, 'wb') as f:
        f.write(fax.content)
    msg = Message(
            'Faxahoy!!!',
            sender='augustqmoney@gmail.com',
            recipients=['a.money@uspm.us'])
    msg.body = "You have received a fax from " + sender + "\n\n\n" + faxsid
    with app.open_resource(path + media) as fp:
        msg.attach(media, "application/pdf", fp.read())
    mail.send(msg)
    print(sender + "-> 7799")
    return 'sent...'

@app.route('/fax/sent', methods=['POST'])
def fax_sent():
    twiml = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Receive action="/fax/received"/>
</Response>
    """

    return Response(twiml, mimetype='text/xml')


@app.route('/fax/received', methods=['POST'])
def fax_received():
    sender = request.form.get('From')
    recipient = request.form.get('To')
    paper = request.form.get('MediaUrl')
    faxsid = request.form.get('FaxSid')

    if recipient == '+17132367706':
        ext7706(paper, sender, faxsid)
    elif recipient == '+17132367721':
        ext7721(paper, sender, faxsid)
    elif recipient == '+17132367722':
        ext7722(paper, sender, faxsid)
    elif recipient == '+17132367743':
        ext7743(paper, sender, faxsid)
    elif recipient == '+17132367768':
        ext7768(paper, sender, faxsid)
    elif recipient == '+17132367799':
        ext7799(paper, sender, faxsid)
    else:
        print("sorry, unrecognized number")

    return 'sent', 200

@app.route('/sendfax')
def sendfax():
    return render_template(
        'sendfax.jade',
        title='Send a Fax!'
    )
