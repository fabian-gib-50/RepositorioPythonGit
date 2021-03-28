import pandas as pd
import plotly.express as px
import numpy as np
import geopandas as gpd
import pendulum
import pydot
import inflection
from matplotlib import pyplot as plt ###pyplot(classe)desenha o gráfico, que esta na biblioteca matplotlib(pasta)######
from datetime import datetime

data = pd.read_csv('datasets/kc_house_data.csv')
data['date'] = pd.to_datetime(data['date'])
pd.set_option('display.float_format', lambda x: '%.3f' % x)
print(pendulum.datetime(1969,9,2).age)
#######################################################################
# AULA - 02 PERGUNTAS DO CEO ROCKET HOUSE EMPREENDIMENTOS
#######################################################################
# 1.	Qual a data do imóvel mais antigo do portfólio?
# print(data.sort_values('date',ascending=True)) #Ordem decrescente
# print( data.sort_values( 'date', ascending=False )) Ordem crescente
# print(data.head)
#######################################################################
# 2 -perfunta: Quantos imóveis têm o número máximo de andares?
# print(data.columns)
# print( data['floors'].unique())
# print(data.floors) ==3.5
# # print( data[data['floors'] == 3.5][['floors','id']] )
# # print( data[data['floors'] ==3.5].shape )
#######################################################################
# 3 - Criar uma classificação para os imóveis, separando-os em baixo e alto padrão, de acordo com o preço.
# Acima de R$ 540.000 -> alto padrão (high_standard)
# Abaixo de R$ 540.000 -> baixo padrão (standard)
# R: Criar uma nova coluna no conjunto de dados chamada (Standard)
#     - para cada linha eu comparo a coluna “price”
# Se “price” for maior que 540.000, eu escrevo “high_standard” na coluna “standard”
# Se “price” for maior que 540.000, eu escrevo “low_standard” na coluna “standard”
# data['level'] = "null"
# # print(data.columns)
# data.loc[data['price'] > 540000, 'level'] = 'high_level'
# data['level'] = "standard"
# data.loc[data['price'] > 540000, 'level'] = 'high_level'
# data.loc[data['price'] < 540000, 'level'] = 'low_level'
# print(data.head(10))
#######################################################################
# print(data.describe())
# print(df2.shape)
# data_mapa = data[['id', 'lat', 'long', 'price']]
# mapa=px.scatter_mapbox( data_mapa, lat='lat', lon='long',
#                   hover_name=
#                   'id',
#                   hover_data=
#                   ['price'],
#                   color_discrete_sequence=
#                   ['red'],
#                   zoom=7,
#                   height=300 )
# mapa.update_layout( mapbox_style=
#                   'open-street-map')
# mapa.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0})
# mapa.show()
# print(data.describe())
# print(data.head())
print(data.columns.tolist)
#######################################################################
#soma listas exercicios - dataframe
#######################################################################
# Distritos = {'distritos':['local1','local2'],'2017':[30,40],'2018':[50,60]}
# Blumenau = pd.DataFrame(data=Distritos)
# print(Blumenau)
# print(data['date'].unique)