import os

# Función para leer las rutas desde un archivo
def leer_rutas(archivo_rutas):
    with open(archivo_rutas, 'r') as file:
        rutas = file.readlines()
    return [ruta.strip() for ruta in rutas]

# Función para obtener los archivos en cada ruta
def obtener_archivos(ruta):
    try:
        archivos = os.listdir(ruta)
        return archivos
    except FileNotFoundError:
        return [f"Error: Ruta no encontrada ({ruta})"]
    except Exception as e:
        return [f"Error: {str(e)}"]

# Función principal
def listar_archivos_por_ruta(archivo_rutas, archivo_salida):
    rutas = leer_rutas(archivo_rutas)

    with open(archivo_salida, 'w') as salida:
        for ruta in rutas:
            archivos = obtener_archivos(ruta)
            salida.write(f"Ruta: {ruta}\n")
            salida.write("Archivos encontrados:\n")
            for archivo in archivos:
                salida.write(f"- {archivo}\n")
            salida.write("\n")  # Para separar las rutas en el archivo de salida

# Especifica los archivos de entrada y salida
archivo_rutas = 'rutas.txt'
archivo_salida = 'lista.txt'

# Ejecuta el script
listar_archivos_por_ruta(archivo_rutas, archivo_salida)

print(f"Los resultados se han guardado en {archivo_salida}")
