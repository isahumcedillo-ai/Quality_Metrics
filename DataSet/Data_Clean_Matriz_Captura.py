import pandas as pd
import os

#poner rutas
ruta_script = os.path.dirname(__file__)
archivo = os.path.join(ruta_script, "Matriz_Captura_2023.xlsx")

#Cargar el archivo de excel
Data_Frame_2023=pd.read_excel(archivo, sheet_name='Matriz_captura',header=15)
Data_Frame_2023=Data_Frame_2023.dropna(how='all')
print(Data_Frame_2023.isnull().sum()) 
print(Data_Frame_2023.columns)
