# Copyright 2013-2018 Open Architects Consulting SPRL.
# Copyright 2018-Coop IT Easy SC (<http://www.coopiteasy.be>)
# - Houssine BAKKALI - <houssine@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Cooperators Website",
    "version": "15.0.1.0.0",
    "depends": [
        "cooperator",
        "website",
    ],
    "author": "Coop IT Easy SC, Odoo Community Association (OCA)",
    "category": "Cooperative management",
    "website": "https://github.com/OCA/cooperative",
    "license": "AGPL-3",
    "summary": """
    This module adds the cooperator subscription form
    allowing to subscribe for shares online.
    """,
    "data": [
        "views/subscription_template.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "cooperator_website/static/src/js/*.js",
        ],
    },
    "application": True,
}
