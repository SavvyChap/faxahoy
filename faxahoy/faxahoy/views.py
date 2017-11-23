"""
Routes and views for the flask application.
"""

from datetime import datetime
from pip._vendor.requests.status_codes import title
from flask import render_template
from faxahoy import app
from .forms import LoginForm

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.jade',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.jade',
                           title='Login',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS']
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.jade',
        title='About',
        year=datetime.now().year,
        message='a description of faxahoy!'
    )
