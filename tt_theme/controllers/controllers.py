# -*- coding: utf-8 -*-
from odoo import http

# class TtTheme(http.Controller):
#     @http.route('/tt_theme/tt_theme/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tt_theme/tt_theme/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tt_theme.listing', {
#             'root': '/tt_theme/tt_theme',
#             'objects': http.request.env['tt_theme.tt_theme'].search([]),
#         })

#     @http.route('/tt_theme/tt_theme/objects/<model("tt_theme.tt_theme"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tt_theme.object', {
#             'object': obj
#         })