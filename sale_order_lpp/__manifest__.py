# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sale Jimmy Fairly",
    "version": "15.0.1.0.1",
    "category": "Sales",
    "summary": "This module allows you to add custom field on sale order",
    "website": "https://github.com/OCA/product-pack",
    "author": "Arkeup",
    "license": "AGPL-3",
    "depends": ["sale"],
    "data": ["security/ir.model.access.csv",
             "views/product_template_views.xml",
             "views/sale_order_views.xml",
             "views/sale_report_template.xml",
             "views/res_users_views.xml",
             "views/res_company_views.xml",
             ],
    "installable": True,
}
