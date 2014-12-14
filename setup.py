from setuptools import setup, find_packages
from codecs import open

setup(
    name='SenialSOLID',
    version='1.0.0',
    description='SenialSOLID: Violacion la principio de SRP',
    author='VV',
    author_email='vvalotto@gmail.com',
    packages=['senial_solid'],
    py_modules=['lanzador'],
    entry_points = {'console_scripts' :
                    'lanzador = lanzador:Lanzador.ejecutar'}
)