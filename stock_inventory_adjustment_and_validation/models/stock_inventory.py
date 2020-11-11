# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, _
from odoo.exceptions import ValidationError


class Inventory(models.Model):
    _inherit = "stock.inventory"

    def action_done(self):
        for line in self.line_ids:
            if line.product_id.standard_price == 0.0:
                error_string = (
                    _(
                        "You cannot validate with product (%r) \
                     with standard price in 0.0"
                    )
                    % (line.product_id.display_name)
                )
                raise ValidationError(error_string)
        return super(Inventory, self).action_done()


class InventoryLine(models.Model):
    _inherit = "stock.inventory.line"

    def _get_move_values(self, qty, location_id, location_dest_id, out):
        res = super(InventoryLine, self)._get_move_values(
            qty, location_id, location_dest_id, out
        )
        if not out:
            res["is_in_inventory_adjustment"] = True
        return res
