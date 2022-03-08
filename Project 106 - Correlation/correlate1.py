import pandas
import plotly.express as pe
import numpy

# changing the data from a string (default) to a list
data = pandas.read_csv("CoffeevsSleep.csv")
coffee = data["Coffee in ml"].tolist()
sleep = data["sleep in hours"].tolist()

correlate = numpy.corrcoef(coffee, sleep)
print("Correlation: ", correlate[0,1])

graph = pe.scatter(data, x=coffee, y=sleep)
graph.show()