import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("School3.csv")
data = df["Math_score"].tolist()
fig = ff.create_distplot([data],["Math Scores"], show_hist= False)
#fig.show()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print("\n")
print("mean of popultion : ",mean)
print("Standard deviation of popultion : ",std_deviation)

def randomSetOfMeans(counter):
     dataset = []
     for i in range(0, counter):
          random_index= random.randint(0,len(data)-1)
          value = data[random_index]
          dataset.append(value)
     mean = statistics.mean(dataset)
     return mean

mean_list = []
for i in range(0,1000):
    set_of_means= randomSetOfMeans(100)
    mean_list.append(set_of_means)

std = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)

print("\n")
print("mean of sampling distribution : ",mean)
print("Standard deviation of sampling distribution : ", std)

first_std_start, first_std_end = mean - std, mean + std
second_std_start, second_std_end = mean - (2*std), mean + (2*std)
third_std_start, third_std_end = mean -(3*std), mean + (3*std)

fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines+markers",name="Mean"))
#fig.show()


df = pd.read_csv("School_1_Sample.csv")
data = df["Math_score"].tolist()
meanOfSample1 = statistics.mean(data)

print("\n")
print("Mean of Sample 1: ",meanOfSample1)

fig = ff.create_distplot([mean_list],["Student Marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines+markers",name="Mean"))
fig.add_trace(go.Scatter(x=[meanOfSample1,meanOfSample1],y=[0,0.17],mode="lines+markers",name="Mean of student had math lab"))
fig.add_trace(go.Scatter(x=[first_std_end,first_std_end],y=[0,0.17],mode="lines+markers",name="First std end"))
fig.add_trace(go.Scatter(x=[second_std_end,second_std_end],y=[0,0.17],mode="lines+markers",name="Second std end"))
fig.add_trace(go.Scatter(x=[third_std_end,third_std_end],y=[0,0.17],mode="lines+markers",name="Third std end"))
#fig.show()


df = pd.read_csv("School_2_Sample.csv")
data = df["Math_score"].tolist()
meanOfSample2 = statistics.mean(data)

print("Mean of Sample 2: ",meanOfSample2)

fig = ff.create_distplot([mean_list],["Student Marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines+markers",name="Mean"))
fig.add_trace(go.Scatter(x=[meanOfSample2,meanOfSample2],y=[0,0.17],mode="lines+markers",name="Mean of student had math app"))
fig.add_trace(go.Scatter(x=[first_std_end,first_std_end],y=[0,0.17],mode="lines+markers",name="First std end"))
fig.add_trace(go.Scatter(x=[second_std_end,second_std_end],y=[0,0.17],mode="lines+markers",name="Second std end"))
fig.add_trace(go.Scatter(x=[third_std_end,third_std_end],y=[0,0.17],mode="lines+markers",name="Third std end"))
#fig.show()


df = pd.read_csv("School_3_Sample.csv")
data = df["Math_score"].tolist()
meanOfSample3 = statistics.mean(data)

print("Mean of Sample 3: ",meanOfSample3)

fig = ff.create_distplot([mean_list],["Student Marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines+markers",name="Mean"))
fig.add_trace(go.Scatter(x=[meanOfSample3,meanOfSample3],y=[0,0.17],mode="lines+markers",name="Mean of student had enforced with registers"))
fig.add_trace(go.Scatter(x=[first_std_end,first_std_end],y=[0,0.17],mode="lines+markers",name="First std end"))
fig.add_trace(go.Scatter(x=[second_std_end,second_std_end],y=[0,0.17],mode="lines+markers",name="Second std end"))
fig.add_trace(go.Scatter(x=[third_std_end,third_std_end],y=[0,0.17],mode="lines+markers",name="Third std end"))
#fig.show()

print("\n")
zscore1 = (meanOfSample1 - mean) / std
print("z score for the first group:", zscore1)

zscore2 = (meanOfSample2 - mean) / std
print("z score for the second group:", zscore2)

zscore3 = (meanOfSample3 - mean) / std
print("z score for the third group:", zscore3)

print("\n")

# The first group had no impact, the second one had slight impact.
# The third group had the most impact.