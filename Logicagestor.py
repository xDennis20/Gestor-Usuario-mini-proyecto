#Logica
from Historial import Historial

class GestorUsuario:
    def __init__(self):
        self.lista_usuarios = []
        self.historial = Historial()
        self.historial.cargar_json()
    @staticmethod
    def registrar_usuario():
        nombre = input("Ingrese su nombre: ").strip()
        edad = int(input("Ingrese su edad: "))
        correo = input("Ingrese su correo: ")
        diccionario_usuario = dict({
            "nombre": nombre,
            "edad": edad,
            "correo": correo
        })
        print("Usuario Registrado Correctamente")
        return diccionario_usuario

    def agregar_usuario(self,usuario: dict):
        verificar_correo = self.buscar_usuario(usuario.get("correo"))
        if verificar_correo is None:
            self.lista_usuarios.append(usuario)
            self.historial.guardar_json(self.lista_usuarios)
            print("Usuario Agregado Correctamente Al Gestor")
        else:
            print("El correo ya existe, No se agrego el usuario")

    def buscar_usuario(self,correo):
        for usuario in self.lista_usuarios:
            if usuario.get("correo") == correo:
                return usuario
        return None

    def usuario_mayores(self):
        lista_usuarios_mayores = []
        for usuario in self.lista_usuarios:
            if usuario.get("edad") >= 18:
                lista_usuarios_mayores.append(usuario)
        return lista_usuarios_mayores

    def mostrar_usuarios(self):
        for u in self.lista_usuarios:
            print("Usuario:\n"
                  f"Nombre: {u.get("nombre")}\n"
                  f"Edad: {u.get("edad")}\n"
                  f"Correo: {u.get("correo")}\n")

    def eliminar_usuario(self,correo_usuario):
        usuario_eliminado = False
        for usuario in self.lista_usuarios:
            if usuario.get("correo") == correo_usuario:
                del usuario
                usuario_eliminado = True
        if not usuario_eliminado:
            print("El usuario no fue encontrado")
        else:
            print("El usuario fue eliminado con exito")