import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import csv 
import random
import statistics

df = pd.read_csv("newdata.csv")
data=df["temp"].tolist()

def random_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()
def setup ():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean=statistics.mean(mean_list)
    print(mean)
setup()

def sd ():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_mean(100)
        mean_list.append(set_of_means)
    s_d=statistics.stdev(mean_list)
    print(s_d)
sd()           



