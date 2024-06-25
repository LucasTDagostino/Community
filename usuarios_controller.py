from db_usuarios import get_db
from usuarios_class import Usuario
from exchange_rate import tipo_de_cambio
import os

#Definis la funcion para insertar inversores en la tabla "inversores"
def insert_inversor(email, nombre, pais, tipo_inversor, perfil_inversor, rubros_preferencias, capital_a_invertir):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO inversores (email, nombre, pais, tipo_inversor, perfil_inversor, rubros_preferencias, capital_a_invertir) \
    VALUES ( ?, ? ,?, ?, ?, ?, ?)" #Statement que va a correr SQL
    cursor.execute(statement, [email,nombre,  pais, tipo_inversor, perfil_inversor, rubros_preferencias, capital_a_invertir]) #Ejecuta el statement
    db.commit()
    return True

#Definis la funcion para insertar emprendedores en la table "emprendedores"
def insert_emprendedor(email, nombre, pais,rubro,descripcion, estado_inversion, instancia, valuacion):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO emprendedores (email, nombre, pais,rubro, descripcion,  estado_inversion, instancia, valuacion) \
    VALUES ( ?, ? ,?, ?, ?, ?, ?, ?)" #Statement que va a correr el SQL
    cursor.execute(statement, [email, nombre, pais,rubro, descripcion, estado_inversion, instancia, valuacion]) #Ejecuta el statement
    db.commit()
    return True

#Definis la funcion para actualizar los datos de los emprendedores en la tabla "emprendedores"
def update_emprendedor(email, nombre, pais,rubro, descripcion, estado_inversion, instancia, valuacion):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE emprendedores SET nombre = ?, pais= ?, rubro= ?, descripcion = ?, estado_inversion= ?, instancia= ?, valuacion= ? \
    WHERE email = ?" #Actualizara los datos de la fila donde el email sea el mismo que el que querramos cambiar
    cursor.execute(statement, [email, nombre, pais,rubro, descripcion, estado_inversion, instancia, valuacion]) #le pasas una lista con los valores, ISBN al final por el where isbn (update cuyo ISBN sea el pasado al final)
    db.commit() 
    return True
#Definis la funcion para actualizar los datos de los emprendedores en la tabla "inversores"
def update_inversor(email, nombre, pais, tipo_inversor, perfil_inversor, rubros_preferencias, capital_a_invertir):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE inversores SET nombre = ?, pais= ?, tipo_inversor= ?, perfil_inversor= ?, rubros_preferencias= ?, capital_a_invertir= ? \
    WHERE email = ?" #Actualizara los datos de la fila donde el email sea el mismo que el que querramos cambiar
    cursor.execute(statement, [email,nombre, pais, tipo_inversor, perfil_inversor, rubros_preferencias, capital_a_invertir]) 
    db.commit() 
    return True

#Definis la funcion para eliminar un usuario 
def delete_usuario():
    db = get_db()
    cursor = db.cursor()
    usuario_eliminar= input ("Emprendedor/Inversor: ") #Elegis que tipo de usuario queres eliminar 
    if usuario_eliminar== "Emprendedor":
        statement="DELETE FROM emprendedores WHERE email = ?" #Statement --> Eliminara de emprendedores la fila de tal mail
    elif usuario_eliminar=="Inversor":
        statement = "DELETE FROM inversores WHERE email = ?" #Statement --> Eliminara de inversores la fila de tal mail
    email = (input('ingrese el email del usuario a eliminar: ')) #Ingresas el mail del usuario que queres eliminar
    cursor.execute(statement, [email]) #Ejecuta el statement en la base de datos de SQL
    db.commit()
    return True

#Definis la funcion para seleccionar un usuario segun el mail y mostrar sus datos
def get_by_email():
    db = get_db()
    cursor = db.cursor()
    usuario_buscar= input ("Emprendedor/Inversor: ") #Elegis que tipo de usuario queres seleccionar y mostrar
    if usuario_buscar == "Emprendedor": 
        #Statement --> Seleccionara y mostrara los datos del emprendedor cuyo mail sea el ingresado
        statement = "SELECT email, nombre, pais,rubro, descripcion, estado_inversion, instancia, valuacion ranking FROM emprendedores WHERE email = ?"
    elif usuario_buscar=="Inversor":
        #Statement --> Seleccionara y mostrara los datos del inversor cuyo mail sea el ingresado
        statement = "SELECT email, nombre, pais, tipo_inversor, perfil_inversor, rubros_preferencias, capital_a_invertir FROM inversores WHERE email = ?"
    email=input("Email: ")
    cursor.execute(statement, [email]) #Ejecuta el statement en la base de datos de SQL
    return cursor.fetchone()

#Definis la funcion para seleccionar y mostrar todos los usuarios segun tipo de usuario
def get_all_usuarios ():
    db = get_db()
    cursor = db.cursor()
    usuario_buscar= input ("Emprendedor/Inversor: ")#Elegis que tipo de usuario queres mostrar
    if usuario_buscar == "Emprendedor":
        #Query --> Selecciona todos los emprendedores
        query = "SELECT email, nombre, pais,rubro, descripcion, estado_inversion, instancia, valuacion ranking FROM emprendedores"
    elif usuario_buscar=="Inversor":
        #Query --> Selecciona todos los inversores
        query = "SELECT email, nombre, pais, tipo_inversor, perfil_inversor, rubros_preferencias, capital_a_invertir FROM inversores"
    cursor.execute(query)
    return cursor.fetchall()

#Definis la funcion para ingresar los datos
def Menu():
    print('****************************************************')
    print()
    print('Ingrese 1 para registrar un usuario a la base de datos.')
    print ('Ingrese 2 para eliminar un usuario de la base de datos.')
    print ("Ingrese 3 para modificar un emprendedor/inversor.")
    print ('Ingrese 4 para buscar un usuario por su email.')
    print('Ingrese 5 para listar todos los usuarios segun su tipo.')
    print ('Ingrese 6 para salir del menu.')        


flag = True
while flag:
    Menu()
    opcion = int(input())

#Ingresas los datos para correr las funciones 
    if opcion == 1:
        email= input ("Email: ")
        nombre= input ("Nombre completo: ")
        pais= input ("Pais: ")
        tipo_usuario= input("Inversor/Emprendedor: ")
        if tipo_usuario== "Inversor":
            print ("Angel/Incubadora/Fondo/Otro")
            tipo_inversor= input ("Tipo de inversor: ")
            print ("Estrategico/Financiero")
            perfil_inversor = input ("Perfil del inversor: ")
            print ("Agro/Fintech/Biotech/Industrial")
            rubros_preferencias = input ("Rubros preferidos: ")
            if pais=="Argentina":
                capital_a_invertir = int (input("Capital disponible para invertir (Pesos): ")) * tipo_de_cambio
            else:
                capital_a_invertir = int (input("Capital disponible para invertir (Dolares): "))
            result = insert_inversor(email, nombre, pais, tipo_inversor, perfil_inversor, rubros_preferencias, capital_a_invertir)
        elif tipo_usuario=="Emprendedor":
            print ("Agro/Fintech/Biotech/Industrial")
            rubro= input ("Rubro: ")
            descripcion= input ("Descripcion del negocio: ")
            print ("Pre-Seed/Seed/Serie A/Serie B/ Serie C/ Otro")
            estado_inversion= input ("Estado de inversion: ")
            print ("(Idea/Desarrollo/Lanzamiento/Crecimiento/Maduros)")
            instancia= input ("Instancia: ")
            if pais=="Argentina":
                valuacion = int (input("Valuacion del negocio (Pesos): ")) * tipo_de_cambio
            else:
                valuacion = int (input("Valuacion del negocio (Dolares): "))
            result = insert_emprendedor(email, nombre, pais,rubro, descripcion, estado_inversion, instancia, valuacion)
        
    elif opcion == 2:
        result = delete_usuario()
        if result == True:
            print('Usuario eliminado.')
            print()
            print()
        else:
            print('Error')
            print()
    elif opcion==3:
        tipo_usuario=input("Inversor/Emprendedor: ")
        email= input ("Email: ")
        nombre= input ("Nombre completo: ")
        pais= input ("Pais: ")
        if tipo_usuario=="Inversor":
            print ("Angel/Incubadora/Fondo/Otro")
            tipo_inversor= input ("Tipo de inversor: ")
            print ("Estrategico/Financiero")
            perfil_inversor = input ("Perfil del inversor: ")
            print ("Agro/Fintech/Biotech/Industrial")
            rubros_preferencias = input ("Rubros preferidos: ")
            if pais=="Argentina":
                capital_a_invertir = int (input("Capital disponible para invertir (Pesos): ")) / tipo_de_cambio
            else:
                capital_a_invertir = int (input("Capital disponible para invertir (Dolares): "))
            result=update_inversor (nombre, pais, tipo_inversor, perfil_inversor, rubros_preferencias, capital_a_invertir, email)
        elif tipo_usuario=="Emprendedor":
            print ("Agro/Fintech/Biotech/Industrial")
            rubro= input ("Rubro: ")
            descripcion= input ("Descripcion del negocio: ")
            print ("Pre-Seed/Seed/Serie A/Serie B/ Serie C/ Otro")
            estado_inversion= input ("Estado de inversion: ")
            print ("(Idea/Desarrollo/Lanzamiento/Crecimiento/Maduros)")
            instancia= input ("Instancia: ")
            if pais=="Argentina":
                valuacion = int (input("Valuacion del negocio (Pesos): ")) / tipo_de_cambio
            else:
                valuacion = int (input("Valuacion del negocio (Dolares): "))
            result = update_emprendedor(nombre, pais,rubro, descripcion, estado_inversion, instancia, valuacion, email)
    elif opcion == 4:
        result = get_by_email() # devuelve una tupla con el registro
        print (result)
        print()
        print()
    
    elif opcion == 5:
        result = get_all_usuarios() # devuelve una lista de tuplas donde cada tupla es un registro
        print(result)
        print()
        print()
    
    elif opcion == 6:
        print('Saliendo')
        print()
        flag = False
        pass

print ('Terminado.')
print('****************************************************')
        
Menu()