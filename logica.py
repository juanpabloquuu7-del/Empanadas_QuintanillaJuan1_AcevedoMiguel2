import json
NOMBRE_ARCHIVO = "empanadas.json"

def cargar_datos():
    try:
        # Intentamos abrir el archivo
        with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        # Si el archivo no existe todavía, devolvemos una lista vacía
        return []

def guardar_datos(lista):
    with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4)


def agregar_empanada(nombre, precio):
    lista = cargar_datos()
    lista.append({"nombre": nombre, "precio": precio})
    guardar_datos(lista)

def proceso_eliminar(indice):
    if 0 <= indice < len(bd_empanadas):
        bd_empanadas.pop(indice)
        return True
    return False