from setuptools import setup, find_packages

setup(
    name='SenialSOLID',
    version='2.2.0',
    description='SenialSOLID - Paso 3: Aplicacion del Principio SRP - con Modulos separados',
    author='VV',
    author_email='vvalotto@gmail.com',
    packages=find_packages(),
    py_modules=['lanzador'],
    entry_points={'console_scripts': 'lanzador = lanzador:Lanzador.ejecutar'}
)
