# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Stock Analytic Required",
    "summary": """
        This module adds required status to analytic tags field
    """,
    "author": "Calyx Servicios S.A.",
    "maintainers": ["ParadisoCristian", "PerezGabriela"],
    "website": "http://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    "category": "Stock",
    "version": "13.0.2.0.0",
    "depends": [
        "stock_analytic"
    ],
    "data": [
        'views/stock_move_views.xml',
    ],
}