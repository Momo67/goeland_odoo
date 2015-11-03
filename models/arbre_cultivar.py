# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ArbreCultivar(models.Model):
    _name = 'goeland.arbre_cultivar'

    name = fields.Char(string='Cultivar', required=True)
    idgoeland = fields.Integer(string='Id Goeland')
    sortorder = fields.Integer(string='Sort order', required=True)
    isactive = fields.Boolean(string='Is active', required=True)

