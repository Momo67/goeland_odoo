# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ArbreValidation(models.Model):
    _name = 'goeland.arbre_validation'
    _inherit = 'goeland.liste_ordree'

    name = fields.Char(string='Validation', required=True)

