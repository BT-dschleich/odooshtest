# -*- coding: utf-8 -*-

from odoo import models, fields, api
import odoo
import logging
_logger = logging.getLogger(__name__)
addonspath = odoo.tools.config['addons_path']
_logger.info('DEBUG TESTITUUUUT ADDONSPATH: %s' % addonspath)

# class testit(models.Model):

# class testituut(models.Model):
#     _name = 'testituut.testituut'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
