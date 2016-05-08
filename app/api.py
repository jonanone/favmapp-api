# -*- coding: utf-8 -*-
from flask import request
from flask import make_response
from . import app
import json


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        response = make_response(json.dumps('Hello this is the Favmapp API'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    if request.method == 'POST':
        response = make_response(json.dumps('Hello, you successfully sent a '\
                                            + 'POST to Favmapp API'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
