# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ArbreGenre(models.Model):
    _name = 'goeland.arbre_genre'

    name = fields.Char(string='Genus', required=True)
    sortorder = fields.Integer(string='Sort order', required=True)
    isactive = fields.Boolean(string='Is active', required=True)

