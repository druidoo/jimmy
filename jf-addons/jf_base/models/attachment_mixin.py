# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields


class AttachmentMixin(models.AbstractModel):
    _name = 'attachment.mixin'
    _description = 'Attachment Mixin'

    attachment_id = fields.Many2one('ir.attachment', string='Prescription')
    attachment_name = fields.Char(string='Prescription name')
    attachment_file = fields.Binary(compute='compute_attachment_file', inverse='set_attachment_id')

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