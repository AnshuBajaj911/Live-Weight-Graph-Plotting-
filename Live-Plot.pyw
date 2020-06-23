import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt 
import re

plt.style.use('fivethirtyeight')

fig1 = plt.figure("Live Plot")


ax1 = fig1.add_subplot(1,1,1)

def animate(p):
    plot_data = open('test.txt','r').read()
    
    line_data = plot_data.split('\n')
    x1=[]
    y1=[]

    for line in line_data:
        if len(line)>1:

            x,y = line.split(',')
        
            x1.append(x)
            y1.append(float(y))
          
        ax1.clear()
        ax1.plot(x1,y1)
        plt.xticks(rotation=45)
        plt.subplots_adjust(bottom=0.15)
anime_data = animation.FuncAnimation(fig1,animate,interval=500)
plt.title("WEIGHT-PLOT")
plt.show()            



