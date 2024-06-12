# -*- coding: utf-8 -*-
{
    'name': 'Base Vietnam Address',
    'summary': """This is the Vietnamese address module based on Circular No 124/2004/QĐ-TTg issued by Viet Nam Government""",
    'description': """""",
    'author': "Long Duong Nhat",
    'license': "LGPL-3",
    'category': 'Hidden',
    'version': '17.0.1.0',
    'application': False,
    'installable': True,
    'images': ['static/description/thumbnail.png'],
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'data/res_country_state_data.xml',
        'data/res.country.district.csv',
        'data/res.country.ward.csv',
        'views/res_country_district_views.xml',
        'views/res_country_ward_views.xml',
        'views/res_partner_views.xml',
        'views/res_company_views.xml',
        'views/menus.xml'
    ],
}
