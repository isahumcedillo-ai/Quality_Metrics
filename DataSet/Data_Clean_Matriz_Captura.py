from email import header

import pandas as pd
import os

#poner rutas
ruta_script = os.path.dirname(__file__)

# Lista de años a procesar
encabezados = {

    2022: 5,
    2023: 15,
    2024: 1,
    2025: 5,
    2026: 6,  #  fila 7 en Excel = índice 6 en pandas (empieza desde 0)
}
# Procesar cada archivo según el año y su fila de encabezado correspondiente
for año, fila_header in encabezados.items():
    archivo = os.path.join(ruta_script, f"Matriz_Captura_{año}.xlsx")

    if not os.path.exists(archivo):
        print(f"[AVISO] No se encontró el archivo para {año}: {archivo}")   #Se envia mensaje en caso que no se encuwentre el archivo de Excel
        continue

    print(f"\nProcesando {año}...")

# Cargar el archivo Excel con la fila de encabezado específica para cada año
    df = pd.read_excel(archivo, sheet_name='Matriz_captura', header=fila_header)

# Eliminar filas y columnas completamente vacías, y limpiar espacios en los nombres de las columnas
    df = df.dropna(how='all')
    df = df.dropna(axis=1, how='all')

# Limpiar espacios en los nombres de las columnas y eliminar filas con valores nulos en columnas clave
    df.columns = df.columns.str.strip()
    df = df.dropna(subset=['Cantidad', 'Cantidad Muestra', 'ROOT'])

# Rellenar valores nulos en columnas específicas con texto descriptivo o 'N/A'
    df["Tecnico"] = df["Tecnico"].fillna('Tecnico no especificado').str.strip().str.title()
    df["Categoría"] = df["Categoría"].fillna('Categoría no especificada')
    df["Nombre del Supervisor"] = df["Nombre del Supervisor"].fillna('Supervisor no especificado')
    df["Componente afectado"] = df["Componente afectado"].fillna('Componente no especificado')

# Rellenar columnas de folios con 'N/A' y limpiar espacios si existen
    if "Folio de Warning?" in df.columns:
        df["Folio de Warning?"] = df["Folio de Warning?"].fillna('N/A').str.strip()

    if "Folio de process Audit?" in df.columns:
        df["Folio de process Audit?"] = df["Folio de process Audit?"].fillna('N/A')

# Guardar el DataFrame limpio en un nuevo archivo Excel
    archivo_limpio = os.path.join(ruta_script, f"Matriz_Captura_{año}_Limpia.xlsx")
    df.to_excel(archivo_limpio, index=False)

# Mostrar resumen de nulos restantes y confirmación de guardado
    print(f"Nulos restantes ({año}):")
    print(df.isnull().sum())
    print(f"✔ Guardado: {archivo_limpio}")


#print(Data_Frame["Tecnico"].value_counts())
#print(Data_Frame["Componente afectado"].value_counts())
#print(Data_Frame["Folio de Warning?"].value_counts())
#print(Data_Frame["Folio de process Audit?"].value_counts())
#print(Data_Frame.columns.tolist())
#print(Data_Frame.isnull().sum())