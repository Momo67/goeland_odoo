# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ArbreSubstrat(models.Model):
    _name = 'goeland.arbre_substrat'
    _inherit = 'goeland.liste_ordree'

    name = fields.Char(string='Substratum', required=True)

