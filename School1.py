import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("School1.csv")
data = df["Math_score"].tolist()
fig = ff.create_distplot([data],["Math Scores"], show_hist=False)
# fig.show()

mean = statistics.mean(data)
std = statistics.stdev(data)

print("\n")
print("Mean of population: ", mean )
print("Standard deviation of population:", std)

def randomSetofMeans(counter):
    dataset = []
    for i in range(0, counter):
          random_index= random.randint(0,len(data)-1)
          value = data[random_index]
          dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means = randomSetofMeans(30)
    mean_list.append(set_of_means)

std = statistics.mean(mean_list)
mean = statistics.mean(mean_list)

print("\n")
print("mean of sampling distribution : ",mean)
print("Standard deviation of sampling distribution : ", std)

first_std_start, first_std_end = mean - std, mean + std
second_std_start, second_std_end = mean - (2*std), mean + (2*std)
third_std_start, third_std_end = mean -(3*std), mean + (3*std)

fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines+markers",name="Mean"))

# fig.show()


df = pd.read_csv("School_1_Sample.csv")
data = df["Math_score"].tolist()
meanOfSample1 = statistics.mean(data)

print("\n")
print("Mean of Sample 1: ",meanOfSample1)

fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines+markers",name="Mean"))

fig.add_trace(go.Scatter(x=[meanOfSample1,meanOfSample1],y=[0,0.17],mode="lines+markers",name="Mean of Sample 1"))
fig.add_trace(go.Scatter(x=[first_std_end,first_std_end],y=[0,0.17],mode="lines+markers",name="Std 1 end"))
fig.add_trace(go.Scatter(x=[second_std_end,second_std_end],y=[0,0.17],mode="lines+markers",name="Std 2 end"))
fig.add_trace(go.Scatter(x=[third_std_end,third_std_end],y=[0,0.17],mode="lines+markers",name="Std 3 end"))

# fig.show()

df = pd.read_csv("School_2_Sample.csv")
data = df["Math_score"].tolist()
meanOfSample2 = statistics.mean(data)

print("Mean of Sample 2: ",meanOfSample2)

fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines+markers",name="Mean"))

fig.add_trace(go.Scatter(x=[meanOfSample2,meanOfSample2],y=[0,0.17],mode="lines+markers",name="Mean of Sample 1"))
fig.add_trace(go.Scatter(x=[first_std_end,first_std_end],y=[0,0.17],mode="lines+markers",name="Std 1 end"))
fig.add_trace(go.Scatter(x=[second_std_end,second_std_end],y=[0,0.17],mode="lines+markers",name="Std 2 end"))
fig.add_trace(go.Scatter(x=[third_std_end,third_std_end],y=[0,0.17],mode="lines+markers",name="Std 3 end"))

# fig.show()

df = pd.read_csv("School_3_Sample.csv")
data = df["Math_score"].tolist()
meanOfSample3 = statistics.mean(data)

print("Mean of Sample 3: ",meanOfSample3)

fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines+markers",name="Mean"))

fig.add_trace(go.Scatter(x=[meanOfSample3,meanOfSample3],y=[0,0.17],mode="lines+markers",name="Mean of Sample 1"))
fig.add_trace(go.Scatter(x=[first_std_end,first_std_end],y=[0,0.17],mode="lines+markers",name="Std 1 end"))
fig.add_trace(go.Scatter(x=[second_std_end,second_std_end],y=[0,0.17],mode="lines+markers",name="Std 2 end"))
fig.add_trace(go.Scatter(x=[third_std_end,third_std_end],y=[0,0.17],mode="lines+markers",name="Std 3 end"))

# fig.show()

print("\n")
z_score1 = (meanOfSample1 - mean) / std
print("The z score of sample 1 is: ", z_score1)

z_score2 = (meanOfSample2 - mean) / std
print("The z score of sample 2 is: ", z_score2)

z_score3 = (meanOfSample3 - mean) / std
print("The z score of sample 3 is: ", z_score3)

print("\n")

# All the groups had very less impacts.
# But the third group had the most impact between the three.