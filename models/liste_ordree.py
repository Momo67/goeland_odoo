# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ListeOrdree(models.Model):
    _name = 'goeland.liste_ordree'

    name = fields.Char(string='Name', required=True)
    idgoeland = fields.Integer(string='Id Goeland')
    sortorder = fields.Integer(string='Sort order', required=True)
    isactive = fields.Boolean(string='Is active', required=True)

