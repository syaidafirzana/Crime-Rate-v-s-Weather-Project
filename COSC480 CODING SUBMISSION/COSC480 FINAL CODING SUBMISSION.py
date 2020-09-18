#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# PYTHON PROJECT COSC480
# Nur Syaida Firzana Mohamad Isham
# 66474666


# In[1]:


import os
os.path.abspath(os.getcwd())


# In[40]:


# Import pandas package
# Import Dataset
import pandas as pd
data = pd.read_csv("Report Burgular Edited.csv")
data.head()


# In[ ]:


### Calculate total number of crimes for each month in 2018
### Extract from Dataset
### Sum total reported cases per day in each month
### Year 2018


# In[4]:


# Calculate total number of crimes for each month in 2018

def cal(month_num, lines):
    """ Calculates the total number of crimes in each month 2018"""
    total = 0
    for i in range(1, len(lines)):
        list1 = lines[i].split(",")
        if list1[3].endswith("/{}/2018".format(month_num)) == True:
            total = total + 1
    return total

def crime(filename):
    """Crimes per month in 2018"""
    file = open(filename)
    lines = file.readlines()
    print("Crimes per month in 2018")
    for i in range(1, 13):
        number = cal(i, lines)
        print("Number of crimes in month {}: {}".format(i, number))
        
crime("Report Burgular Edited.csv")


# In[41]:


# Use pandas to present data in a neat table.
# prints total burglary cases in 2018
import pandas as pd

data = {'Year 2018':['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
         'Monthly Burglary cases':[0, 490, 503, 496, 574, 539, 527, 525, 593, 640, 718, 676]}
df = pd.DataFrame(data)
print(df)

print("\n", "Total Burglary crime cases in 2018 is", sum([0, 490, 503, 496, 574, 539, 527, 525, 593, 640, 718, 676]), "cases.")


# In[ ]:


### Calculate total number of crimes for each month in 2018
### Extract from Dataset
### Sum total reported cases per day in each month
### Year 2019


# In[42]:


### Totals the total cases reported for each day to total for each month.



def cal(month_num, lines):
    """Calculates total number of cases for each month"""
    total = 0
    for i in range(1, len(lines)):
        list1 = lines[i].split(",")
        if list1[3].endswith("/{}/2019".format(month_num)) == True:
            total = total + 1
    return total

def crime(filename):
    """Crimes per month in 2019"""
    file = open(filename)
    lines = file.readlines()
    print("Crimes per month in 2019")
    for i in range(1, 13):
        number = cal(i, lines)
        print("Number of crimes in month {}: {}".format(i, number))
        
crime("Report Burgular Edited.csv")


# In[6]:


# Calculate total number of crimes for each month in 2019

def cal(month_num, lines):
    """Calculate total number of crimes for each month in 2019 """
    total = 0
    for i in range(1, len(lines)):
        list1 = lines[i].split(",")
        if list1[3].endswith("/{}/2019".format(month_num)) == True:
            total = total + 1
    return total

def crime(filename):
    """Crimes per month in 2019"""
    file = open(filename)
    lines = file.readlines()
    print("Crimes per month in 2019")
    for i in range(1, 13):
        number = cal(i, lines)
        print("Number of crimes in month {}: {}".format(i, number))
        
crime("Report Burgular Edited.csv")


# In[43]:


# Use pandas to present data in a neat table.
# prints total burglary cases in 2019

import pandas as pd

data = {'Year 2019':[ 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
         'Monthly Burglary cases':[ 661, 525, 490, 542, 488, 573, 547, 532, 600, 550, 561]}
df = pd.DataFrame(data)
print(df)

print("\n", "Total Burglary crime cases in 2019 is", sum([ 661, 525, 490, 542, 488, 573, 547, 532, 600, 550, 561]), "cases.")


# In[ ]:


# AREA UNITS


# In[44]:


#count

def area(filename):
    """returns a dictionary mapping from object names to occurrence counts """
    file = open(filename)
    lines = file.readlines()
    file.close()
    counts = {}
    for word in lines:
        word = word.rstrip()
        if word != "":
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
    return counts

area("Area_unit.txt")


# In[150]:


# Python program to generate WordCloud 

get_ipython().run_line_magic('matplotlib', 'inline')
from wordcloud import WordCloud, STOPWORDS 
  
comment_words = ' '
stopwords = set(STOPWORDS)

file = open('Area_unit.txt', 'r+')
textdata = file.read().replace('\n', '')


cloud = WordCloud(background_color="white").generate(textdata)
plt.axis('off')
plt.imshow(cloud)
plt.show()

#halfway haven't completed still learning how to get it


# In[45]:


# MONTH TO MONTH COMPARISON
# DOUBLE BAR CHART


# In[141]:


# Generate double bar chart

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


# In[ ]:


# CONTINUE OF ANALYSIS INVOLVING TEMPERATURE


# In[ ]:


# TEMPERATURE 2018


# In[14]:


# Import pandas package
# Import temperature dataset 2018


import pandas as pd
data_temp = pd.read_csv("Temperature 2018.csv")
data_temp.head()


# In[ ]:


### Table Overall Analysis in 2018 (Temperature, Crime cases)


# In[15]:


import pandas as pd

data = {'Year 2018':['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
         'Average Temperature (Celsius)':[18.91, 17.02, 15.30, 10.80, 9.68, 7.09, 7.13, 7.92, 8.92, 11.09, 13.00, 15.71],
        'Burglary Cases':[0, 490, 503, 496, 574, 539, 527, 525, 593, 640, 718, 676]
}
df = pd.DataFrame(data)
print(df)


# In[ ]:


# TEMPERATURE 2019


# In[46]:


# Import pandas package
# Import temperature dataset 2019
import pandas as pd
data_temp = pd.read_csv("Temperature 2019.csv")
data_temp.head()


# In[47]:


### Table Overall Analysis in 2018 (Temperature, Crime cases)


# In[48]:


import pandas as pd

data = {'Year 2019':['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
         'Average Temperature (Celsius)':[18.42, 17.27, 16.38, 11.45, 10.32, 5.94, 7.61, 6.9, 9.31, 10.54, 15.49, 15.93],
        'Burglary Cases':[728, 661, 525, 490, 542, 488, 573, 547, 532, 600, 550, 561]
}



df = pd.DataFrame(data)
print(df)


# In[ ]:


# ANALYSIS USING LINE GRAPH


# In[153]:


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


# In[151]:


# Line Graph - Change Number of Burglary Cases

x = ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
Burglary_2018 = [490, 503, 496, 574, 539, 527, 525, 593, 640, 718, 676]
Burglary_2019 = [661, 525, 490, 542, 488, 573, 547, 532, 600, 550, 561]
plt.plot(x,Burglary_2018)
plt.plot(x,Burglary_2019)
plt.title("Christchurch Burglary Cases per month")
plt.xlabel("Months")
plt.ylabel("Burglary Cases")
plt.legend(['2018', '2019'])
plt.show


# In[ ]:


# STATISTICAL SUMMARY


# In[133]:


import pandas as pd
import numpy as np

print("\n", "Statistical Summary for Burglary Cases 2018", "\n")

#Create a Dictionary of series
d = {'Year':pd.Series([2018]),
   'Month':pd.Series([1,2,3,4,5,6,7,8,9,10,11]),
   'Burglary Cases':pd.Series([ 490, 503, 496, 574, 539, 527, 525, 593, 640, 718, 676]),
    'Mean Temperature':pd.Series([ 17.02, 15.30, 10.80, 9.68, 7.09, 7.13, 7.92, 8.92, 11.09, 13.00, 15.71])
}

#Create a DataFrame
df = pd.DataFrame(d)
print (df.describe(include='all'))

print("\n","\n", "Statistical Summary for Burglary Cases 2019", "\n")


#Create a Dictionary of series
d = {'Year':pd.Series([2019]),
   'Month':pd.Series([1,2,3,4,5,6,7,8,9,10,11]),
   'Burglary Cases':pd.Series([ 661, 525, 490, 542, 488, 573, 547, 532, 600, 550, 561]),
    'Mean Temperature':pd.Series([ 17.27, 16.38, 11.45, 10.32, 5.94, 7.61, 6.9, 9.31, 10.54, 15.49, 15.93])
}

#Create a DataFrame
df = pd.DataFrame(d)
print (df.describe(include='all'))


# In[ ]:


# SCATTERPLOT


# In[29]:


import matplotlib.pyplot as plt
import numpy as np

Burglary_cases = [ 490, 503, 496, 574, 539, 527, 525, 593, 640, 718, 676,  661, 525, 490, 542, 488, 573, 547, 532, 600, 550, 561]
temperature = [ 17.02, 15.30, 10.80, 9.68, 7.09, 7.13, 7.92, 8.92, 11.09, 13.00, 15.71,  17.27, 16.38, 11.45, 10.32, 5.94, 7.61, 6.9, 9.31, 10.54, 15.49, 15.93]

fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.scatter(temperature, Burglary_cases, color='black')

ax.set_xlabel('ChristchurchMain$MeanTemperature')
ax.set_ylabel('ChristchurchMain$BurglaryCases')
ax.set_title('scatter plot')

plt.plot()
plt.show()


# In[ ]:


# STATISTICAL ANALYSIS OF THE SCATTER PLOT


# In[49]:


# SLOPE
# INTERCEPT
# R VALUE
# P VALUE
# STANDARD ERROR

Burglary_cases_2018 = [ 490, 503, 496, 574, 539, 527, 525, 593, 640, 718, 676, 661, 525, 490, 542, 488, 573, 547, 532, 600, 550, 561]
temperature2018 = [ 17.02, 15.30, 10.80, 9.68, 7.09, 7.13, 7.92, 8.92, 11.09, 13.00, 15.71, 17.27, 16.38, 11.45, 10.32, 5.94, 7.61, 6.9, 9.31, 10.54, 15.49, 15.93]
from scipy.stats import linregress
linregress(Burglary_cases_2018,temperature2018)


# In[6]:


#Boxplot Burglary Cases
import matplotlib.pyplot as plt
 
Burglary_2018 = [490, 503, 496, 574, 539, 527, 525, 593, 640, 718, 676]
Burglary_2019 = [661, 525, 490, 542, 488, 573, 547, 532, 600, 550, 561]
 
box_plot_data=[Burglary_2018,Burglary_2019]
plt.title('Boxplot of Burglary Cases in 2018 and 2019 in Christchurch')
plt.ylabel('Number of Burglary Cases')
plt.xlabel('Years')
plt.boxplot(box_plot_data,patch_artist=True,labels=['2018', '2019'])
plt.show()


# In[11]:


#Boxplot Temperature
import matplotlib.pyplot as plt
 
tempt_2018 = [17.02, 15.30, 10.80, 9.68, 7.09, 7.13, 7.92, 8.92, 11.09, 13.00, 15.71]
tempt_2019 = [17.27, 16.38, 11.45, 10.32, 5.94, 7.61, 6.9, 9.31, 10.54, 15.49, 15.93]
 
box_plot_data=[tempt_2018 ,tempt_2019]
plt.title('Boxplot of Temperature in Christchurch 2018 and 2019')
plt.ylabel('Temperature (Celsius)')
plt.xlabel('Years')
plt.boxplot(box_plot_data,patch_artist=False,labels=['2018', '2019'])
plt.show()


# In[ ]:


# GRAPHICAL USER INTERFACE (GUI)

### Allows users to select the type of analysis they are interested 

from tkinter import *
from tkinter.ttk import *  
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Gui:
    def __init__(self, window):
        """Construct and runs GUI"""
        self.label = Label(window, text='CRIME V/S WEATHER ANALYSIS IN CHRISTCHURCH')
        self.label.grid(row=0, column=2 ) 
        self.button1 = Button(window, text="Statistical Summary", command=self.stat)
        self.button1.grid(row=1, column=1, padx=20, pady=10)
        self.button2 = Button(window, text="Bar Chart", command=self.make_bar_chart)
        self.button2.grid(row=1, column=2, padx=20, pady=10)
        self.button3 = Button(window, text="Temperature Line Graph", command=self.linetemp)
        self.button3.grid(row=1,column=3, padx=20, pady=10)
        self.button4 = Button(window, text="Area Units", command=self.area)
        self.button4.grid(row=3,column=2, padx=20, pady=10) 
        self.button5 = Button(window, text="Scatterplot", command=self.scatterplot)
        self.button5.grid(row=2,column=2, padx=20, pady=10)   
        self.button6 = Button(window, text="Burglary Cases Line graph", command=self.line_cases)
        self.button6.grid(row=2,column=3, padx=20, pady=10)         
        self.button7 = Button(window, text="Box Plot Report Cases", command=self.boxplotcase)
        self.button7.grid(row=2,column=1, padx=20, pady=10)          
        self.button8 = Button(window, text="Box Plot Temperature", command=self.boxplot_temp)
        self.button8.grid(row=3,column=1, padx=20, pady=10)           
    def stat(self):
        """Prints output of statistical summary """
        filename = open('statistical_summary.txt')
        self.lines = filename.read().strip()
        print(self.lines)
    
    def area(self):
        """returns a dictionary mapping from object names to occurrence counts """
        file = open("Area_unit.txt")
        lines = file.readlines()
        file.close()
        counts = {}
        for word in lines:
            word = word.rstrip()
            if word != "":
                if word not in counts:
                    counts[word] = 1
                else:
                    counts[word] += 1
        print(counts)       

    def make_bar_chart(self):
        """Displays an bar chart """
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
        for rect in rects:
            h = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 1*h, '%d'%int(h),
                    ha='center', va='bottom')
    
    def linetemp(self):
        """Displays a line graph for analysing the temperature """
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

    
    def scatterplot(self):
        """Displays scatterplot for analysis """
        Burglary_cases = [ 490, 503, 496, 574, 539, 527, 525, 593, 640, 718, 676,  661, 525, 490, 542, 488, 573, 547, 532, 600, 550, 561]
        temperature = [ 17.02, 15.30, 10.80, 9.68, 7.09, 7.13, 7.92, 8.92, 11.09, 13.00, 15.71,  17.27, 16.38, 11.45, 10.32, 5.94, 7.61, 6.9, 9.31, 10.54, 15.49, 15.93]
        fig=plt.figure()
        ax=fig.add_axes([0,0,1,1])
        ax.scatter(temperature, Burglary_cases, color='black')
        ax.set_xlabel('ChristchurchMain$MeanTemperature')
        ax.set_ylabel('ChristchurchMain$BurglaryCases')
        ax.set_title('scatter plot')
        plt.plot()
        plt.show()        
       
    def line_cases(self):
        """Displays line graph for analysing burglary cases """
        x = ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        Burglary_2018 = [490, 503, 496, 574, 539, 527, 525, 593, 640, 718, 676]
        Burglary_2019 = [661, 525, 490, 542, 488, 573, 547, 532, 600, 550, 561]
        plt.plot(x,Burglary_2018)
        plt.plot(x,Burglary_2019)
        plt.title("Christchurch Burglary Cases per month")
        plt.xlabel("Months")
        plt.ylabel("Burglary Cases")
        plt.legend(['2018', '2019'])
        plt.show()   
        
    def boxplotcase(self):
        """Displays boxplot for burglary cases """
        Burglary_2018 = [490, 503, 496, 574, 539, 527, 525, 593, 640, 718, 676]
        Burglary_2019 = [661, 525, 490, 542, 488, 573, 547, 532, 600, 550, 561]
         
        box_plot_data=[Burglary_2018,Burglary_2019]
        plt.title('Boxplot of Burglary Cases in 2018 and 2019 in Christchurch')
        plt.ylabel('Number of Burglary Cases')
        plt.xlabel('Years')
        plt.boxplot(box_plot_data,patch_artist=True,labels=['2018', '2019'])
        plt.show()        
        
    def boxplot_temp(self):
        """Displays boxplot for temperature """
        tempt_2018 = [17.02, 15.30, 10.80, 9.68, 7.09, 7.13, 7.92, 8.92, 11.09, 13.00, 15.71]
        tempt_2019 = [17.27, 16.38, 11.45, 10.32, 5.94, 7.61, 6.9, 9.31, 10.54, 15.49, 15.93]
        box_plot_data=[tempt_2018 ,tempt_2019]
        plt.title('Boxplot of Temperature in Christchurch 2018 and 2019')
        plt.ylabel('Temperature (Celsius)')
        plt.xlabel('Years')
        plt.boxplot(box_plot_data,patch_artist=False,labels=['2018', '2019'])
        plt.show()
        
def main():
    """Main function tests the Gui class """
    window = Tk() 
    gui = Gui(window)
    quit_button = Button(window, text="Quit", command=window.destroy)
    quit_button.grid(row=3, column=3, pady=20, padx=10)
    window.mainloop()
main()





