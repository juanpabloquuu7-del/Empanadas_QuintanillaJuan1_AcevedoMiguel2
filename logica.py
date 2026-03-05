bd_empanadas = []

def obtener_todo():
    return bd_empanadas

def proceso_guardar(nombre, precio):
    
    nueva = {"item": nombre, "costo": precio}
    bd_empanadas.append(nueva)
    return True

def proceso_editar(indice, nombre, precio):
   
    if 0 <= indice < len(bd_empanadas):
        bd_empanadas[indice]["item"] = nombre
        bd_empanadas[indice]["costo"] = precio
        return True
    return False

def proceso_eliminar(indice):
    if 0 <= indice < len(bd_empanadas):
        bd_empanadas.pop(indice)
        return True
    return False