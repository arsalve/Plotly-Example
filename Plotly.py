import pandas as pd
import plotly.graph_objects as go 
import plotly.offline as pyo 
df= pd.read_csv(r"hungary_chickenpox.csv")
df=df.assign(total=lambda x : df.sum(axis=1))
odf=df.drop(df.columns[-1],axis = 1).plot.line()
da=[]
for i in df.columns[1:-2]:
   da.append(go.Scatter(x=df[df.columns[0]],y=df[i],name=i,mode='markers')) #you can cahnge the type of graph here
pyo.plot({
    "data": da,
    "layout": go.Layout(title="Total Victems")
}) 
