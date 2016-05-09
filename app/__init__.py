# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Initialization
app = Flask(__name__)
app.config.from_object('app.settings')
db = SQLAlchemy(app)

import api
