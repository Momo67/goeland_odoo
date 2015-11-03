# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ArbreProtection(models.Model):
    _name = 'goeland.arbre_protection'
    _inherit = 'goeland.liste_ordree'

    name = fields.Char(string='Protection', required=True)

