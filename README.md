# 🚗 Análisis de KPIs de Calidad - Manufactura Automotriz

📌 Descripción del Proyecto

Este proyecto consiste en el desarrollo de una solución integral de análisis de datos para el monitoreo de los Indicadores Clave de Rendimiento (KPIs) de Calidad en una planta de manufactura de autopartes. 

Utilizando un enfoque híbrido, se desarrolló un script en Python para la automatización del proceso de ETL (extracción, limpieza y normalización) de las matrices de captura manuales de la empresa, para posteriormente modelar y diseñar un dashboard interactivo en Power BI que abarca el histórico desde el año 2022 a la fecha.

🎯 Objetivos

* Automatizar la limpieza y unificación de las bases de datos de calidad (2022-2026).
* Monitorear el comportamiento de las tasas de defectos en la producción de autopartes.
* Identificar los componentes automotrices con mayor frecuencia de fallas.
* Evaluar el desempeño operativo mediante el análisis de incidencias por técnico y supervisor.
* Facilitar la toma de decisiones basada en datos para auditorías de proceso y alertas de calidad.

🛠️ Herramientas Utilizadas

* Power BI Desktop (Modelado y Visualización)
* Python & Pandas (ETL y Automatización de limpieza)
* DAX (Data Analysis Expressions para métricas dinámicas)
* Microsoft Excel (Orígenes de datos)
* Git & GitHub (Control de versiones)

📊 Indicadores Analizados

* **Tasa de Defectos:** Volumen total de producto afectado.
* **Componentes Afectados:** Frecuencia e impacto por tipo de autoparte.
* **Análisis de Raíz (ROOT):** Clasificación del origen de las fallas encontradas.
* **Trazabilidad de Auditorías:** Monitoreo y estatus de folios de *Warning* y *Process Audit*.
* **Productividad por Turno/Personal:** Desempeño y registro de incidencias por Técnico y Supervisor.

📂 Estructura del Proyecto

QUALITY_METRICS/
│
├── QUALITY REPORT.pbix  # Archivo de Power BI
├── Data_Clean_Matriz_Captura.py   # Script de limpieza en Python
├── README.md
│
├── Dataset/
│   ├── Matriz_Captura_2022.xlsx  # Orígenes de datos anuales (Raw)
│   └── ..._Limpia.xlsx           # Datos procesados por Python
│
└── Screenshots/
    └── Capturas del dashboard interactivo

📈 Proceso de Análisis

1. **ETL con Python:** Conexión a múltiples matrices de Excel, detección dinámica de encabezados según el año, remoción de acentos/espacios (`.strip()`) y estandarización de variables de texto.
2. **Filtrado de Calidad:** Depuración de registros nulos en columnas críticas como 'Cantidad' y 'ROOT'.
3. **Modelado en Power BI:** Creación del modelo relacional a partir de los archivos limpios de Python.
4. **Desarrollo DAX:** Creación de medidas y cálculos dinámicos para el análisis de tendencias.
5. **Diseño Visual:** Estructuración de un dashboard intuitivo enfocado en la toma de decisiones de manufactura.

📷 Dashboard

Las capturas de las diferentes pestañas del dashboard se encuentran en la carpeta:
`Screenshots/`

💡 Hallazgos Principales

* Identificación de los componentes críticos que generan el mayor porcentaje de rechazo en la línea.
* Reducción del tiempo de preparación de datos gracias a la automatización del script de Python.
* Visibilidad clara sobre el estatus de los folios de auditorías pendientes por cerrar.
* Comparativa del comportamiento histórico de fallas año con año.

👨‍💻 Autor

Isaac Cedillo
Técnico de Calidad Automotriz | Analista de Datos en formación | Power BI | SQL | Python
GitHub: [isahumcedillo-ai](https://github.com/isahumcedillo-ai)
