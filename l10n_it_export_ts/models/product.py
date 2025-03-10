##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2016 luca Vercelli
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import models, fields, api

# see /usr/lib/python2.7/dist-packages/openerp/addons/product/product.py


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    tipo_spesa_730 = fields.Selection([
        ('TK', 'Ticket'),
        ('FC', 'Farmaco, anche omeopatico'),
        ('FV', 'Farmaco per uso veterinario'),
        ('SV', 'Spese veterinarie'),
        ('SP', 'Prestazioni sanitarie'),
        ('AD', 'Acquisto o affitto dispositivo medico CE'),
        ('AS', 'ECG, spirometria, Holter pressorio e cardiaco, test, ...'),
        ('SR', 'Assistenza specialistica ambulatoriale'),
        ('CT', 'Cure termali'),
        ('PI', 'Protesica e integrativa'),
        ('IC', 'Chirurgia estetica e medicina estetica'),
        ('AA', 'Altre spese'),
    ], default="SP")
