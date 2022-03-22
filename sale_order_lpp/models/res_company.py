# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import _, api, fields, models
from odoo.exceptions import UserError


class ResCompany(models.Model):
    _inherit = "res.company"

    signature = fields.Image('Signature',
                             copy=False,
                             attachment=True,
                             max_width=1024,
                             max_height=1024)
    signed_by = fields.Char('Signed By',
                            help='Name of the person that signed the SO.',
                            copy=False)
