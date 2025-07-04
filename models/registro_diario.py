from odoo import models, fields, api

class RegistroMaterial(models.Model):
    _name = 'obras.registro_material'
    _description = 'Registro de Materiales Usados'

    registro_diario_id = fields.Many2one('obras.registro_diario', string='Registro Diario', required=True, ondelete='cascade')
    material_id = fields.Many2one('product.product', string='Material', required=True)
    cantidad_usada = fields.Float(string='Cantidad Usada', required=True)
    inicio_aplicacion = fields.Float(string='Inicio de Aplicación')
    fin_aplicacion = fields.Float(string='Fin de Aplicación')
    observaciones = fields.Text(string='Observaciones')

class RegistroDiario(models.Model):
    _name = 'obras.registro_diario'
    _description = 'Registro Diario de Obra'

    obra_id = fields.Many2one('obras.obra', string='Obra', required=True)
    fecha = fields.Date(string='Fecha', required=True)
    metros_aplicados = fields.Float(string='Metros cuadrados aplicados')
    observaciones = fields.Text(string='Observaciones')
    hora_inicio = fields.Float(string='Hora inicio')
    hora_fin = fields.Float(string='Hora fin')
    duracion_jornada = fields.Float(
        string='Duración jornada',
        compute='_compute_duracion_jornada',
        store=True,
    )
    empleado_ids = fields.Many2many('hr.employee', string='Empleados')
    registro_material_ids = fields.One2many(
        'obras.registro_material',
        'registro_diario_id',
        string='Materiales Usados',
    )

    @api.depends('hora_inicio', 'hora_fin')
    def _compute_duracion_jornada(self):
        for record in self:
            if record.hora_inicio and record.hora_fin:
                record.duracion_jornada = record.hora_fin - record.hora_inicio
            else:
                record.duracion_jornada = 0.0
