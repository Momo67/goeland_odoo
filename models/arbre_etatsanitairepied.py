# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ArbreEtatSanitairePied(models.Model):
    _name = 'goeland.arbre_etatsanitairepied'
    _inherit = 'goeland.liste_ordree'

    name = fields.Char(string='Health status of foot', required=True)

