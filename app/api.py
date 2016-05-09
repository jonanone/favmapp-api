# -*- coding: utf-8 -*-
from flask import request
from flask import make_response
from flask import jsonify
from . import app
import json


@app.route('/api', methods=['GET', 'POST'])
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


@app.route('/api/tags', methods=['GET', 'POST'])
def all_tags_handler():
    if request.method == 'GET':
        return jsonify(tags=[])
    if request.method == 'POST':
        return jsonify(tag=[]), 201


@app.route('/api/tags/<int:tag_id>', methods=['GET', 'PUT', 'DELETE'])
def tag_handler(tag_id):
    if request.method == 'GET':
        return jsonify(tag=[])
    if request.method == 'PUT':
        return jsonify(tag=[])
    if request.method == 'DELETE':
        return jsonify(status='OK')


@app.route('/api/points', methods=['GET', 'POST'])
def all_points_handler():
    if request.method == 'GET':
        return jsonify(points=[])
    if request.method == 'POST':
        return jsonify(point=[]), 201


@app.route('/api/points/<int:point_id>', methods=['GET', 'PUT', 'DELETE'])
def point_handler(point_id):
    if request.method == 'GET':
        return jsonify(point=[])
    if request.method == 'PUT':
        return jsonify(point=[])
    if request.method == 'DELETE':
        return jsonify(status='OK')
