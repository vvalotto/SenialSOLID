from setuptools import setup
import lanzador

setup(
    name='SenialSOLID',
    version=lanzador.__version__,
    description='SenialSOLID - Paso 5: Aplicacion del Principio OCP - Solo Procesador',
    author='VV',
    author_email='vvalotto@gmail.com',
    py_modules=['lanzador', 'configurador'],
    entry_points={'console_scripts': 'lanzador = lanzador:Lanzador.ejecutar'}
)
