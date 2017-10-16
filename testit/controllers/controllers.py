# -*- coding: utf-8 -*-
from odoo import http

# class Testit(http.Controller):
#     @http.route('/testit/testit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/testit/testit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('testit.listing', {
#             'root': '/testit/testit',
#             'objects': http.request.env['testit.testit'].search([]),
#         })

#     @http.route('/testit/testit/objects/<model("testit.testit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('testit.object', {
#             'object': obj
#         })