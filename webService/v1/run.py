#!/usr/bin/env python

# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api

from resource import api_resource

app = Flask(__name__)
api = Api(app)


def resource_register(resource):
    for k, v in resource.iteritems():
        api.add_resource(k, v)


def run(ip, port, threaded=True, debug=False):
    resource_register(api_resource)
    app.run(ip, port, threaded=threaded, debug=debug)
