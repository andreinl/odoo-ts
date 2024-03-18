# © 2024 Andrei Levin <andrei.levin@codebeex.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    ts_export_id = fields.Many2one(comodel_name='exportts.export.registry', string="TS Export", required=False, )
