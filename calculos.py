from operator import index, itemgetter
from select import select
#from tkinter import N
from zoneinfo import available_timezones
import pandas as pd
import itertools
from math import isnan


## Carga de dataframes
frameworkPatterns = pd.read_csv(r'C:/Users/juanj/OneDrive/Desktop/microAzimutTesting-rama/microAzimutTesting-rama/proyectoMicroAzimut/datasets/frameworkPatterns.csv', delimiter= ';', index_col='index')
tacticsPatterns = pd.read_csv(r'C:/Users/juanj/OneDrive/Desktop/microAzimutTesting-rama/microAzimutTesting-rama/proyectoMicroAzimut/datasets/tacticsPatterns.csv', delimiter= ';', index_col='index',na_values='-')
properties = pd.read_csv(r'C:/Users/juanj/OneDrive/Desktop/microAzimutTesting-rama/microAzimutTesting-rama/proyectoMicroAzimut/datasets/Properties.csv', delimiter= ';', index_col='index', na_values='nan')

## Comienzo de proceso de filtrado de properties
properties_dict=properties.transpose().to_dict(orient='list')
properties_empty={}
for key in properties_dict:
    properties_empty[key]=[]
    for value in properties_dict[key]:   
        if isinstance(value, str):
            properties_empty[key].append(value)


## Función para elegir las columnas para el primer cálculo
def selector(df,filter,alf):
    df=df[filter]
    df=(df>=alf).sum(axis=1)
    df=df[df>0]
    return df.index.values.tolist()

## Contador de columnas del dataframe no nulas
def cuenta_columnas(df):
    contador=df.notnull().sum(axis=1)
    return contador

## Calculo de las columnas que pasaron la selección en C1
def c1 (df,alf):
    df_filtrado_fil=(df >= alf).sum(axis=1)/cuenta_columnas(df)
    df_filtrado_fil=df_filtrado_fil[df_filtrado_fil>0]
    return df_filtrado_fil

## Cálculo 2 a partir de los resultados de C1
def c2 (df_filtrado,beta):

    patterns=df_filtrado.index.values.tolist()
    frameworks=frameworkPatterns[patterns]
    df_frameworks_filtrado=(frameworks >= beta)
    df_frameworks_valores=df_frameworks_filtrado.mul(df_filtrado,axis=1)
    df_frameworks_valores=df_frameworks_valores.sum(axis=1)/len(frameworkPatterns.columns)
    df_frameworks_valores=df_frameworks_valores[df_frameworks_valores>0]
    return df_frameworks_valores

## Cálculo final de las combinaciones existentes
def c3(df):
    resultados_opciones=df.index.values.tolist()
    i=1
    combinaciones=[]
    valores=[]
    while i <=4:
        for comb in itertools.combinations(resultados_opciones,i):
            combinaciones.append(' - '.join(comb))
            df_comb=df.filter(items=comb).mean()
            valores.append(df_comb)
        i+=1
    return combinaciones,valores

## Llamados a funciones
def df_salida ():
    Lista_Propiedades = []
    file = open(r'lista.txt','r')

    for x in file:
        Lista_Propiedades = x.strip().split(",")
  
    file.close()

    Crea_Lista_Calculos=[]
    for key in Lista_Propiedades:
        Crea_Lista_Calculos.append(properties_empty[key])
    filtro=list(set(itertools.chain(*Crea_Lista_Calculos)))
    dataframe_salida=c1(tacticsPatterns,0.6)
    filtro_pruebas=selector(tacticsPatterns,filtro,0.6)
    filtrado=dataframe_salida.filter(items=filtro_pruebas)
    resultado= c2(filtrado,0.6)
    combinaciones,valores=c3(resultado*1000)

    df=pd.DataFrame({'Combinations':combinaciones,'Support Score':valores})
    df.sort_values(by=['Support Score'],inplace=True,ascending=False)
    df_salida=df.head(10)
    print(df)
    #print(df_salida.to_html())
    return df_salida.to_html

salida = df_salida()
