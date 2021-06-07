from os import name
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics 

count=[]
dice_result=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)
    count.append(i)

mean=statistics.mean(dice_result)
print("mean is :"+ str (mean))

median=statistics.median(dice_result)
print("median is :"+str (median))

mode=statistics.mode(dice_result)
print("mode is :"+str (mode))

sd=statistics.stdev(dice_result)
print("stardand divesion is :"+str(sd))

first_sd_start,first_sd_end=mean-sd,mean+sd
second_sd_start,second_sd_end=mean-(2*sd),mean+(2*sd)
third_sd_start,third_sd_end=mean-(3*sd),mean+(3*sd)

fig=ff.create_distplot([dice_result],["result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[first_sd_start,first_sd_start],y=[0,0.17],mode="lines",name="sd1"))
fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.17],mode="lines",name="sd1"))

fig.add_trace(go.Scatter(x=[second_sd_start,second_sd_start],y=[0,0.17],mode="lines",name="sd2"))
fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.17],mode="lines",name="sd2"))

fig.add_trace(go.Scatter(x=[third_sd_start,third_sd_start],y=[0,0.17],mode="lines",name="sd3"))
fig.add_trace(go.Scatter(x=[third_sd_end,third_sd_end],y=[0,0.17],mode="lines",name="sd3"))
fig.show()

list_1=[result for result in dice_result if result>first_sd_start and result<first_sd_end]
list_2=[result for result in dice_result if result>second_sd_start and result<second_sd_end]
list_3=[result for result in dice_result if result>third_sd_start and result<third_sd_end]
#print("{}% of data lies in 1sd".format(len(list_1)*100.0/len(dice_result)))
#print("{}% of data lies in 2sd".format(len(list_2)*100.0/len(dice_result)))
#print("{}% of data lies in 3sd".format(len(list_3)*100.0/len(dice_result)))