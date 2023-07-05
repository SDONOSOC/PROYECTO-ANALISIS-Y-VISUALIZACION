#importar libreria
import pandas as pd

#cargar dataset  archivo por articulo
df_detalles_por_articulo=pd.read_csv(r'./OC_DETALLADAS_POR_ARTCULOS_AL_31052023.csv',encoding='utf-8',sep = ';')
#mostrar los primeros 5 resultado
print(df_detalles_por_articulo.head(5))

#cargar dataset por ejecutivo
df_detalles_por_ejecutivo= pd.read_csv(r'./OC_DETALLADAS_POR_EJECUTIVO_Y_OC_AL_31052023.csv',encoding='utf-8',sep = ';')
#mostrar los primeros 5 resultados
print(df_detalles_por_ejecutivo.head(5))

#Listar el nombre de las columnas del dataset por ejecutivos
print(df_detalles_por_ejecutivo.columns)

#Listar el nombre de las columnas del dataset por articulos
print(df_detalles_por_articulo.columns)