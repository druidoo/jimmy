# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class EyeInfo(models.Model):
    _name = 'eye.info'
    _description = 'Customer eye info'

    partner_id = fields.Many2one('res.partner', string='Customer')
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
    attachment_id = fields.Many2one('ir.attachment', string='Prescription')
    attachment_name = fields.Char(string='Prescription name')
    attachment_file = fields.Binary(compute='compute_attachment_file',
                                    inverse='set_attachment_id')

    @api.depends('attachment_id')
    def compute_attachment_file(self):
        for rec in self:
            rec.attachment_file = rec.attachment_id.datas

    def set_attachment_id(self):
        for rec in self:
            if not rec.attachment_id:
                rec.attachment_id = rec._create_prescription_attachment()
            else:
                if not rec.attachment_file:
                    rec.attachment_id.unlink()
                else:
                    rec.attachment_id.datas = rec.attachment_file
                    rec.attachment_id.name = rec.attachment_name

    def action_open_prescription(self):
        self.ensure_one()
        return {
            "name": _('Prescription'),
            "type": "ir.actions.act_window",
            "res_model": 'ir.attachment',
            "views": [(self.env.ref('jf_base.pdf_attachment_view_form').id,
                       "form")],
            "view_mode": "form",
            "res_id": self.attachment_id.id,
            "target": "new",
        }

    def _create_prescription_attachment(self):
        self.ensure_one()
        attachment_id = self.env['ir.attachment'].create({
            'name': self.attachment_name,
            'datas': self.attachment_file,
            'type': 'binary',
            'res_model': self._name,
            'res_id': self.id,
        })
        return attachment_id
