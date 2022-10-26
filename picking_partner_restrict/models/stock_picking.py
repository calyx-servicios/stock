import logging
import json
from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)


class StockPicking(models.Model):
    _inherit = "stock.picking"

    partner_domain = fields.Char(default=json.dumps([('id','!=',False)]), compute="_compute_partner_domain")

    def _compute_partner_domain(self):
        for picking in self:
            partner_domain = [("id", "!=", False)]
            if picking.sale_id:
                partner_domain = [
                    "|",
                    ("id", "=", picking.sale_id.partner_id.id),
                    ("id", "child_of", picking.sale_id.partner_id.id),
                ]
            picking.partner_domain = json.dumps(partner_domain)
