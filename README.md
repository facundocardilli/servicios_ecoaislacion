# 📐 Gestión Integral de Obras de Aislamiento

## 🏗️ Objetivo de la App
La aplicación gestiona el ciclo completo de obras de aislamiento para empresas constructoras, desde la planificación hasta el registro detallado de materiales, empleados y métricas de rendimiento.

---

## 🧩 Estructura de la Base de Datos

### Obras
- **IdObra** (PK)
- **Nombre**
- **Dirección**
- **Cliente** (FK)
- **Status** (Activa, Finalizada, etc.)
- **Tiempo de traslado**
- **Metros a aplicar**
- **Espesor**
- **Altura máxima**

> **Restricción:** Solo una obra activa por dirección en simultáneo para evitar duplicados.

### Clientes
- **IdCliente** (PK)
- **Nombre**
- **Teléfono**
- **Ubicación**

### Empleados
- **IdEmpleado** (PK)
- **Nombre**
- **Email**
- **Rol**

### Materiales
- **IdMaterial** (PK)
- **Nombre**
- **Unidad de medida**
- **Tipo** (Fibra, Adhesivo, etc.)

### Registros Diarios
- **IdRegistro** (PK)
- **Fecha**
- **Obra** (FK)
- **Metros cuadrados aplicados**
- **Observaciones**
- **Hora inicio**
- **Hora fin**
- **Duración jornada**
- **Empleados** (relación EnumList referenciada)

### Registros de Materiales Usados
- **IdRegistroMaterial** (PK)
- **IdRegistroDiario** (FK)
- **Material** (FK)
- **Cantidad Usada**
- **Inicio de Aplicación**
- **Fin de Aplicación**
- **Observaciones**

### Cronograma
- **IdCronograma** (PK)
- **Obra** (FK)
- **Fecha**
- **EmpleadoAsignado** (FK)
- **Estado**
- **Notas**

---

## ⚙️ Funciones Clave

- **Registro de Jornada:**  
  - Inicio/fin de jornada por operario.  
  - Asignación de empleados por registro.  
  - Observaciones técnicas.

- **Carga de Materiales Usados:**  
  - Registro múltiple de materiales por jornada con unidades específicas.

- **Panel de Control Administrador:**  
  - ABM (Alta/Baja/Modificación/Consulta) de obras, clientes, empleados y materiales.  
  - Reglas de consistencia para evitar duplicados.

- **Cronograma de Obras:**  
  - Planificación y asignación semanal.  
  - Vistas filtradas por empleado.

- **Reportes Automatizados:**  
  - KPIs semanales enviados por email.  
  - Plantillas personalizadas de indicadores clave.

---

## 📈 Indicadores y KPIs

- m² aplicados por semana.
- Rendimiento de material (m² por tipo de fibra).
- Consumo de material vs estimado.
- Duración promedio de jornada.
- Empleados asignados por obra.
- Obras activas vs finalizadas.
- Desviación estándar de rendimiento.
- Distribución temporal/dispersión de materiales usados.

---

## 🔐 Restricciones y Seguridad

- **Filtrado por usuario:** Cada empleado visualiza solo sus asignaciones y registros.
- **Control de acceso:** Vistas restringidas para roles administrativos.
- **Consistencia de datos:** Validaciones y referencias estrictas.
- **Evita duplicidad:** Obras y clientes únicos por criterio definido.

---

## 🔄 Automatizaciones

- Envío automático de reportes semanales.
- Notificaciones a empleados asignados a tareas.
- Claves primarias automáticas.
- Sincronización y control de datos entre tablas relacionadas.

---

## 🛠️ Recomendaciones Técnicas

- Usar campos de referencia (FK) y validaciones para consistencia.
- Automatizar generación de claves y cálculos de métricas.
- Implementar roles de usuario y filtros de acceso.
- Aplicar triggers/notificaciones para automatizaciones y alertas.
- Optimizar reportes con plantillas adaptadas a las métricas del negocio.

---

> **Nota:** Esta estructura es adaptable para desarrollo low-code (AppSheet, Retool) o soluciones personalizadas (React, Django, etc.).
