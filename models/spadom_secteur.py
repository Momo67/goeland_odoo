# -*- coding: utf-8 -*-
from openerp import models, fields, api


class SPADOMSecteur(models.Model):
    _name = 'goeland.spadom_secteur'

    idthing = fields.Many2one(comodel_name='goeland.thing',
                              required=True,
                              ondelete='cascade',
                              string='Base object',
                              delegate=True)


