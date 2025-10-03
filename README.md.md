# Módulo de Cálculo de Calificación Final

## Descripción
Módulo Python para calcular la calificación final de estudiantes según especificaciones de la Evaluación Rápida 3.

## Funcionalidades
- Cálculo ponderado de calificaciones
- Validación de rangos y ponderaciones
- Aplicación de reglas de negocio (asistencia, examen final)
- Manejo robusto de errores

## Uso
```python
from calificacion_final import calcularCalificacionFinal

resultado = calcularCalificacionFinal(8.5, 9.0, 7.5, 90, 0.3, 0.3, 0.4)
print(resultado)  # Output: 8.3