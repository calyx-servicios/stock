# pylint: disable=missing-module-docstring,pointless-statement
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Print control",
    "summary": """
        This module allow the user to have control over the printed stock reports
    """,
    "author": "Calyx Servicios S.A.",
    "maintainers": ["<lucianobaleani>"],
    "website": "https://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    "category": "Technical Settings",
    "version": "11.0.1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "depends": ["stock"],
    'data': [
        'views/stock_picking_inherited_views.xml',
    ],
}
