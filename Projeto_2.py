import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import time
import numpy as np


st.set_page_config(
     page_title="Análise exploratória previsão de renda",
     page_icon="C:/Users/Cris/Downloads/dados.png", #:?:
     layout="wide",
)

with st.spinner(text='Carregando... Aguarde!'):
    time.sleep(3)
    
st.write('# Análise exploratória previsão de renda')

#Lendo o arquivo csv
renda = pd.read_csv('C:/Users/Cris/Documents/Python Scripts/Curso/Projeto2/input/previsao_de_renda.csv')

renda.data_ref = pd.to_datetime(renda.data_ref)

min_data = renda.data_ref.min()
max_data = renda.data_ref.max()

#campos filtros de data:
data_inicial = st.sidebar.date_input('Data Inicial', 
                value = min_data,
                min_value = min_data,
                max_value = max_data)
data_final = st.sidebar.date_input('Data Final', 
                value = max_data,
                min_value = min_data,
                max_value = max_data)    

st.sidebar.write('Data Inicial = ', data_inicial)
st.sidebar.write('Data Final = ', data_final)
#Filtrando o dataset conforme a seleção das datas
renda  = renda[(renda['data_ref'] <= pd.to_datetime(data_final)) & (renda['data_ref'] >=pd.to_datetime(data_inicial) )]

with st.spinner(text='Carregando... Aguarde!'):
    time.sleep(3)

with st.container(border=True):
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.subheader('Proporção de Clientes por Sexo')
        #plt.figure(figsize=(0.5, 0.5))

        df_sexo = renda['sexo'].value_counts()
        data = [df_sexo['F'], df_sexo['M']]
        keys = ['Feminino', 'Masculino']

        palette_color = sns.color_palette('pastel')   
        fig = plt.pie(data, labels=keys, colors=palette_color, explode=[0, 0.1], autopct='%.0f%%')
        
        st.pyplot(fig=plt, clear_figure=True, use_container_width=True)
      
    with col2:
        st.subheader('Média Salárial por Sexo')
        #plt.figure(figsize=(1, 2))
        fig = sns.barplot(data=renda, x='sexo', y='renda')
        #plt.xticks(rotation=20)
        st.pyplot(fig=plt, clear_figure=True, use_container_width=True)
       
    
    with col3:
        st.subheader('Média Salárial por Escolaridade')
        fig = sns.barplot(data=renda, x='renda', y='educacao')
        st.pyplot(fig=plt, clear_figure=True, use_container_width=True)  

with st.container(border=True):
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.subheader('Quantidade de pessoas na mesma residência')
        fig = sns.countplot(data=renda, x='qt_pessoas_residencia')
        st.pyplot(fig=plt, clear_figure=True, use_container_width=True)  
      
    with col2:
        st.subheader('Quantidade de pessoas por Idade')
        fig = sns.histplot(renda['idade'], color='#A1C9F4', label='Idade', kde=False)
        plt.xticks(rotation=50)
        st.pyplot(fig=plt, clear_figure=True, use_container_width=True)  

    with col3:
        st.subheader('Média Salárial por Tipo de Renda')
        fig = sns.barplot(data=renda, x='tipo_renda', y='renda') 
        plt.xticks(rotation=20)
        st.pyplot(fig=plt, clear_figure=True, use_container_width=True)

with st.container(border=True):
    col1, col2, col3 = st.columns([1, 1, 1])
        
    with col1:
        st.subheader('Renda timeline')
        fig = sns.lineplot(x='data_ref',y='renda', data=renda)
        plt.xticks(rotation=20)
        st.pyplot(fig=plt, clear_figure=True, use_container_width=True)  
        
    with col2:
        st.subheader('Renda por Tempo de Emprego')
        fig = sns.scatterplot(data=renda, x="tempo_emprego", y="renda")
        st.pyplot(fig=plt, clear_figure=True, use_container_width=True)    
        
    with col3:
        st.subheader('Renda por Quantidade de filhos')
        fig = sns.scatterplot(data=renda, x="qtd_filhos", y="renda")
        st.pyplot(fig=plt, clear_figure=True, use_container_width=True)       
            
        
                 