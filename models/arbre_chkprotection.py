# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ArbreChkProtection(models.Model):
    _name = 'goeland.arbre_chkprotection'
    _inherit = 'goeland.liste_ordree'

    name = fields.Char(string='Status', required=True)

