from odoo import models, fields, api


class StockInventoryLine(models.Model):
    _inherit = "stock.inventory.line"

    new_qty = fields.Float(string="New Quantity")


    @api.depends('theoretical_qty','new_qty')
    def _quantity_update(self):
        for record in self:
            quantity = record.theoretical_qty + record.new_qty
            record.update({"product_qty":quantity})


    @api.onchange('theoretical_qty',"new_qty")
    def onchange_quantity_update(self):
        for record in self:
            quantity = record.theoretical_qty + record.new_qty
            record.update({"product_qty":quantity})
