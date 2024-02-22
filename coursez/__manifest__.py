{
    'name': "coursez",
    'version': '1.0',
    'depends': ['base','mail'],
    'data': ['security/ir.model.access.csv',
             'views/course_reg_views.xml',
             'views/course_reg_student_views.xml',
             'views/course_menus.xml'],
    'installable': True,
    'application': True,
}
