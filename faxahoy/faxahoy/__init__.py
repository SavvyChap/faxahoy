"""
The flask application package.
"""

from flask import Flask
from flask_sqalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
db = SQLAlchemy(app)

import faxahoy.views
