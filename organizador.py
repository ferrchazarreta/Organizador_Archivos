import os
import shutil

extensiones = {
    '.txt':'documentos',
    '.docx':'documentos',
    '.pdf':'documentos',
    '.xlsx':'documentos',
    '.jpg':'imagenes',
    '.jpeg':'imagenes',
    '.png':'imagenes',
    '.mp4':'videos',
    '.mov':'videos',
    '.mp3':'audios',
    '.exe':'ejecutables',
    '.stl':'stl',
    '.3mf':'stl',
    '.rar':'comprimidos',
    '.zip':'comprimidos',
}

predeterminada = 'otros'

ruta_carpeta_organizar = r'C:\Users\Fernando\Downloads'    #Ingresar la ruta de la carpeta que se quiere organizar

archivos = os.listdir(ruta_carpeta_organizar)
for archivo in archivos:
    ruta_origen_archivo = os.path.join(ruta_carpeta_organizar, archivo)
    if os.path.isfile(ruta_origen_archivo):
        _, extension = os.path.splitext(archivo)
        nombre_carpeta = extensiones.get(extension.lower(),'otros')
        ruta_destino_archivo = os.path.join(ruta_carpeta_organizar, nombre_carpeta)
        if not os.path.exists(ruta_destino_archivo):
            os.makedirs(ruta_destino_archivo)
        shutil.move(ruta_origen_archivo, ruta_destino_archivo)