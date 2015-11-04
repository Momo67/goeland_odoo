# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ArbreTobeChecked(models.Model):
    _name = 'goeland.arbre_tobechecked'
    _inherit = 'goeland.liste_ordree'

    name = fields.Char(string='To be checked', required=True)

