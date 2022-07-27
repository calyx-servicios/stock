# pylint: disable=missing-module-docstring,pointless-statement
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{

    "name": "Inventory Adjusment",
    "summary": """
        This Module add the new_qty field and hide the location_id and product_uom_id fields in the Inventory form view.
    """,
    "author": "Calyx Servicios S.A.",
    "maintainers": ["<Github Username/s>"],
    "website": "https://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",

    "category": "Technical Settings",
    "version": "11.0.1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "depends": ["base","stock"],
    'data': [
        'views/stock_inventory_inherited_views.xml',
    ],

}
