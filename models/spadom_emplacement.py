# -*- coding: utf-8 -*-
from openerp import models, fields, api


class SPADOMEmplacement(models.Model):
    _name = 'goeland.spadom_emplacement'

    idthing = fields.Many2one(comodel_name='goeland.thing',
                              required=True,
                              ondelete='cascade',
                              string='Base object',
                              delegate=True)


