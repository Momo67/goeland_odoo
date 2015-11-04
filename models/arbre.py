# -*- coding: utf-8 -*-
from openerp import models, fields, api


class Arbre(models.Model):
    _name = 'goeland.arbre'
    # _inherits = {'goeland.thing': 'idthing'}

    idthing = fields.Many2one(comodel_name='goeland.thing',
                              required=True,
                              ondelete='cascade',
                              string='Base object',
                              delegate=True)
    # thing_ids = fields.One2many(comodel_name='goeland.thing', inverse_name='id', required=True, ondelete='cascade')
    validation = fields.Selection([('existant', 'Existant'),('supprime', 'Supprimé'),('reposition', 'A repositionner'),
                                   ('replant', 'A replanter'),('waitcare', 'En attente de soin'),('waitfelling', 'En attente d''abattage'),
                                   ('wait replacement', 'En attente de remplacement')], string='Validation', required=True)
    genre_id = fields.Many2one(comodel_name='goeland.arbre_genre',
                               ondelete='set null',
                               string='Genus',
                               index=True)
    espece_id = fields.Many2one(comodel_name='goeland.arbre_espece',
                               ondelete='set null',
                               string='Specie',
                               index=True)
    cultivar_id = fields.Many2one(comodel_name='goeland.arbre_cultivar',
                               ondelete='set null',
                               string='Cultivar',
                               index=True)
    circonference = fields.Float(string='Circonference', help='Circumference in meters')
    diametrecouronne = fields.Selection([('', '')], string='Crown diameter')
    hauteur = fields.Selection([('', '')], string='Height')
    envracinaire_id = fields.Many2one(comodel_name='goeland.arbre_envracinaire',
                                      string='Root environment')
    chkenvracinaire_id = fields.Many2one(comodel_name='goeland.arbre_chkenvracinaire',
                                         string='Status of root environment')
    envracinairerem = fields.Char(string='Comment on root environment')
    substrat_id = fields.Many2one(comodel_name='goeland.arbre_substrat',
                                  string='Substratum')
    chksubstrat_id = fields.Many2one(comodel_name='goeland.arbre_chksubstrat',
                                     string='Status of substratum')
    substratrem = fields.Char(string='Comment on substratum')
    entourage_id = fields.Many2one(comodel_name='goeland.arbre_entourage',
                                   string='Entourage')
    chkentourage_id = fields.Many2one(comodel_name='goeland.arbre_chkentourage',
                                      string='Status of entourage')
    entouragerem = fields.Char(string='Comment on entourage')
    revsurface_id = fields.Many2one(comodel_name='goeland.arbre_revsurface',
                                    string='Coating surface')
    chkrevsurface_id = fields.Many2one(comodel_name='goeland.arbre_chkrevsurface',
                                       string='Status of coating surface')
    revsurfacerem = fields.Char(string='Comment on coating surface')
    protection_id = fields.Many2one(comodel_name='goeland.arbre_protection',
                                    string='Protection')
    chkprotection_id = fields.Many2one(comodel_name='goeland.arbre_chkprotection',
                                       string='Status of protection')
    protectionrem = fields.Char(string='Comment on protection')
    etatsanitairepied_id = fields.Many2one(comodel_name='goeland.arbre_etatsanitairepied',
                                           string='Health status of foot')
    etatsanitairetronc_id = fields.Many2one(comodel_name='goeland.arbre_etatsanitairetronc',
                                            string='Health status of trunk')
    etatsanitairecouronne_id = fields.Many2one(comodel_name='goeland.etatsanitairecouronne',
                                               string='Health status of crown')
    datereleve = fields.Datetime(string='Statement date')
    anneeplantation = fields.Char(size=4, string='Seeding year')
    isincada = fields.Boolean(string='Is in cadastre')
    tobecontrolled = fields.Boolean(string='To be controlled')
    tobechecked_id = fields.Many2one(comodel_name='goeland.arbre_tobechecked', string='Tobechecked')

    secteur = fields.Many2one(comodel_name='goeland.spadom_secteur', string='SPADOM sector')
    emplacement = fields.Many2one(comodel_name='goeland.spadom_emplacement', string='SPADOM location')

    # @api.onchange('validation')
    # def _verify_validation(self):
    #     if self.validation != 'existant':
    #         return {
    #             'warning': {
    #                 'title': "Wrong value for validation",
    #                 'message': "Change validation value for object with parent %s" % self.idthing.mafonctiondebase()
    #             },
    #         }

