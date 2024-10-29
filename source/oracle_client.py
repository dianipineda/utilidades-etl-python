import os
import zipfile
import subprocess
import sys

oracle_client_path = r"D:\clientes_bbdd\instantclient_19_24"
zip_file_name = "instantclient_19_24.zip" 

def extract_zip(zip_path, extract_to):
    """Extraer el archivo zip en la ubicación especificada"""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def set_oracle_environment(oracle_path):
    """Configurar las variables de entorno para Oracle Instant Client"""
    if oracle_path not in os.environ.get('PATH', ''):
        os.environ['PATH'] = oracle_path + os.pathsep + os.environ['PATH']
        # subprocess.run(f'setx PATH "{oracle_path};%PATH%"', shell=True)
    if 'TNS_ADMIN' not in os.environ:    
        os.environ['TNS_ADMIN'] = oracle_path
        # subprocess.run(f'setx TNS_ADMIN "{oracle_path}"', shell=True)
    if 'TNS_ADMIN' not in os.environ:
        os.environ['ORACLE_HOME'] = oracle_path
        # subprocess.run(f'setx ORACLE_HOME "{oracle_path}"', shell=True)

def install_oracle_client():
    """Función principal para instalar el cliente de Oracle"""
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    zip_file_path = os.path.join(script_dir, zip_file_name)

    if not os.path.exists(oracle_client_path):
        os.makedirs(oracle_client_path)

    if not os.path.exists(zip_file_path):
        print(f"Archivo {zip_file_name} no encontrado en la carpeta del ejecutable.")
        return

    extract_zip(zip_file_path, oracle_client_path)

    # Mover los archivos extraídos a la ruta correcta y limpiar
    for item in os.listdir(oracle_client_path):
        item_path = os.path.join(oracle_client_path, item)
    if os.path.isdir(item_path):
        for file in os.listdir(item_path):
            source_path = os.path.join(item_path, file)
            destination_path = os.path.join(oracle_client_path, file)
            
            # Verificar si el archivo ya existe en el destino
            if os.path.exists(destination_path):
                print(f"El archivo {file} ya existe en {oracle_client_path}. No se moverá.")
            else:
                # Mover el archivo si no existe en el destino
                os.rename(source_path, destination_path)
        
        # Eliminar la subcarpeta después de mover los archivos
        os.rmdir(item_path)

    set_oracle_environment(oracle_client_path)

    print("Instalación y configuración completadas.")
