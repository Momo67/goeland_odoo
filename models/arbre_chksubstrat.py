# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ArbreChkSubstrat(models.Model):
    _name = 'goeland.arbre_chksubstrat'
    _inherit = 'goeland.liste_ordree'

    name = fields.Char(string='Status', required=True)

