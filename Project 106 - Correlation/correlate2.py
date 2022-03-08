import numpy as n
import plotly.express as pe
import pandas as px

data = px.read_csv("StudentvsDays.csv")
marks = data["Marks In Percentage"].tolist()
present = data["Days Present"].tolist()
graph = pe.scatter(data, x=present, y=marks)
graph.show()
correlate = n.corrcoef(present, marks)
print("Correlation: ", correlate[0,1])