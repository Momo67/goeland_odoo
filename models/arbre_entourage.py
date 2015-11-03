# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ArbreEntourage(models.Model):
    _name = 'goeland.arbre_entourage'
    _inherit = 'goeland.liste_ordree'

    name = fields.Char(string='Entourage', required=True)

