# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class HrEmployeeInherit(models.Model):
    _inherit = "hr.employee"

    military_certificate = fields.Binary()


