from odoo import models,fields,api

class Account(models.Model):
    _inherit = 'account.move'
    description = 'account'

    entreprise_souscription = fields.Many2one('souscripteur.souscripteur',string='Entreprise souscripteur',required=True)
    taux_charge = fields.Integer(string='taux prise en charge',required=True)
    part_assureur = fields.Float(string='part assureur',required=True)
    part_assuré = fields.Float(string='part assuré',required=True)
    prise_charge = fields.Boolean(string='Prise en Charge')


class ResPartner(models.Model):
    _inherit = 'res.partner'
    description = 'res.partner'

    num_police = fields.Char(string='numéro de police', required=True)
    souscripteur_id = fields.Many2one('souscripteur.souscripteur',string='souscripteur',required=True)

class souscripteur(models.Model):
    _name = 'souscripteur.souscripteur'
    _rec_name='matricule_souscripteur'
    description = 'souscripteur'

    matricule_souscripteur = fields.Char(string='nom du souscripteur',required=True)
    assureur_ids = fields.Many2many('assureur.assureur',string='Assureur')
    nom_souscripteur = fields.Char(required=True)
    situa_geo_souscripteur = fields.Char(string='situation géographique',required=True)

class assureur(models.Model):
    _name = 'assureur.assureur'
    description = 'assureur'

    name= fields.Char(string='nom assureur')




