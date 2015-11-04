# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ArbreChkRevSurface(models.Model):
    _name = 'goeland.arbre_chkrevsurface'
    _inherit = 'goeland.liste_ordree'

    name = fields.Char(string='Status', required=True)

