# Primero, abrimos (o creamos) el archivo 'my_notes.txt' en modo escritura
archivo = open('my_notes.txt', 'w')  # 'w' es para escribir

# Escribimos tres notas personales, cada una en una línea
archivo.write('Hoy aprendí a usar archivos en Python.\n')
archivo.write('Me parece útil para guardar información.\n')
archivo.write('Mañana quiero probar con archivos CSV.\n')

# Cerramos el archivo después de escribir
archivo.close()

# Ahora lo abrimos en modo lectura para ver lo que escribimos
archivo = open('my_notes.txt', 'r')  # 'r' es para leer

# Leemos línea por línea y mostramos cada una en pantalla
linea = archivo.readline()
while linea:
    print(linea.strip())  # .strip() quita el salto de línea al mostrar
    linea = archivo.readline()

# Cerramos el archivo después de leer
archivo.close()
