#!/usr/bin/env python
"""Fax snippet."""

from faxahoy import app
from flask import render_template, Flask, Response, request
from flask_mail import Mail, Message
from datetime import datetime
import requests

mail=Mail(app)

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

    time = datetime.now().strftime("%Y%m%d_%I%M%p")
    theFile = requests.get(paper)
    media = 'media_' + time + '.pdf'
    path = "fax\\inbox\\"
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

    return 'sent', 200

@app.route('/sendfax')
def sendfax():
    return render_template(
        'sendfax.jade',
        title='Send a Fax!'
    )