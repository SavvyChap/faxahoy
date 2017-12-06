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
    print(sender + "->" + recipient)
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
    print(sender + "->" + recipient)
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
    print(sender + "->" + recipient)
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
    print(sender + "->" + recipient)
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
    print(sender + "->" + recipient)
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
    print(sender + "->" + recipient)
    return 'sent...'

@app.route('/fax/sent', methods=['POST'])
def fax_sent():
    twiml = """
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

<<<<<<< HEAD
    if sender == '+17132367706':
        ext7706(paper, sender, faxsid)
    elif sender == '+17132367721':
        ext7721(paper, sender, faxsid)
    elif sender == '+17132367722':
        ext7722(paper, sender, faxsid)
    elif sender == '+17132367743':
        ext7743(paper, sender, faxsid)
    elif sender == '+17132367768':
        ext7768(paper, sender, faxsid)
    elif sender == '+17132367799':
        ext7799(paper, sender, faxsid)
    else:
        print("sorry, unrecognized number")
=======
    time = datetime.now().strftime("%Y%m%d_%I%M%p")
    theFile = requests.get(paper)
    media = 'media_' + time + '.pdf'
    path = "fax\\inbox\\" ### set for windows environment. change to fax/inbox/ for linux, mac ###
    with open('faxahoy/fax/inbox/' + media, 'wb') as f:
        f.write(theFile.content)

    msg = Message(
            'Hello',
            sender='augustqmoney@gmail.com',
            recipients=['a.money@uspm.us'])
    msg.body = "You have received a fax from " + sender + "\n\n\n" + faxsid + "\n\n\n" + paper
    with app.open_resource(path + media) as fp:
        msg.attach(media, "application/pdf", fp.read())
    mail.send(msg)
    print(sender + "->" + recipient + "\n \n" + paper)
>>>>>>> 0a7426095366724e12e9f3c587d682dfbf8cb735

    return 'sent', 200

@app.route('/sendfax')
def sendfax():
    return render_template(
        'sendfax.jade',
        title='Send a Fax!'
    )
