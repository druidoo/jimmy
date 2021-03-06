# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PosOrder(models.Model):
    _name = 'pos.order'
    _inherit = ['pos.order', 'attachment.mixin']

    use_last_eye_info = fields.Boolean(string='Use last eye info')
    left_sphere = fields.Float(string='Left eye sphere', copy=False)
    left_cylinder = fields.Float(string='Left eye cylinder', copy=False)
    left_axis = fields.Float(string='Left eye axis', copy=False)
    left_addition = fields.Float(string='Left eye addition', copy=False)
    left_pupil_gap = fields.Float(string='Left eye pupillary gap', copy=False)
    left_height = fields.Float(string='Left eye height', copy=False)
    right_sphere = fields.Float(string='Right eye sphere', copy=False)
    right_cylinder = fields.Float(string='Right eye cylinder', copy=False)
    right_axis = fields.Float(string='Right eye axis', copy=False)
    right_addition = fields.Float(string='Right eye addition', copy=False)
    right_pupil_gap = fields.Float(string='Right eye pupillary gap', copy=False)
    right_height = fields.Float(string='Right eye height', copy=False)
    with_prescription = fields.Boolean(string="With prescription", default=False)
    ophthalmologist_name = fields.Char(string="Ophthalmologist name")
    ophthalmologist_code = fields.Char(string="Ophthalmologist code")
    prescription_date = fields.Date(string="Prescription date", copy=False)

    @api.onchange('partner_id', 'use_last_eye_info')
    def _onchange_partner_id_eye(self):
        for rec in self:
            last_info = self.env['eye.info'].search([('partner_id', '=', rec.partner_id.id)], limit=1,
                                                    order='prescription_date desc, id desc')
            if last_info and rec.use_last_eye_info:
                rec.left_sphere = last_info.left_sphere
                rec.left_cylinder = last_info.left_cylinder
                rec.left_axis = last_info.left_axis
                rec.left_addition = last_info.left_addition
                rec.left_pupil_gap = last_info.left_pupil_gap
                rec.left_height = last_info.left_height
                rec.right_sphere = last_info.right_sphere
                rec.right_cylinder = last_info.right_cylinder
                rec.right_axis = last_info.right_axis
                rec.right_addition = last_info.right_addition
                rec.right_pupil_gap = last_info.right_pupil_gap
                rec.right_height = last_info.right_height
                rec.ophthalmologist_name = last_info.ophthalmologist_name
                rec.prescription_date = last_info.prescription_date
                rec.attachment_id = last_info.attachment_id
                rec.attachment_name = last_info.attachment_name
                rec.ophthalmologist_code = last_info.ophthalmologist_code

    @api.model
    def _process_order(self, order, draft, existing_order):
        res = super(PosOrder, self)._process_order(order, draft, existing_order)
        if not existing_order:
            order_id = self.browse(res)
            order_id._onchange_partner_id_eye()
        return res
