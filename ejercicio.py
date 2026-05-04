personas = []

def cargar_persona(personas):
    """Añade una nueva persona a la lista"""
    nombre = input("Ingrese nombre de la persona: ")
    peso = float(input("Ingrese su peso en kg: "))
    nivel = int(input("Ingrese su nivel de actividad (1:baja ; 2:media ; 3:alta): "))
    consumo = float(input("Ingrese la cantidad de agua consumida hoy en ml: "))

    objetivo = calcular_objetivo_ml(peso, nivel)
    estado = estado_hidratacion(consumo, objetivo)

    personas.append({
        "nombre": nombre,
        "peso": peso,
        "nivel_actividad": nivel,
        "consumo": consumo,
        "objetivo": objetivo,
        "estado": estado
    })
    print(f"Persona {nombre} cargada exitosamente.\n")


def calcular_objetivo_ml(peso_kg, nivel_actividad):
    if nivel_actividad == 1:   # baja
        objetivo_ml = peso_kg * 35 * 0.9
    elif nivel_actividad == 2: # media
        objetivo_ml = peso_kg * 35
    else:                      # alta
        objetivo_ml = peso_kg * 35 * 1.1
    return round(objetivo_ml)


def estado_hidratacion(consumo_ml, objetivo_ml):
    if consumo_ml < objetivo_ml:
        porcentaje_falta = round(((objetivo_ml - consumo_ml) / objetivo_ml) * 100, 2)
        return f"Le falta un {porcentaje_falta}% para llegar."
    elif consumo_ml == objetivo_ml:
        return "Has alcanzado tu objetivo."
    else:
        porcentaje_exceso = round(((consumo_ml - objetivo_ml) / objetivo_ml) * 100, 2)
        return f"Has excedido tu objetivo en {porcentaje_exceso}%."

def cargar_persona(personas):
    try:
        nombre = input("Ingrese nombre de la persona: ")
        peso = float(input("Ingrese su peso en kg: "))
        nivel = int(input("Ingrese su nivel de actividad (1:baja ; 2:media ; 3:alta): "))
        consumo = float(input("Ingrese la cantidad de agua consumida hoy en ml: "))

        objetivo = calcular_objetivo_ml(peso, nivel)
        estado = estado_hidratacion(consumo, objetivo)

        personas.append({
            "nombre": nombre,
            "peso": peso,
            "nivel_actividad": nivel,
            "consumo": consumo,
            "objetivo": objetivo,
            "estado": estado
        })
        print(f"Persona {nombre} cargada exitosamente.\n")

    except ValueError:
        print("Error: Debías ingresar un número válido.\n")
    except IndexError as e:
        print(f"Error: {e}\n")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.\n")


# MENÚ PRINCIPAL
while True:
    print('''
    ===MENU===
    1 - Cargar persona
    2 - Mostrar personas cargadas y sus datos
    3- Salir
    ''')
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        cargar_persona(personas)
    elif opcion == "2":
        mostrar_personas(personas)
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
