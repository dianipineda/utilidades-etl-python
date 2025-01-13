
import pyodbc

def check_odbc_driver():
    try:
        print("Verificando controladores ODBC disponibles...")
        drivers = pyodbc.drivers()
        if "ODBC Driver 17 for SQL Server" in drivers:
            print("El controlador ODBC Driver 17 for SQL Server está instalado.")
            return True
        else:
            print("El controlador ODBC Driver 17 for SQL Server no está instalado.")
            return False
    except Exception as e:
        print(f"Error al verificar los controladores ODBC: {e}")
        return False
#! este codigo hace que el antivirus elimine el archivo
# def install_sql_server_odbc_driver():
#     try:
#         print("Instalando el ODBC Driver 17 para SQL Server...")
        
#         # URL de descarga del driver ODBC 17 para SQL Server (enlace directo)
#         url = "https://go.microsoft.com/fwlink/?linkid=2266337"
        
#         # Nombre del archivo temporal donde se descargará el instalador
#         installer_path = "sql_server_odbc_driver_installer.exe"
        
#         # Descargar el instalador
#         urllib.request.urlretrieve(url, installer_path)
#         print("Instalador descargado correctamente.")

#         # Ejecutar el instalador de forma silenciosa
#        # Ejecutar el instalador de forma silenciosa
#         subprocess.check_call(["msiexec", "/i", installer_path, "/quiet", "/norestart"], shell=True)

#         # Eliminar el archivo del instalador
#         os.remove(installer_path)
        
#         print("ODBC Driver 17 para SQL Server instalado con éxito.")
#     except Exception as e:
#         print(f"Error al instalar el controlador ODBC: {e}")

# def ensure_odbc_driver_installed():
#     if not check_odbc_driver():
        # print("El controlador ODBC no está instalado. Procediendo con la instalación...")
        # install_sql_server_odbc_driver()
    # else:
    #     print("El controlador ODBC ya está instalado.")

#!Para pruebas, lo siguiente eliminar despues:
# if __name__ == "__main__":
#   check_odbc_driver()