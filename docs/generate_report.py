import datetime

# Datos base proporcionados
DATA = {
    'Fecha': '2025-06-26',
    'Bolsas_fibra': 231,
    'Adhesivo_bidones': 48,
    'Volumen_aplicado_m2': 2654,
    'Obras_iniciadas_semana': 13,
    'Kg_descartes_semana': 446.0,
    'Tiempo_promedio_jornada_horas': 5.33,
    'Cantidad_registros_diarios': 18,
}

# Indicadores adicionales calculados
def indicadores_adicionales(data):
    vol = data['Volumen_aplicado_m2']
    fibra_por_m2 = data['Bolsas_fibra'] / vol
    adhesivo_por_m2 = data['Adhesivo_bidones'] / vol
    descarte_por_m2 = data['Kg_descartes_semana'] / vol
    horas_totales = data['Tiempo_promedio_jornada_horas'] * data['Cantidad_registros_diarios']
    return {
        'Fibra por m2': round(fibra_por_m2, 4),
        'Adhesivo por m2': round(adhesivo_por_m2, 4),
        'Descarte por m2 (kg)': round(descarte_por_m2, 4),
        'Horas totales estimadas': round(horas_totales, 2),
    }

# Generador de barras ASCII
def barra(value, max_value, width=30):
    proportion = value / max_value if max_value else 0
    fill = int(proportion * width)
    return '[' + '#' * fill + '-' * (width - fill) + ']'

def generar_reporte(data):
    lines = []
    lines.append(f"Reporte Semanal - Fecha: {data['Fecha']}")
    lines.append('')
    lines.append('Indicadores Principales:')

    valores = {
        'Bolsas de fibra usadas': data['Bolsas_fibra'],
        'Adhesivo (bidones)': data['Adhesivo_bidones'],
        'Volumen aplicado (m2)': data['Volumen_aplicado_m2'],
        'Obras iniciadas': data['Obras_iniciadas_semana'],
        'Kg de descarte': data['Kg_descartes_semana'],
        'Tiempo promedio jornada (h)': data['Tiempo_promedio_jornada_horas'],
        'Cantidad registros diarios': data['Cantidad_registros_diarios'],
    }

    max_val = max(valores.values())
    for nombre, valor in valores.items():
        lines.append(f"- {nombre}: {valor}")
        lines.append('  ' + barra(valor, max_val))

    lines.append('')
    lines.append('Indicadores Adicionales:')
    extras = indicadores_adicionales(data)
    for nombre, valor in extras.items():
        lines.append(f"- {nombre}: {valor}")

    return '\n'.join(lines)

if __name__ == '__main__':
    contenido = generar_reporte(DATA)
    ruta = 'docs/reporte_semanal_2025-06-26.txt'
    with open(ruta, 'w') as f:
        f.write(contenido + "\n")
    print(f'Reporte generado en {ruta}')
