import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly 
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


dataset = pd.read_csv('covid_data.csv')



dataset = dataset[['Province_State','Country_Region','Confirmed','Recovered','Deaths','Active']]
dataset.columns= ('State','Country','Confirmed','Recovered','Deaths','Active')


dataset['State']=dataset['State'].fillna(value='')
print(dataset.isnull().sum())

#Top 10 most effected countires(Confirmed)

topcs = pd.DataFrame(dataset.groupby('Country')['Confirmed'].sum().sort_values(ascending=False).head(10))
print(topcs)
fig1 = px.scatter(topcs,x=topcs.index,y='Confirmed',size='Confirmed',size_max=120,color=topcs.index,title='Top 10 Confirmed Covid Effects Areas')
fig1.write_html('fig1.html',auto_open=True)



