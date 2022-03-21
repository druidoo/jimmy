# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import Warning


class ResPartner(models.Model):
    _inherit = "res.partner"

    number_of_rates = fields.Integer(
        compute="_compute_rates_number", string="Number of rates", store=True
    )
    average_ratings = fields.Selection(
        [("0", "0"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")],
        compute="_compute_ratings",
        store=True,
    )

    last_rating = fields.Selection(
        [("0", "0"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")],
        compute="_compute_last_rating",
        store=True,
    )
    partner_review_ids = fields.One2many("customer.reviews", "partner_id")

    @api.depends("partner_review_ids.partner_id")
    def _compute_rates_number(self):
        for rec in self:
            partner_review_ids = self.env["customer.reviews"].search(
                [("partner_id", "=", rec.id)]
            )
            rec.number_of_rates = len(partner_review_ids)

    @api.depends("partner_review_ids.ratings", "partner_review_ids.partner_id")
    def _compute_last_rating(self):
        for rec in self:
            review_id = self.env["customer.reviews"].search(
                [("partner_id", "=", rec.id)], order="create_date", limit=1
            )

            rec.last_rating = review_id.ratings

    @api.depends("partner_review_ids.ratings", "partner_review_ids.partner_id")
    def _compute_ratings(self):
        for rec in self:
            reviews = self.env["customer.reviews"].search([("partner_id", "=", rec.id)])
            ratings = 0
            for review in reviews:
                if review.ratings != "0":
                    ratings = ratings + int(review.ratings)
            if ratings != 0:
                ratings = ratings / len(reviews)
            rec.average_ratings = str(int(ratings))

    def open_reviews(self):
        return {
            "name": "Customer Reviews",
            "view_mode": "tree,form",
            "res_model": "customer.reviews",
            "domain": [("partner_id", "=", self.id)],
            "type": "ir.actions.act_window",
            "target": "current",
        }

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def open_reviews(self):
        return {
            "name": "Customer Reviews",
            "view_mode": "tree,form",
            "res_model": "customer.reviews",
            "domain": [("partner_id", "=", self.partner_id.id)],
            "type": "ir.actions.act_window",
            "target": "current",
        }

    number_of_rates = fields.Integer(
        related="partner_id.number_of_rates", store=True
    )
    average_ratings = fields.Selection(
        [("0", "0"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")],
        related="partner_id.average_ratings", store=True
    )

class CustomerReview(models.Model):
    _name = "customer.reviews"
    _rec_name = 'partner_id'


    partner_id = fields.Many2one("res.partner", string="Customer", required=True)
    message = fields.Text(string="Message")
    ratings = fields.Selection(
        [("0", "0"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")],
        string="Ratings",
    )