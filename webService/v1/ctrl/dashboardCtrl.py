#!/usr/bin/env python

# -*- coding: utf-8 -*-

from flask_restful import Resource, reqparse

import v1.service.dashboardService as dashboardServ


def api_fmt(code, msg, data, httpCode):
    return {"code": code, "msg": msg, "data": data}, httpCode


class System(Resource):

    def __init__(self):
        self.system = dashboardServ.SystemService()

    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('info', type=bool)
            parser.add_argument('stats', type=bool)
            args = parser.parse_args()
            res = dict()
            if args.get("info") is not None:
                res["info"] = self.system.get_sys_info()
            elif args.get("stats") is not None:
                res["stats"] = self.system.get_sys_stats()
            else:
                res["info"] = self.system.get_sys_info()
                res["stats"] = self.system.get_sys_stats()
            return api_fmt(0, "", res, 200)
        except Exception as exc1:
            return api_fmt(1, exc1, {}, 400)


class QuickEntry(Resource):

    def __init__(self):
        self.system = dashboardServ.SystemService()

    def get(self):
        try:
            res = self.system.get_quick_entry()
            print res
            return api_fmt(0, "", res, 200)
        except Exception as exc1:
            return api_fmt(1, exc1, {}, 400)
