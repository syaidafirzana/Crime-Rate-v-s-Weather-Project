#Line Graph - Change in Temperature

import pandas as pd
from matplotlib import pyplot as plt
x = ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
tempt_2018 = [17.02, 15.30, 10.80, 9.68, 7.09, 7.13, 7.92, 8.92, 11.09, 13.00, 15.71]
tempt_2019 = [17.27, 16.38, 11.45, 10.32, 5.94, 7.61, 6.9, 9.31, 10.54, 15.49, 15.93]
plt.plot(x,tempt_2018)
plt.plot(x,tempt_2019)
plt.title("Christchurch Average Temperature per month")
plt.xlabel("Months")
plt.ylabel("Average Temperature (Celsius)")
plt.legend(['2018', '2019'])
plt.show