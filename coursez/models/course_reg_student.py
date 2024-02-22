from odoo import fields, models

class CourseRegistrationStudent(models.Model):
    _name = "course.reg.student"
    _description = "Course Registration Student"

    name = fields.Char(required=True,string="Full Name")
    student_id = fields.Char(required=True,string="Student ID")
    email = fields.Char(required=True)
    contact_no = fields.Char(required=True)
    grade_level = fields.Char()
    registered_courses = fields.Integer()
