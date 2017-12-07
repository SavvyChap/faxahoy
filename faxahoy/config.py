import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG=True

WTF_CSRF_ENABLED = True
SECRET_KEY = 'give-it-your-best-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

MAIL_SERVER='smtp-relay.gmail.com'
MAIL_PORT=587
MAIL_USE_TLS=True
## MAIL_USERNAME='----'
## MAIL_PASSWORD='----'
