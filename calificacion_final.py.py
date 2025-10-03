def calcularCalificacionFinal(promedio_tareas, promedio_quizzes, calificacion_examen_final, 
                            porcentaje_asistencia, ponderacion_tareas, ponderacion_quizzes, 
                            ponderacion_examen_final):
    """
    Calcula la calificacion final de un estudiante basándose en:
    - Promedio de tareas
    - Promedio de quizzes
    - Calificación del examen final
    - Porcentaje de asistencia
    - Ponderaciones de cada componente
    """
    
    # Validacion de rangos de todos los parametros
    if not (0.0 <= promedio_tareas <= 10.0):
        return -1.0
    if not (0.0 <= promedio_quizzes <= 10.0):
        return -1.0
    if not (0.0 <= calificacion_examen_final <= 10.0):
        return -1.0
    if not (0 <= porcentaje_asistencia <= 100):
        return -1.0
    if not (0.0 <= ponderacion_tareas <= 1.0):
        return -1.0
    if not (0.0 <= ponderacion_quizzes <= 1.0):
        return -1.0
    if not (0.0 <= ponderacion_examen_final <= 1.0):
        return -1.0
    
    # Validacion de ponderacion (suma debe ser exactamente 1.0)
    suma_ponderaciones = (ponderacion_tareas + ponderacion_quizzes + 
                         ponderacion_examen_final)
    if abs(suma_ponderaciones - 1.0) > 0.0001:
        return -1.0
    
    # Condicion de Asistencia
    if porcentaje_asistencia < 80:
        return 5.0
    
    # Condicion del Examen Final
    if calificacion_examen_final < 6.0:
        return 5.0
    
    # Calculo Ponderado
    calificacion_ponderada = (
        promedio_tareas * ponderacion_tareas +
        promedio_quizzes * ponderacion_quizzes +
        calificacion_examen_final * ponderacion_examen_final
    )
    
    # Redondear a un decimal
    calificacion_final = round(calificacion_ponderada, 1)
    
    return calificacion_final

def ejecutarPruebas():
    """
    Ejecuta los casos de prueba definidos en la especificacion
    """
    print("=== EJECUCION DE CASOS DE PRUEBA ===")
    
    # Caso 1: Aprobado
    resultado1 = calcularCalificacionFinal(8.5, 9.0, 7.5, 90, 0.3, 0.3, 0.4)
    print(f"Caso 1 - Aprobado: {resultado1} (Esperado: 8.3)")
    
    # Caso 2: Reprobado por Asistencia
    resultado2 = calcularCalificacionFinal(10.0, 10.0, 10.0, 79, 0.3, 0.3, 0.4)
    print(f"Caso 2 - Reprobado por Asistencia: {resultado2} (Esperado: 5.0)")
    
    # Caso 3: Reprobado por Examen Final
    resultado3 = calcularCalificacionFinal(10.0, 10.0, 5.9, 100, 0.3, 0.3, 0.4)
    print(f"Caso 3 - Reprobado por Examen Final: {resultado3} (Esperado: 5.0)")
    
    # Caso 4: Reprobado por Calificacion
    resultado4 = calcularCalificacionFinal(6.0, 6.0, 7.0, 85, 0.3, 0.3, 0.4)
    print(f"Caso 4 - Reprobado por Calificacion: {resultado4} (Esperado: 6.4)")
    
    # Caso 5: Error - Ponderacion Invalida
    resultado5 = calcularCalificacionFinal(8.0, 8.0, 8.0, 90, 0.3, 0.3, 0.3)
    print(f"Caso 5 - Error Ponderacion: {resultado5} (Esperado: -1.0)")
    
    # Caso 6: Error - Calificacion Fuera de Rango
    resultado6 = calcularCalificacionFinal(11.0, 8.0, 8.0, 90, 0.3, 0.3, 0.4)
    print(f"Caso 6 - Error Rango: {resultado6} (Esperado: -1.0)")
    
    # Caso 7: Caso Frontera (Asistencia)
    resultado7 = calcularCalificacionFinal(10.0, 10.0, 10.0, 80, 0.3, 0.3, 0.4)
    print(f"Caso 7 - Frontera Asistencia: {resultado7} (Esperado: 10.0)")

if __name__ == "__main__":
    ejecutarPruebas()