# -*- coding: utf-8 -*-
# from odoo import http

# class Addons/xestionSat/xestionSat(http.Controller):
#     @http.route('/addons/xestion_sat/xestion_sat/addons/xestion_sat/
# xestion_sat/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons/xestion_sat/xestion_sat/addons/xestion_sat/
# xestion_sat/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons/xestion_sat/xestion_sat.listing',
#  {
#             'root': '/addons/xestion_sat/xestion_sat/addons/xestion_sat/
# xestion_sat',
#             'objects': http.request.env['addons/xestion_sat/xestion_sat.
# addons/xestion_sat/xestion_sat'].search([]),
#         })

#     @http.route('/addons/xestion_sat/xestion_sat/addons/xestion_sat/
# xestion_sat/objects/<model("addons/xestion_sat/xestion_sat.addons/
# xestion_sat/xestion_sat"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons/xestion_sat/xestion_sat.object', {
#             'object': obj
#         })
