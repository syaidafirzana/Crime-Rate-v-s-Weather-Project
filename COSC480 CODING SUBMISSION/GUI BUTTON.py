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
        Burglary_2018 = [490, 503, 496, 574, 539, 527, 525, 593, 640, 718, 676]
        Burglary_2019 = [661, 525, 490, 542, 488, 573, 547, 532, 600, 550, 561]
         
        box_plot_data=[Burglary_2018,Burglary_2019]
        plt.title('Boxplot of Burglary Cases in 2018 and 2019 in Christchurch')
        plt.ylabel('Number of Burglary Cases')
        plt.xlabel('Years')
        plt.boxplot(box_plot_data,patch_artist=True,labels=['2018', '2019'])
        plt.show()        
        
    def boxplot_temp(self):
        tempt_2018 = [17.02, 15.30, 10.80, 9.68, 7.09, 7.13, 7.92, 8.92, 11.09, 13.00, 15.71]
        tempt_2019 = [17.27, 16.38, 11.45, 10.32, 5.94, 7.61, 6.9, 9.31, 10.54, 15.49, 15.93]
        box_plot_data=[tempt_2018 ,tempt_2019]
        plt.title('Boxplot of Temperature in Christchurch 2018 and 2019')
        plt.ylabel('Temperature (Celsius)')
        plt.xlabel('Years')
        plt.boxplot(box_plot_data,patch_artist=False,labels=['2018', '2019'])
        plt.show()
        
def main():
    window = Tk() 
    gui = Gui(window)
    quit_button = Button(window, text="Quit", command=window.destroy)
    quit_button.grid(row=3, column=3, pady=20, padx=10)
    window.mainloop()
main()



