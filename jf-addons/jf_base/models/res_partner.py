# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    eye_info_ids = fields.One2many('eye.info', 'partner_id', string='Eyes infos')
    eye_info_count = fields.Integer(compute='_compute_eye_info_count')
    type = fields.Selection(selection_add=[('shop', 'Shop')])
    finess_number = fields.Char(string='FINESS number')
    opening_date = fields.Date(string='Opening date')
    closing_date = fields.Date(string='Closing date')
    status = fields.Selection([('open', 'Open'), ('closed', 'Closed')], string='Shop status')
    opening_time = fields.Text(string='Opening days and hours')
    sales_area = fields.Float(string='Sales area')
    linear_area = fields.Float(string='Linear are')
    social_security_number = fields.Char(string='Social security number')

    @api.depends('eye_info_ids')
    def _compute_eye_info_count(self):
        for rec in self:
            rec.eye_info_count = len(rec.eye_info_ids)

