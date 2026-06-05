import pandas as pd
import os

#poner rutas
ruta_script = os.path.dirname(__file__)
archivo = os.path.join(ruta_script, "Matriz_Captura_2023.xlsx")

#Cargar el archivo de excel
Data_Frame_2023=pd.read_excel(archivo, sheet_name='Matriz_captura',header=15)
Data_Frame_2023=Data_Frame_2023.dropna(how='all')
Data_Frame_2023=Data_Frame_2023.dropna(axis=1, how='all')
Data_Frame_2023=Data_Frame_2023.dropna(subset=['Cantidad ', 'Cantidad Muestra', 'ROOT'])
Data_Frame_2023["Tecnico"]=Data_Frame_2023["Tecnico"].fillna('Tecnico no especificado') 
Data_Frame_2023["Tecnico"] = (
    Data_Frame_2023["Tecnico"]
    .str.strip()      # elimina espacios al inicio y final
    .str.title()      # Convierte a formato Nombre Apellido
)
print(Data_Frame_2023["Tecnico"].value_counts())
print(Data_Frame_2023.isnull().sum()) 