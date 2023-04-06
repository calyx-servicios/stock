from odoo import models, fields, _
from odoo.exceptions import UserError

class StockPicking(models.Model):
    _inherit = 'stock.picking'


    cai_number = fields.Char(string='CAI Number', size=100)
    cot_number = fields.Char(string='COT Number', size=100)
    
    def button_validate(self):
        for rec in self:
            if not rec.cai_number or not rec.cot_number:
                raise UserError(_('Before validating please add the CAI or COT number'))
        return super(StockPicking, self).button_validate()