# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ArbreEnvRacinaire(models.Model):
    _name = 'goeland.arbre_envracinaire'
    _inherit = 'goeland.liste_ordree'

    name = fields.Char(string='Root environment', required=True)

