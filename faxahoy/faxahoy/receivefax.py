#!/usr/bin/env python
"""Fax snippet."""

from faxahoy import app
from flaskext.mail import Mail, Message

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
    """ Will put email send function in here """
    msg = Message(
            'Hello',
            sender='augustqmoney@gmail.com',
            recipients=['a.money@uspm.us'])
    msg.body = "Hello world"
    mail.send(msg)
    print(request.form.get('MediaUrl'))

    return 'sent', 200