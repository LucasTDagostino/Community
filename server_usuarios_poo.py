from flask import Flask, jsonify, request
import usuarios_controller
from db_usuarios import create_table

app = Flask(__name__)

@app.route('/welcome', methods=["GET"])
def welcome():
    return "Bienvenido a Community. (Se logro acceder a la API)"
#Crea la ruta para seleccionar y mostrar todos los usuarios
@app.route('/usuarios', methods=["GET"])
def get_all_usuarios():
    user = usuarios_controller.get_all_usuarios()
    users_list=[]
    for user in users_list:
        elem = user.serialize()
        users_list.append(elem)
    return jsonify(users_list)

#Crea la ruta para crear un usuario de tipo emprendedor
@app.route("/usuarios/emprendedores/create", methods=["POST"])
def insert_emprendedor():
    user_details = request.get_json()
    email = user_details["email"]
    nombre = user_details["nombre"]
    pais =user_details["pais"]
    rubro = user_details["rubro"]
    descripcion = user_details ["descripcion"]
    estado_inversion = user_details["estado_inversion"]
    instancia = user_details["instancia"]
    valuacion = user_details["valuacion"]
    result = usuarios_controller.insert_emprendedor(email, nombre, pais, rubro, descripcion, estado_inversion, instancia, valuacion)
    return jsonify(result)

#Crea la ruta para crear un usuario de tipo inversor
@app.route("/usuarios/inversores/create", methods=["POST"])
def insert_inversor():
    user_details = request.get_json()
    email = user_details["email"]
    nombre = user_details["nombre"]
    pais =user_details["pais"]
    tipo_inversor = user_details["tipo_inversor"]
    perfil_inversor = user_details["perfil_inversor"]
    rubros_preferencias = user_details["robros_preferencia"]
    capital_a_invertir = user_details["capital_a_invertir"]
    result = usuarios_controller.update_inversor(email, nombre, pais, tipo_inversor, perfil_inversor, rubros_preferencias,capital_a_invertir)
    return jsonify(result)

#Crea la ruta para modificar un usuario de tipo emprendedor
@app.route("/usuarios/emprendedores/modify", methods=["PUT"])
def update_emprendedor():
    user_details = request.get_json()
    email = user_details["email"]
    nombre = user_details["nombre"]
    pais =user_details["pais"]
    rubro = user_details["rubro"]
    descripcion = user_details ["descripcion"]
    estado_inversion = user_details["estado_inversion"]
    instancia = user_details["instancia"]
    valuacion = user_details["valuacion"]
    result = usuarios_controller.update_emprendedor(email, nombre, pais, rubro, descripcion, estado_inversion, instancia, valuacion)
    return jsonify(result)

#Crea la ruta para eliminar usuarios segun el email
@app.route("/usuarios/eliminate/<email>", methods=["DELETE"])
def delete_usuario(email):
    result = usuarios_controller.delete_usuario(email)
    return jsonify(result)

#Crea la ruta para obtener y mostrar los datos del usuario segun su mail
@app.route("/usuarios/<email>", methods=["GET"])
def get_by_email(email):
    usuario = usuarios_controller.get_by_email(email)
    return jsonify(usuario)
create_table()
if __name__ == '__main__':
    app.run()
