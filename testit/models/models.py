# -*- coding: utf-8 -*-

from odoo import models, fields, api
import odoo
import logging
_logger = logging.getLogger(__name__)
addonspath = odoo.tools.config['addons_path']
_logger.error('DEBUG ADDONSPATH: %s' % addonspath)
# class testit(models.Model):
#     _name = 'testit.testit'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
