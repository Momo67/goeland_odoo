# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ArbreChkEnvRacinaire(models.Model):
    _name = 'goeland.arbre_chkenvracinaire'
    _inherit = 'goeland.liste_ordree'

    name = fields.Char(string='Status', required=True)

