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

#renombrar columnas
df_detalles_por_ejecutivo=df_detalles_por_ejecutivo.rename(columns={'Ver':'N Pedido','Proveedor':'Nombre del proveedor','Estado':'Estado Pedido','Total del pedido':'presupuesto pedido','requision':'ID Orden de Compra'})

# Integración de tablas 
df_integrados=pd.merge(df_detalles_por_articulo,df_detalles_por_ejecutivo,on='N Pedido',how='left')

#guardar dataframe consolidado en un archivo csv
df_integrados.to_csv('./df_datos_integrados.csv')