import json
import os
from json import JSONDecodeError


class Historial:
    def __init__(self):
        self.ruta_json = "usuarios.json"

    def guardar_json(self,usuarios):
        with open(self.ruta_json,"w") as archivo:
            json.dump(usuarios,archivo,indent=4)

    def cargar_json(self):
        if not os.path.exists(self.ruta_json):
            return []
        try:
            with open(self.ruta_json,"r") as archivo:
                usuarios = json.load(archivo)
                return usuarios
        except JSONDecodeError:
            return []