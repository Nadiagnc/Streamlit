#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().system('pip install -q streamlit')


# In[34]:


import pandas as pd
import numpy as np
import plotly.express as px
import datetime
import streamlit as st


# In[35]:


st.set_page_config(layout="wide")


# In[36]:


Nagem=pd.read_csv(r"C:\Users\nadia\Downloads\RECLAMEAQUI_NAGEM.csv")


# In[37]:


st.write(Nagem)


# In[41]:


Localidade = st.sidebar.selectbox("Selecione a Localidade", Nagem["LOCAL"].unique())


# In[42]:


Ano = st.sidebar.selectbox("Selecione o ANO", Nagem["ANO"].unique())


# In[43]:


Mês = st.sidebar.selectbox("Selecione o ANO", Nagem["MES"].unique())


# In[44]:


Filtro = Nagem[Nagem["LOCAL"] == Localidade]


# In[45]:


st.write(Filtro)


# In[48]:


col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)


# In[54]:


fig = px.bar(Filtro, x="LOCAL", y="CASOS", color="LOCAL", title="Total de Casos")


# In[55]:


col1.plotly_chart(fig, use_container_width=True)


# In[30]:


if localidade !='FORTALEZA - CE':
  Reclamacao= Nagem[Nagem['LOCAL']==localidade]['CASOS'].count()
  Reclamacao

if localidade =='FORTALEZA':
  Reclamacao=Nagem['CASOS'].count()
  Reclamacao


# In[31]:


print("Para a localidade de ",localidade, "tem", Reclamacao, "Reclamações")


# In[32]:


if localidade !='FORTALEZA - CE':
  Status= Nagem[Nagem['LOCAL']==localidade]['STATUS'].value_counts()
  Status

if localidade =='FORTALEZA':
  Status=Nagem['STATUS'].value_counts()
  Status


# In[13]:


print("Para a localidade de ",localidade, "tem", Status, "Reclamações")


# In[ ]:





# In[29]:





# In[ ]:




