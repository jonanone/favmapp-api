# -*- coding: utf-8 -*-
from flask import Flask

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Initialization
app = Flask(__name__)
app.config.from_object('app.settings')

import api
