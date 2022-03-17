# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    use_last_eye_info = fields.Boolean(string='Use last eye info',
                                       default=True)
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

    @api.onchange('partner_id', 'use_last_eye_info')
    def _onchange_partner_id_eye(self):
        for rec in self:
            last_info = self.env['eye.info'].search([('partner_id', '=',
                                                      rec.partner_id.id)],
                                                    limit=1,
                                                    order='create_date desc')
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

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for rec in self:
            #todo add condition to create an eye info
            if not rec.use_last_eye_info:
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
                })
        return res
