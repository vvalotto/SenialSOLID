
class Usuario(object):

    def __init__(self):
        self._id = 0
        self._usuario = ""
        self._nombre_apellido = ""
        self._clave = ""

    # Propiedades
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def nombre_apellido(self):
        return self._nombre_apellido

    @nombre_apellido.setter
    def nombre_apellido(self, valor):
        self._nombre_apellido = valor

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, valor):
        self._usuario = valor

    @property
    def clave(self):
        return self._clave

    @clave.setter
    def clave(self, valor):
        self._clave = valor

    def __str__(self):
        cadena = ''
        cadena += 'id: ' + str(self._id) + '\n'
        cadena += 'usuario: ' + str(self._usuario) + '\n'
        cadena += 'clave: ' + str(self._clave) + '\n'
        cadena += 'nombre: ' + str(self._nombre_apellido) + '\n'
        return cadena