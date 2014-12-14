from setuptools import setup, find_packages
from codecs import open

setup(
    name='SenialSOLID',
    version='2.2.1-dev',
    description='SenialSOLID: Aplicacion de l Principio SRP - Modularizacion',
    author='VV',
    author_email='vvalotto@gmail.com',
    packages=['adquisidor', 'modelo', 'procesador', 'visualizador'],
    py_modules=['lanzador'],
    entry_points = {'console_scripts' :
                    'lanzador = lanzador:Lanzador.ejecutar'}
)