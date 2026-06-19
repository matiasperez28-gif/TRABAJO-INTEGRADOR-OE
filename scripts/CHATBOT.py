import csv

ARCHIVO = "empleados.csv"

def cargar_empleados():
    empleados = {}

    try:
        with open(ARCHIVO, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                empleados[fila["legajo"]] = {
                    "nombre": fila["nombre"],
                    "dias_disponibles": int(fila["dias_disponibles"])
                }

    except FileNotFoundError:
        print("Error: No se encontró el archivo CSV.")

    return empleados


def guardar_empleados(empleados):
    with open(ARCHIVO, mode="w", newline="", encoding="utf-8") as archivo:

        campos = ["legajo", "nombre", "dias_disponibles"]

        escritor = csv.DictWriter(archivo, fieldnames=campos)

        escritor.writeheader()

        for legajo, datos in empleados.items():
            escritor.writerow({
                "legajo": legajo,
                "nombre": datos["nombre"],
                "dias_disponibles": datos["dias_disponibles"]
            })


def autenticar_empleado(empleados, legajo):
    return legajo in empleados


def verificar_dias(empleados, legajo, dias):
    return dias <= empleados[legajo]["dias_disponibles"]


def actualizar_dias(empleados, legajo, dias):
    empleados[legajo]["dias_disponibles"] -= dias


def decision_supervisor():
    decision = input("\nSupervisor: ¿Aprueba la solicitud? (si/no): ").lower().strip()

    while decision not in ["si", "no"]:
        decision = input("Ingrese solamente 'si' o 'no': ").lower().strip()

    return decision


# ===========================
# PROGRAMA PRINCIPAL
# ===========================

try:

    empleados = cargar_empleados()

    print("=== CHATBOT DE VACACIONES ===")

    legajo = input("Ingrese su legajo: ")

    if not autenticar_empleado(empleados, legajo):
        print("Legajo inexistente.")

    else:

        print(f"\nBienvenido {empleados[legajo]['nombre']}")
        dias = int(input("Cantidad de días solicitados: "))

        if verificar_dias(empleados, legajo, dias):

            print("\nSolicitud enviada al supervisor.")

            respuesta = decision_supervisor()

            if respuesta == "si":

                actualizar_dias(empleados,legajo,dias)

                guardar_empleados(empleados)

                print("\nSOLICITUD APROBADA")

                print("Días restantes:",empleados[legajo]["dias_disponibles"])

            else:

                print("\nSOLICITUD RECHAZADA POR EL SUPERVISOR")

        else:

            print("\nRECHAZO AUTOMÁTICO")
            print("No posee suficientes días disponibles.")

except ValueError:
    print("Error: la cantidad de días debe ser numérica.")

except Exception as e:
    print(f"Error inesperado:", {e})


'''ARCHIVO_ESTADOS = "estados.csv"

def cargar_estados():
    estados = {}

    try:
        with open(ARCHIVO_ESTADOS, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                estados[fila["legajo"]] = fila["estado"]

    except FileNotFoundError:
        pass

    return estados


def guardar_estados(estados):

    with open(ARCHIVO_ESTADOS,
              mode="w",
              newline="",
              encoding="utf-8") as archivo:

        campos = ["legajo", "estado"]

        escritor = csv.DictWriter(
            archivo,
            fieldnames=campos
        )

        escritor.writeheader()

        for legajo, estado in estados.items():

            escritor.writerow({
                "legajo": legajo,
                "estado": estado
            })


def cambiar_estado(estados, legajo, nuevo_estado):

    estados[legajo] = nuevo_estado

    guardar_estados(estados)'''