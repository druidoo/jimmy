# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import _, api, fields, models
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    optimum_message = fields.Text(string="Optimum message")
    optimum_url = fields.Char(string="Optimum URL")
    optimum_state = fields.Selection(
        [("in_progress", "In progress"), ("done", "Done"), ("refused", "Refused")],
    )
