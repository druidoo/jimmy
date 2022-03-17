# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PosConfig(models.Model):
    _inherit = 'pos.config'

    team_user_ids = fields.Many2many('res.users', store=False,
                                     compute='compute_team_user_ids',
                                     search='search_team_user_ids')

    @api.depends('crm_team_id')
    def compute_team_user_ids(self):
        for rec in self:
            rec.team_user_ids = rec.crm_team_id.member_ids

    def search_team_user_ids(self, operator, value):
        # need to do this workaround as filter doesn't work well
        if operator == 'in':
            user_crm_team = self.env['crm.team'].search([('member_ids',
                                                          'in', value)])
            return [('crm_team_id', operator, user_crm_team.ids)]
        return []