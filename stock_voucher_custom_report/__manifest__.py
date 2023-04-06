# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Stock Vouchers Custom Report",
    "summary": """
        This module adds the CAI and COT fields and also adds them to the report.
    """,
    "author": "Calyx Servicios S.A.",
    "maintainers": ["Zamora, Javier"],
    "website": "http://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    "category": "Technical Settings",
    "version": "11.0.1.0.0",
    "application": False,
    "installable": True,
    "depends": [
        "l10n_ar_aeroo_stock",
        "stock",
    ],
    "data": [
        "views/stock_picking.xml",
        "report/report.xml",
    ],
}
