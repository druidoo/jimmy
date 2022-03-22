# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import _, api, models, fields

class ProductTemplate(models.Model):
    _inherit = "product.template"

    lpp_code = fields.Char(string="LPP code")
    rss_amount = fields.Monetary(string="RSS Amount")


