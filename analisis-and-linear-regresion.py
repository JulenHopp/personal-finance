# -*- coding: utf-8 -*-
"""Copia de Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12mAsPLUhDacxr3U6LQDRBdBBmzPczMW4
"""

import pandas as pd #Importando la libreria de pandas para poder utilizarla

df = pd.read_excel('/content/sample_data/Datos.xlsx') #Creando nuestro dataFrame con la base de datos

df.head()#Esta nos devuelve los 5 primeras filas de nuestro dataFrame para ver si lo creamos correctamente

df = df.iloc[:,3:9] #Creando un nuevo DataFrame pero solo con las columas del 3 al 9
                    #costos, presupuesto, tiempo invertido, tipo, momento, y numero de personas

df.head()#Un despliegue rapido del nuevo dataFrame

df.info()#Para ver las caracteristicas y tipos de datos que contiene el dataFrame

df.isnull().sum()#Este nos checa cuantos datos faltantes tenemos

df = df.dropna()#dropna remeuve todas las filas que contengan algun dato vacio

df.isnull().values.any()#Con isnull estamos checando que casillas estan vacias
                        #con values agarrando solo los valores que en este caso es falso en todos
                        #porque ya depueramos los datos vacios y con any()checamos que todos los datos
                        #sean falsos en caso de haber algun verdadero este nos mostraria true porque
                        #si hay datos vacios

df.columns#Mostrando que columnas tenemos

#Aqui creamos 2 matrices:
#* x que contiene los valores las columnas de presupuesto, tiempo, tipo, momento y
# numero de personas que van a funcionar como variables de entradas
#* y que contiene los valores de la columna de costo que va a funcionar como la variable dependiente

x = df[['Presupuesto', 'Tiempo invertido', 'Tipo', 'Momento', 'No. de personas']].values # variables independientes
y = df['Costo'].values # variable dependiente


from sklearn.model_selection import train_test_split# importamos libreria para dividir los datos

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)#separamos los datos
y_test# desplegamos los valores de prrueba que nos arrojo el test

from sklearn.linear_model import LinearRegression#Importamos libreria para realizar la regresion lineal

model_regression = LinearRegression()# creamos un objeto con la funcion de regresion lineal

model_regression.fit(x_train, y_train)# le damos los datos a nuestro modelo de regresion

#creamos dataframes con los nombres de las variables en x y los coeficientes de neustra ecuacion
x_labels = ['Presupuesto', 'Tiempo invertido', 'Tipo', 'Momento', 'No. de personas']
c_label = ['Coeficientes']

coeff_df = pd.DataFrame(model_regression.coef_, x_labels, c_label)#organizamos los coeficientes en un dataFRrame
coeff_df#Desplegamos en panatalla los coeficientes

y_pred = model_regression.predict(x_test) # realiza la predicción con el modelo generado

#Creamos e imprimimos en pantalla un data frame con los reciduos
residuals = pd.DataFrame({'Real': y_test, 'Predicción': y_pred, 'Residual': y_test - y_pred})
residuals = residuals.sample(n =  28)
residuals = residuals.sort_values(by='Real')
residuals

from sklearn.metrics import r2_score
r2_score(y_test, y_pred)# generamos el coeficiente de determinacion

# Commented out IPython magic to ensure Python compatibility.
#validamos los datos graficando con matplotlib
import matplotlib.pyplot as plt # importamos la librería pyplot que nos permitirá graficar
import numpy as np # importamos la librería numpy que nos permitirá crear un arreglo para la muestra de 30 datos

# función mágica para desplegar el gráfico en nuestra libreta
# %matplotlib inline

plt.scatter(np.arange(28), residuals['Real'], label = "Real")  # creamos el gráfico con la muestra de datos reales
plt.scatter(np.arange(28), residuals['Predicción'], label = "Predicción")  # creamos el gráfico con la muestra de datos de predicción

plt.title("Comparación de costos: Reales y Predicción") # indicamos el título del gráfico

plt.xlabel("28 observaciones de costos") # indicamos la etiqueta del eje de las x

plt.ylabel("Costos") # indicamos la etiqueta del eje de las y

plt.legend(loc='upper left') # indicamos la posición de la etiqueta de los datos

plt.show() # desplegamos el gráfico

"""# Evaluando mis finanzas

"""

import pandas as pd #Importando neuvamente la libreria de pandas para poder utilizarla

df = pd.read_excel('/content/sample_data/Datos.xlsx') #Creando nuestro dataFrame con la base de datos

df.describe()#Generando un analisis descriptivo de mi base de datos

df.describe().loc[df.describe()['Presupuesto'].idxmax()]

df.describe().loc[df.describe()['Presupuesto'].idxmin()]

df.groupby('Tipo').sum()

df['Fecha (dd/mm/aa)'].nunique()

df['Costo'].sum()

df['Tipo'].value_counts()

df_comida  = df[df['Tipo'] == 1].reset_index(drop=True)

df_comida['Costo'].sum()

objetivo = 15000
print((objetivo - df_comida['Costo'].sum())/(df_comida['Costo'].sum()/30))