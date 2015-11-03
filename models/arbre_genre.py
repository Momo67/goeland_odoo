# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ArbreGenre(models.Model):
    _name = 'goeland.arbre_genre'

    name = fields.Char(string='Genus', required=True)
    idgoeland = fields.Integer(string='Id Goeland')
    sortorder = fields.Integer(string='Sort order', required=True)
    isactive = fields.Boolean(string='Is active', required=True)

