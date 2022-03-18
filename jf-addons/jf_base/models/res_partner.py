# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    eye_info_ids = fields.One2many('eye.info', 'partner_id', string='Eyes infos')
    eye_info_count = fields.Integer(compute='_compute_eye_info_count')
    type = fields.Selection(selection_add=[('shop', 'Shop'), ('ophthalmologist', 'Ophthalmologist')])

    @api.depends('eye_info_ids')
    def _compute_eye_info_count(self):
        for rec in self:
            rec.eye_info_count = len(rec.eye_info_ids)

