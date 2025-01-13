from setuptools import setup,find_packages
setup(
    name = 'setup_environment_bbdd',
    version= '1.1.0',
    packages= find_packages(),# aqui se especifica el paquete o subpaquete que se quiere empaquetar
    description= 'paquete para la configuración de entorno para las conexiones a la base de datos de oracle en la maquina objetivo de quien ejecutara la aplicacion (SO windows)',
    author='Diana Pineda',
)
#nota: 
# actual: setuptools==75.1.0
# version de 24 abr 2023 de acorde al python 3.10.11: pip install setuptools==67.7.2
# ya se hizo el cambio