# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ArbreEtatSanitaireCouronne(models.Model):
    _name = 'goeland.arbre_etatsanitairecouronne'
    _inherit = 'goeland.liste_ordree'

    name = fields.Char(string='Health status of crown', required=True)

