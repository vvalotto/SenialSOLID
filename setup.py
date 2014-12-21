from setuptools import setup

setup(
    name='SenialSOLID',
    version='3.1.0',
    description='SenialSOLID - Paso 4: Violacion al principio de OCP',
    author='VV',
    author_email='vvalotto@gmail.com',
    py_modules=['lanzador'],
    entry_points={'console_scripts': 'lanzador = lanzador:Lanzador.ejecutar'}
)
