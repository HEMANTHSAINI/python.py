import random
import plotly.figure_factory as ff

count=[]
dice_result=[]
for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)
    count.append(i)

fig=ff.create_distplot([dice_result],["result"])

fig.show()