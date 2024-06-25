import csv
import pandas as pd
import matplotlib.pyplot as mp
import os
os.system ("cls")
with open ("inversores.csv", "r") as csv_file:
    csv_reader = csv.reader (csv_file)

#Lee los archivos CSV 
df_inv= pd.read_csv ("inversores.csv", sep=",")
df_emp=pd.read_csv ("emprendedores.csv", sep=",")

paises=df_inv["pais"] #Selecciona la columna "Pais" de la tabla de inversores
capitales=df_inv["capital_a_invertir"]
inversores_argentinos=0
inversores_restodelmundo=0
inversores_brasil=0
inversores_uruguay=0
inversores_chile=0
inversores_ecuador=0
capital_arg=0
capital_brasil=0
capital_uruguay=0
capital_ecuador=0
capital_chile=0

#Suma la cantidad de inversores argentinos y del resto de latam
#Suma el capital a invertir segun pais 
for pais in paises:
    if pais=="Argentina":
        inversores_argentinos+=1
    else:
        inversores_restodelmundo+=1
for index, row in df_inv.iterrows():
    pais = row['pais']
    capital = row['capital_a_invertir']
    if pais == "Argentina":
        inversores_argentinos += 1
        capital_arg += capital
    elif pais =="Brasil":
        inversores_brasil+=1
        inversores_restodelmundo += 1
        capital_brasil += capital
    elif pais =="Uruguay":
        inversores_uruguay+=1
        inversores_restodelmundo += 1
        capital_uruguay += capital  
    elif pais=="Ecuador":
        inversores_ecuador+=1
        inversores_restodelmundo += 1
        capital_ecuador+= capital
    elif pais=="Chile":
        inversores_chile+=1
        inversores_restodelmundo += 1
        capital_chile+= capital
    else:
        inversores_restodelmundo += 1

#Crea un diccionario que compara cantidad de inversores segun region
q_inversores={"Regiones" : ["Argentina", "Resto de LATAM"],
              "Cantidad de inversores" : [inversores_argentinos, inversores_restodelmundo]}
#Convierte al diccionario en un DataFrame (Tabla de Pandas)
df1=pd.DataFrame (q_inversores)
#Creas el grafico
grafico_q=df1.plot(kind="pie", x= "Regiones", y= "Cantidad de inversores", title="Cantidad de inversores segun region: ",labels=df1["Regiones"],autopct="%0.1f %%") #representa que mercado de inversores penetro mas
mp.show()

#Creas un diccionario que compara cantidad de inversores y capital segun pais
capital_paises= {"Paises": ["Argentina", "Brasil", "Uruguay", "Ecuador", "Chile"],
                 "Cantidad de inversores": [inversores_argentinos,inversores_brasil, inversores_uruguay, inversores_ecuador, inversores_chile],
                 "Capital": [capital_arg, capital_brasil, capital_uruguay,capital_ecuador,capital_chile]}
#Convierte al diccionario en un DataFrame
df2=pd.DataFrame(capital_paises)
colores = {
    "Argentina": "lightblue",
    "Uruguay": "lightblue",
    "Brasil": "yellow",
    "Ecuador": "yellow",
    "Chile": "red"
}
df2['Color'] = df2['Paises'].map(colores)

#Creas el grafico que compara capital segun pais y muestra cuantos inversores tiene cada pais
grafico_q=df2.plot(kind="bar", x= "Paises", y= "Capital", title="Capital a invertir por paises: ", color= df2["Color"]) 
for index, row in df2.iterrows():
    grafico_q.text(index, row['Capital'], f'Inversores: {row["Cantidad de inversores"]}', color='black', ha="center")
mp.show()

#Calcula medidas de dispersion varianza y media de Capital y Valuacion
capital_medio=df_inv["capital_a_invertir"].mean()
valuacion_media=df_emp["valuacion"].mean()
varianza_capital=df_inv["capital_a_invertir"].var()
varianza_valuacion=df_emp["valuacion"].var()

print(f"Valuacion media: {valuacion_media}")
print (f"Capital medio: {capital_medio}")

print(f"Varianza de la valuacion: {varianza_valuacion}") #Varianza Alta= Rango amplio de los negocios
print (f"Varianza del capital: {varianza_capital}")#Varianza alta= Rango amplio de inversores


indicadores = ['Capital Medio', 'Valuación Media']
valores = [capital_medio, valuacion_media]

#Creas el grafico que compara Valuacion media vs Capital medio
mp.figure(figsize=(6, 4))  # Tamaño opcional del gráfico
mp.bar(indicadores, valores, color=['blue', 'green'])
mp.ylabel('Valor')
mp.title('Capital medio vs Valuacion media:')
mp.show()