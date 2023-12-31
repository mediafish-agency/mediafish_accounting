from odoo import models, fields, api, _

class Currency(models.Model):
    _inherit = "res.currency"

    full_name = fields.Char(string='Name', translate=True)
    currency_unit_label = fields.Char(string="Currency Unit", translate=True)
    currency_subunit_label = fields.Char(string="Currency Subunit", translate=True)
    symbol = fields.Char(help="Currency sign, to be used when printing amounts.", required=True, translate=True)