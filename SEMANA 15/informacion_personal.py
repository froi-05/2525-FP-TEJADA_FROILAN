# 1. Crear un diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Luisa Fernández",  # Nombre de la persona
    "edad": 30,                   # Edad (se eliminará después)
    "ciudad": "Quito",            # Ciudad de residencia inicial
    "profesion": "Arquitecta"     # Profesión inicial
}

# 2. Acceder y modificar el valor asociado con la clave "ciudad"
informacion_personal["ciudad"] = "Guayaquil"  # Cambiar ciudad a Guayaquil

# Agregar o modificar la clave "profesion"
informacion_personal["profesion"] = "Diseñadora de interiores"  # Nueva profesión

# 3. Verificar si la clave "telefono" existe; si no, agregarla con un número ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0998765432"

# 4. Eliminar la clave "edad" porque no es necesaria
informacion_personal.pop("edad", None)

# 5. Imprimir el diccionario final después de las modificaciones
print(informacion_personal)
