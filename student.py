print("Student Performances Stats")
import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go
import statistics
import random

df=pd.read_csv("data.csv")
data=df["reading score"].tolist()
mean=sum(data)/len(data)
SD = statistics.stdev(data)
median= statistics.median(data)
mode=statistics.mode(data)

SDstart1,SDend1=mean-SD,mean+SD
SDstart2,SDend2=mean-(2*SD),mean+(2*SD)
SDstart3,SDend3=mean-(3*SD),mean+(3*SD)

list_of_data_within_1_SD=[result for result in data if result> SDstart1 and result <SDend1]
list_of_data_within_2_SD=[result for result in data if result> SDstart2 and result <SDend2]
list_of_data_within_3_SD=[result for result in data if result> SDstart3 and result <SDend3]

print("Mean is {}".format(mean))
print("Median is {}".format(median))
print("Mode is {}".format(mode))
print("Standard deviation is {}".format(SD))

print("{}% of data lies within 1st standard deviation.".format(len(list_of_data_within_1_SD)*100.0/len(data)))
print("{}% of data lies within 2nd standard deviation.".format(len(list_of_data_within_2_SD)*100.0/len(data)))
print("{}% of data lies within 3rd standard deviation.".format(len(list_of_data_within_3_SD)*100.0/len(data)))

fig=ff.create_distplot([data], ["reading scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17], mode="lines", name= "MEAN"))
fig.add_trace(go.Scatter(x=[SDstart1, SDstart1], y=[0, 0.17], mode="lines", name="Standard Deviation 1 start"))
fig.add_trace(go.Scatter(x=[SDend1, SDend1], y=[0, 0.17], mode="lines", name="Standard Deviation 1 end"))
fig.add_trace(go.Scatter(x=[SDstart2, SDstart2], y=[0, 0.17], mode="lines", name="Standard Deviation 2 start"))
fig.add_trace(go.Scatter(x=[SDend2, SDend2], y=[0, 0.17], mode="lines", name="Standard Deviation 2 end"))
fig.add_trace(go.Scatter(x=[SDstart3, SDstart3], y=[0, 0.17], mode="lines", name="Standard Deviation 3 start"))
fig.add_trace(go.Scatter(x=[SDend3, SDend3], y=[0, 0.17], mode="lines", name="Standard Deviation 3 end"))
fig.show()