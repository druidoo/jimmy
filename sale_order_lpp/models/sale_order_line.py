# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import _, api, fields, models
from odoo.exceptions import UserError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    lpp_code = fields.Char(string="LPP code")
    rss_amount = fields.Monetary(string="RSS Amount")

    @api.onchange('product_id')
    def product_id_change(self):
        res = super().product_id_change()
        if self.product_id:
            self.lpp_code = self.product_id.lpp_code
            self.rss_amount = self.product_id.rss_amount
        return res
