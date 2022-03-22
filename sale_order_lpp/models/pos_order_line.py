# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import _, api, fields, models
from odoo.exceptions import UserError


class PosOrderLine(models.Model):
    _inherit = "pos.order.line"

    lpp_code = fields.Char(string="LPP code", related="product_id.lpp_code")
    rss_amount = fields.Monetary(string="RSS Amount", related="product_id.rss_amount")
