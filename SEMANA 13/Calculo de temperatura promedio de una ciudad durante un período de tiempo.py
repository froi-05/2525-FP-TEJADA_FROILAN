# Función para calcular la temperatura promedio por ciudad
# Parámetros: datos es un diccionario con ciudades como claves
# y diccionarios internos con semanas en orden como claves y temperaturas como valores.
# Retorna un diccionario con la temperatura promedio por ciudad.

def calcular_promedio_temperaturas(datos):
    promedios = {}
    for ciudad, semanas in datos.items():
        temperaturas = []
        # Recorremos semanas en orden numérico para garantizar el orden correcto
        for semana in sorted(semanas.keys()):
            temperaturas.append(semanas[semana])
        # Calculamos el promedio si hay datos
        if temperaturas:
            promedio = sum(temperaturas) / len(temperaturas)
            promedios[ciudad] = promedio
        else:
            promedios[ciudad] = None
    return promedios

# Datos de ejemplo: cada ciudad con semanas ordenadas y sus temperaturas
datos_temperaturas = {
    'Quito': {'Semana 1': 15, 'Semana 2': 16, 'Semana 3': 14, 'Semana 4': 15},
    'Guayaquil': {'Semana 1': 29, 'Semana 2': 30, 'Semana 3': 28, 'Semana 4': 31},
    'Cuenca': {'Semana 1': 18, 'Semana 2': 17, 'Semana 3': 18, 'Semana 4': 19}
}

# Calcular promedios
promedios = calcular_promedio_temperaturas(datos_temperaturas)
print(promedios)  # {'Quito': 15.0, 'Guayaquil': 29.5, 'Cuenca': 18.0}
