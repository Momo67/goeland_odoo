# -*- coding: utf-8 -*-
from openerp import models, fields, api


class Thing(models.Model):
    _name = 'goeland.thing'

    name = fields.Char(string='Name', required=True)
    isactive = fields.Boolean(string='Active', required=True)
    description = fields.Char(string='Description', required=True)
    dateinactivation = fields.Datetime(string='Inctivation date')
    dateconstruction = fields.Datetime(string='Building date')
    ishavingstory = fields.Boolean(string='IsHavingStory')

    def mafonctiondebase(self):
        return self.name
