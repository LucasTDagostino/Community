import os
os.system ("cls")
#Crea la clase Usuario (Clase madre)
class Usuario:
    def __init__(self, nombre, email, pais) -> None: #Atributos
        self.nombre = nombre
        self.email = email
        self.pais = pais

#Crea la clase Emprendedor (Clase hija de Usuario, hereda sus atributos)
class Emprendedor (Usuario):
    def __init__(self, nombre, email, pais,rubro, descripcion, estado_inversion, instancia, valuacion) -> None: #Atributos
        self.rubro= rubro
        self.descripcion = descripcion
        self.estado_inversion=estado_inversion
        self.instancia=instancia
        self.valuacion=valuacion
        super().__init__(nombre, email, pais) #Hereda los atributos de Usuario
class Inversor (Usuario):
    def __init__(self, nombre, email, pais, tipo_inversor, perfil_inversor, rubros_preferencias) -> None: #Atributos
        self.tipo_inversor=tipo_inversor
        self.perfil_inversor=perfil_inversor
        self.rubros_preferencias=rubros_preferencias
        super().__init__(nombre, email, pais) #Hereda los atributos de Usuario
