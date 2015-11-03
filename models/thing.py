# -*- coding: utf-8 -*-
from openerp import models, fields, api


class Thing(models.Model):
    _name = 'goeland.thing'

    name = fields.Char(string='Name', required=True)
    isactive = fields.Boolean(string='Active')
    description = fields.Char(string='Description')
    dateinactivation = fields.Datetime(string='Inctivation date')
    dateconstruction = fields.Datetime(string='Building date')
    ishavingstory = fields.Boolean(string='Ishavingstory')

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "The thing name must be unique"),
    ]

    def mafonctiondebase(self):
        return self.name
