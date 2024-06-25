import sqlite3
import os
#Crea la base de datos
DATABASE_NAME = "usuarios.db"
os.system ("cls")

#Conecta la base de datos
def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

#Crea las tablas 
#Se introduce el statement para crear las tablas en la base de datos
#"Not null" = No puede estar vacio, "Primary key" = Valor unico para ese inversor/emprendedor (Ej: DNI)

def create_table():
    #Statement para crear tabla "inversores"
    table_inversores= """CREATE TABLE IF NOT EXISTS inversores(
                email TEXT PRIMARY KEY,
                nombre TEXT NOT NULL,
                pais TEXT NOT NULL,
                tipo_inversor TEXT NOT NULL,
                perfil_inversor TEXT NOT NULL,
                rubros_preferencias TEXT NOT NULL,
                capital_a_invertir INTEGER NOT NULL
                )"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute(table_inversores) #Ejecuta statement para crear tabla "inversores"
    #Statement para crear tabla "emprendedores", 
    table_emprendedores=  """CREATE TABLE IF NOT EXISTS emprendedores(
                email TEXT PRIMARY KEY,
                nombre TEXT NOT NULL,
                pais TEXT NOT NULL,
                rubro TEXT NOT NULL,
                descripcion TEXT NOT NULL, 
                estado_inversion TEXT NOT NULL,
                instancia TEXT NOT NULL,
                valuacion INTEGER NOT NULL
                )"""
    db = get_db()
    cursor = db.cursor()
    #Ejecuta el statement
    cursor.execute(table_emprendedores) #EJecuta statement para crear tabla "emprendedores"
create_table()

