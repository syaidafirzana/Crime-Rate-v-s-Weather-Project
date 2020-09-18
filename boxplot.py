import matplotlib.pyplot as plt
 
Burglary_2018 = [490, 503, 496, 574, 539, 527, 525, 593, 640, 718, 676]
Burglary_2019 = [661, 525, 490, 542, 488, 573, 547, 532, 600, 550, 561]
 
box_plot_data=[Burglary_2018,Burglary_2019]
plt.boxplot(box_plot_data,patch_artist=True,labels=['2018', '2019'])
plt.show()