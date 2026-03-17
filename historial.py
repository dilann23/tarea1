def retroceder(historial, pasos):
    
    # Caso base 1: si no hay pasos o el historial está vacío
    if pasos == 0 or len(historial) == 0:
        return historial
    
    # Caso base 2: si encontramos un Error 404
    if "Error 404" in historial[-1]:
        print("Se encontró un Error 404. Retroceso detenido.")
        return historial
    
    # Eliminar la última página visitada
    pagina = historial.pop()
    print("Retrocediendo desde:", pagina)
    
    # Llamada recursiva
    return retroceder(historial, pasos - 1)


# Datos del ejercicio
mi_navegacion = [
    "google.com",
    "uniminuto.edu",
    "Error 404: Campus Virtual",
    "github.com",
    "stackoverflow.com"
]

# Prueba
resultado = retroceder(mi_navegacion, 3)
print("Historial final:", resultado)
