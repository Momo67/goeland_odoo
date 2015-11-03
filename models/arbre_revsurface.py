# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ArbreRevSurface(models.Model):
    _name = 'goeland.arbre_revsurface'
    _inherit = 'goeland.liste_ordree'

    name = fields.Char(string='Coating surface', required=True)

