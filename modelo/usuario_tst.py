__author__ = 'voval'
__project__ = ''

from modelo.usuario import *
from persistidor.contexto import *
from persistidor.repositorio import *


def crear_usuario():
    usu = Usuario()
    nom = Nombre()
    nom.nombre = 'Victor'
    nom.apellido = 'Valotto'
    usu.id = 14367849
    usu.usuario = 'vvalotto'
    usu.clave = 'voval062'
    usu.nombre_apellido = nom

    return usu

if __name__ == '__main__':
    contexto = ContextoArchivo('/Users/voval/tmp/datos')
    repo = RepositorioUsuario(contexto)
    usu = crear_usuario()
    repo.guardar(usu)
    print(usu.usuario)
    usu1 = repo.obtener(Usuario(), usu.id)
    print(usu1)
    print(usu1.usuario)