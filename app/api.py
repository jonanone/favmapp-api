# -*- coding: utf-8 -*-
from flask import request
from flask import make_response
from flask import jsonify
from models import Tag
from error_handler import InvalidUsage
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
        tags = Tag.get_all()
        return jsonify(tags=[
            tag.serialize for tag in tags
        ])
    if request.method == 'POST':
        name = request.args.get('name')
        description = request.args.get('description')
        tag = Tag.create(name=name,
                         description=description)
        return jsonify(tag=[tag.serialize]), 201


@app.route('/api/tags/<int:tag_id>', methods=['GET', 'PUT', 'DELETE'])
def tag_handler(tag_id):
    if request.method == 'GET':
        tag = Tag.get(tag_id)
        if tag is not None:
            return jsonify(tag=[tag.serialize])
        else:
            raise InvalidUsage('Not Found', status_code=404)
    if request.method == 'PUT':
        tag = Tag.get(tag_id)
        if tag is not None:
            name = request.args.get('name')
            description = request.args.get('description')
            updated_tag = tag.update(name, description)
            return jsonify(tag=[updated_tag.serialize])
        else:
            raise InvalidUsage('Not Found', status_code=404)
    if request.method == 'DELETE':
        tag = Tag.get(tag_id)
        if tag is not None:
            deleted = tag.delete()
            if deleted:
                return jsonify(status='OK')
            else:
                raise InvalidUsage('Unknown Error', status_code=520)
        else:
            raise InvalidUsage('Not Found', status_code=404)



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


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response