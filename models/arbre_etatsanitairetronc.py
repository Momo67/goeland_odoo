# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ArbreEtatSanitaireTronc(models.Model):
    _name = 'goeland.arbre_etatsanitairetronc'
    _inherit = 'goeland.liste_ordree'

    name = fields.Char(string='Health status of trunk', required=True)

