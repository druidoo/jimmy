# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = ['sale.order', 'attachment.mixin']

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
    def create(self, values):
        rec = super(SaleOrder, self).create(values)
        if not rec.use_last_eye_info and rec.with_prescription:
            self.env['eye.info'].create({
                "partner_id": rec.partner_id.id,
                "left_sphere": rec.left_sphere,
                "left_cylinder": rec.left_cylinder,
                "left_axis": rec.left_axis,
                "left_addition": rec.left_addition,
                "left_pupil_gap": rec.left_pupil_gap,
                "left_height": rec.left_height,
                "right_sphere": rec.right_sphere,
                "right_cylinder": rec.right_cylinder,
                "right_axis": rec.right_axis,
                "right_addition": rec.right_addition,
                "right_pupil_gap": rec.right_pupil_gap,
                "right_height": rec.right_height,
                "ophthalmologist_name": rec.ophthalmologist_name,
                "ophthalmologist_code": rec.ophthalmologist_code,
                "prescription_date": rec.prescription_date,
                "attachment_id": rec.attachment_id.id,
                "attachment_name": rec.attachment_name,
            })
        return rec

    @api.constrains('use_last_eye_info', 'with_prescription')
    def _check_customer_prescription(self):
        for rec in self:
            if rec.use_last_eye_info and rec.with_prescription:
                last_info = self.env['eye.info'].search([('partner_id', '=', rec.partner_id.id)], limit=1,
                                                        order='prescription_date desc, id desc')
                if not last_info:
                    raise UserError(_("The customer %s doesn't have any prescriptions, please uncheck 'Use last "
                                      "prescription info'") % rec.partner_id.name)
