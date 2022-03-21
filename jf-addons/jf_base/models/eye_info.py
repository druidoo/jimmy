# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class EyeInfo(models.Model):
    _name = 'eye.info'
    _inherit = 'attachment.mixin'
    _description = 'Customer eye info'

    partner_id = fields.Many2one('res.partner', string='Customer', required=True)
    ophthalmologist_name = fields.Char(string="ophthalmologist name")
    ophthalmologist_code = fields.Char(related="ophthalmologist_id.ref", string="Ophthalmologist code", readonly=True)
    prescription_date = fields.Date(string="Prescription date", default=fields.Datetime.now)
    left_sphere = fields.Float(string='Left eye sphere')
    left_cylinder = fields.Float(string='Left eye cylinder')
    left_axis = fields.Float(string='Left eye axis')
    left_addition = fields.Float(string='Left eye addition')
    left_pupil_gap = fields.Float(string='Left eye pupillary gap')
    left_height = fields.Float(string='Left eye height')
    right_sphere = fields.Float(string='Right eye sphere')
    right_cylinder = fields.Float(string='Right eye cylinder')
    right_axis = fields.Float(string='Right eye axis')
    right_addition = fields.Float(string='Right eye addition')
    right_pupil_gap = fields.Float(string='Right eye pupillary gap')
    right_height = fields.Float(string='Right eye height')

    def name_get(self):
        return [(pre.id, '%s - %s - %s' % (_('Prescription'), pre.partner_id.name, pre.prescription_date)) for pre in
                self]
