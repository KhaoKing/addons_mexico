{
    'name': "Project Module Inheritace",
    'category': 'Services/Project',
    'author': 'Leonardo Khaoim',
    'countries': ['mx'],
    'contributors': [
        'Leonardo Khaoim <LeoKhao2611@gmail.com>'
    ],
    'description': """
        This module adds a inheritace to the project module
    """,
    'depends': [
        'project',
    ],
    'data': [
        ## VIEWS ##
        'views/project_menu_actions_inherit.xml',
        'views/project_menus_inherit.xml',
    ],
    'application': True,
    'installable': True,
    "version": "1.0",
    "license": "OEEL-1",
}