# -*- coding: utf-8 -*-
from odoo import http

# class Testituut(http.Controller):
#     @http.route('/testituut/testituut/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/testituut/testituut/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('testituut.listing', {
#             'root': '/testituut/testituut',
#             'objects': http.request.env['testituut.testituut'].search([]),
#         })

#     @http.route('/testituut/testituut/objects/<model("testituut.testituut"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('testituut.object', {
#             'object': obj
#         })