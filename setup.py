from setuptools import setup, find_packages


setup(
    name='SenialSOLID',
    version='1.0.0',
    description='SenialSOLID - Paso 1: Violacion principio de SRP',
    author='VV',
    author_email='vvalotto@gmail.com',
    packages=find_packages(),
    py_modules=['lanzador'],
    entry_points={'console_scripts': 'lanzador = lanzador:Lanzador.ejecutar'}
)