"""
The flask application package.
"""

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

import faxahoy.views
