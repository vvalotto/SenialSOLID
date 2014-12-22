from setuptools import setup

setup(
    name='SenialSOLID',
    version='4.0.2',
    description='SenialSOLID - Paso 5: Aplicacion del Principio OCP - Solo Procesador',
    author='VV',
    author_email='vvalotto@gmail.com',
    py_modules=['lanzador', 'configurador'],
    entry_points={'console_scripts': 'lanzador = lanzador:Lanzador.ejecutar'}
)
