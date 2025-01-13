#Notas:
- Esta aplicacion no tiene environment(venv) y no debe tener

#Generar ejecutable:
1) Cambiar la version en el archivo setup.py
2) Ejecutar sobre la carpeta principal: python setup.py sdist
3) Copiar el archivo que se genero dentro de la carpeta dist/
4) Pegar el archivo en la raiz del proyecto de la aplicacion en donde lo voy a usar
5) Ejecutar en la raiz del proyecto de la aplicacion en donde lo voy a usar: pip install nombre_archivo.tar.gz
6) Donde lo vaya a llamar, llamarlo asi: source.nombremodulo
7) añadir este paquete dentro del comando de pyinstaller asi: ...--add-data"D:\INGENIO\projects\nombre_proyecto\nombre_archivo.tar.gz;." main.py

#TODO: generar commit y versionamiento