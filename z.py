import pandas as pd
import plotly.figure_factory as ff
import random
import statistics
import plotly.graph_objects as go

df=pd.read_csv("medium_data.csv")
data=df["id"].tolist()


def randomData(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

mean_list=[]
for i in range(100):
    for i in range(0,30):
        set_of_means=randomData(100)
        mean_list.append(set_of_means)


mean=statistics.mean(mean_list)
std=statistics.stdev(mean_list)

first_std_start, first_std_end = mean -std, mean+std
second_std_start, second_std_end=mean-(2*std), mean+std
third_std_start, third_std_end=mean-(3*std), mean+std

Nmean=statistics.mean(data)

fig=ff.create_distplot([mean_list], ["id"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[Nmean,Nmean],y=[0,0.17],mode="lines",name="mean1"))
fig.add_trace(go.Scatter(x=[first_std_end,first_std_end],y=[0,0.17],mode="lines",name="first std"))
fig.show()

z_score=(Nmean-mean)/std

print(z_score)