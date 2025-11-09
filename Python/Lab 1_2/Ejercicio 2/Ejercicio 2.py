# Definimos los niveles posibles de amenaza con una tupla
niveles_amenaza = ("bajo", "moderado", "alto", "crítico")

# Asignamos el nivel actual (lo hacemos con input para hacer pruebas más rápido)
amenaza_actual = input("Introduce el nivel de amenaza (bajo, moderado, alto, crítico): ").lower()

# Comprobamos si el valor introducido está en la tupla
if amenaza_actual not in niveles_amenaza:
    print("\n Selecciona un nivel de amenaza adecuado (bajo, moderado, alto, crítico).")

else:
    # Según el nivel, mostramos una recomendación diferente
    if amenaza_actual == "bajo":
        print("\nActividad recomendada: Realizar auditorías de seguridad regulares.")

    elif amenaza_actual == "moderado":
        print("\n Actividad recomendada: Reforzar la concienciación de los empleados sobre riesgos de ciberseguridad.")

    elif amenaza_actual == "alto":
        print("\n Actividad recomendada: Implementar medidas de seguridad adicionales y revisar accesos.")

    elif amenaza_actual == "crítico":
        print("\n Actividad recomendada: Activar el protocolo de respuesta a incidentes.")
