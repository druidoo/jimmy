# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class EyeInfo(models.Model):
    _inherit = 'eye.info'

    def _create_prescription_attachment(self):
        res = super(EyeInfo, self)._create_prescription_attachment()
        self.env['documents.document'].create({
            'owner_id': self.env.user.id,
            'folder_id': self.env.ref(
                'jf_documents.documents_prescription_folder').id,
            'name': self.attachment_name,
            'attachment_id': res.id

        })
        return res
