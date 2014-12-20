from setuptools import setup, find_packages

setup(
    name='SenialSOLID',
    version='2.0.0',
    description='SenialSOLID - Paso 2: Aplicacion del Principio de Responsabilidad Unica',
    author='VV',
    author_email='vvalotto@gmail.com',
    packages=find_packages(),
    py_modules=['lanzador'],
    entry_points={'console_scripts': 'lanzador = lanzador:Lanzador.ejecutar'}
)