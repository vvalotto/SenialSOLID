from setuptools import setup, find_packages
from codecs import open

setup(
    name='SenialSOLID',
    version='2.1.0',
    description='SenialSOLID: Aplicacion del Principio SRP',
    author='VV',
    author_email='vvalotto@gmail.com',
    py_modules=['lanzador'],
    entry_points = {'console_scripts' :
                    'lanzador = lanzador:Lanzador.ejecutar'}
)

setup(
    name='adquisidor',
    version='1.0.1',
    description='Modulo de Adquiscion',
    author='VV',
    author_email='vvalotto@gmail.com',
    packages=['adquisidor'],
)

setup(
    name='modelo',
    version='1.0.0',
    description='Modulo de Modelo de Dominio',
    author='VV',
    author_email='vvalotto@gmail.com',
    packages=['modelo'],
)

setup(
    name='procesador',
    version='1.0.1',
    description='Modulo de Procesamiento',
    author='VV',
    author_email='vvalotto@gmail.com',
    packages=['procesador'],
)

setup(
    name='visualizador',
    version='1.0.1',
    description='Modulo de Visualizacion',
    author='VV',
    author_email='vvalotto@gmail.com',
    packages=['visualizador'],
)

