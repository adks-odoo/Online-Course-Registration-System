from odoo import fields, models

class CourseRegistrationSystem(models.Model):
    _name = "course.reg"
    _description = "Course Registration System"

    name = fields.Char(required=True)
    description = fields.Text()
    course_id = fields.Char(string="Course ID")
    course_link = fields.Char()
    instructor = fields.Char()
    department_id = fields.Char(string="Department ID")
    students_enrolled = fields.Integer()
    price = fields.Integer()
