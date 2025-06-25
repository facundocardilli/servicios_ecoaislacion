from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Obra(models.Model):
    _name = 'obras.obra'
    _description = 'Obra de aislamiento'

    name = fields.Char(string='Nombre', required=True)
    direccion = fields.Char(string='Dirección', required=True)
    cliente_id = fields.Many2one('res.partner', string='Cliente', required=True)
    presupuesto_id = fields.Many2one('sale.order', string='Presupuesto', required=True)
    status = fields.Selection([
        ('activa', 'Activa'),
        ('finalizada', 'Finalizada'),
        ('pendiente', 'Pendiente'),
        ('cancelada', 'Cancelada')
    ], string='Estado', default='pendiente', required=True)
    tiempo_traslado = fields.Float(string='Tiempo de traslado (horas)')
    metros_aplicar = fields.Float(string='Metros a aplicar (m²)')
    espesor = fields.Float(string='Espesor (cm)')
    altura_maxima = fields.Float(string='Altura máxima (m)')
    registro_diario_ids = fields.One2many(
        'obras.registro_diario',
        'obra_id',
        string='Registros Diarios',
    )

    @api.constrains('direccion', 'status')
    def _check_obra_activa_unica_por_direccion(self):
        for record in self:
            if record.status == 'activa':
                otras = self.search([
                    ('direccion', '=', record.direccion),
                    ('status', '=', 'activa'),
                    ('id', '!=', record.id)
                ])
                if otras:
                    raise ValidationError('Solo puede haber una obra activa por dirección.')
