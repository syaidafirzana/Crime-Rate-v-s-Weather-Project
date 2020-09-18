import numpy as np
import matplotlib.pyplot as plt

Number_of_bars = 12
ind = np.arange(Number_of_bars)  # the x locations for the groups
width = 0.3      # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

year2018 = [0, 490, 503, 496, 574, 539, 527, 525, 593, 640, 718, 676]
rects1 = ax.bar(ind, year2018, width, color='r')
year2019 = [728, 661, 525, 490, 542, 488, 573, 547, 532, 600, 550, 561]
rects2 = ax.bar(ind+width, year2019, width, color='g')

ax.set_ylabel('Monthly Burglary Cases')
ax.set_xlabel('Month')

ax.set_xticks(ind+width)
ax.set_xticklabels( ('Jan', 'Feb', 'Mar', 'Apr','May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec') )
ax.legend( (rects1[0], rects2[0]), ('2018', '2019') )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1*h, '%d'%int(h),
                ha='center', va='bottom')

        
autolabel(rects1)
autolabel(rects2)