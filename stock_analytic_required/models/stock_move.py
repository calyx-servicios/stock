from odoo import models, fields, api

class StockMove(models.Model):
    _inherit = "stock.move"
    
    @api.model_create_multi
    def create(self, vals_list):
        res = super(StockMove, self).create(vals_list)
        for line in res:
            line.analytic_tag_ids = line.sale_line_id.analytic_tag_ids
        return res

