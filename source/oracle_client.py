import os
from tkinter import messagebox
from typing import Union
import zipfile
import subprocess
import sys
from pathlib import Path

oracle_client_path:str = r"D:\clientes_bbdd\instantclient_19_24"
zip_file_name:str = "instantclient_19_24.zip" 

def extract_zip(zip_path:Union[str,Path], extract_to:Union[str,Path]) -> None:
    """Extrae el archivo zip en la ubicación especificada"""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def set_oracle_environment(oracle_path:Union[str,Path]) -> None:
    """
    Configura las variables de entorno para Oracle Instant Client.
    
    - Agrega `oracle_path` a la variable `PATH` si no está presente.
    - Configura `TNS_ADMIN` y `ORACLE_HOME` si no están definidos.
    """
    oracle_path_str: str = str(oracle_path)  # Asegurar que siempre sea un str

    if oracle_path_str not in os.environ.get('PATH', ''):
        os.environ['PATH'] = oracle_path_str + os.pathsep + os.environ['PATH']

    if 'TNS_ADMIN' not in os.environ:
        os.environ['TNS_ADMIN'] = oracle_path_str

    if 'ORACLE_HOME' not in os.environ:
        os.environ['ORACLE_HOME'] = oracle_path_str

def install_oracle_client() -> None:
    """
    Instala y configura el cliente de Oracle en la máquina.

    - Verifica la existencia del archivo ZIP con el cliente de Oracle.
    - Extrae el contenido del ZIP en la ubicación correspondiente.
    - Mueve los archivos extraídos a la ruta correcta.
    - Configura las variables de entorno necesarias para el uso del cliente de Oracle.

    Si el archivo ZIP no está presente, la instalación no se realizará.
    """
    script_dir:str = os.path.dirname(os.path.abspath(sys.argv[0]))
    zip_file_path:str = os.path.join(script_dir, zip_file_name)

    if not os.path.exists(oracle_client_path):
        os.makedirs(oracle_client_path)

    if not os.path.exists(zip_file_path):
        messagebox.showwarning("Advertencia",f"Archivo {zip_file_name} no encontrado en la carpeta del ejecutable.\nNo se encuentra el cliente de oracle, por lo tanto no se puede continuar con la ejecucion de la aplicación")
        return None

    extract_zip(zip_file_path, oracle_client_path)

    # Mover los archivos extraídos a la ruta correcta y limpiar
    for item in os.listdir(oracle_client_path):
        item_path:str = os.path.join(oracle_client_path, item)
    if os.path.isdir(item_path):
        for file in os.listdir(item_path):
            source_path:str = os.path.join(item_path, file)
            destination_path:str = os.path.join(oracle_client_path, file)
            
            # Verificar si el archivo ya existe en el destino
            if os.path.exists(destination_path):
                pass
                # print(f"El archivo {file} ya existe en {oracle_client_path}. No se moverá.")
            else:
                # Mover el archivo si no existe en el destino
                os.rename(source_path, destination_path)
        
        # Eliminar la subcarpeta después de mover los archivos
        os.rmdir(item_path)

    set_oracle_environment(oracle_client_path)

    # print("Instalación y configuración completadas.")
