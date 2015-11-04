# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ArbreChkEntourage(models.Model):
    _name = 'goeland.arbre_chkentourage'
    _inherit = 'goeland.liste_ordree'

    name = fields.Char(string='Status', required=True)

