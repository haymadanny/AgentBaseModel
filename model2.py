# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 21:49:11 2017

@author: Hayma
Building a simple Agent-based model (ABM)
"""
import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.backends.backend_tkagg
import matplotlib.pyplot
import agentframework2
import csv 
import matplotlib.animation 
import tkinter
import requests
import bs4

#Import and read some raster data used as agents' environment.
file = open("in.txt", newline='')
reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)		
environment = []
    
for line in reader:
   rowlist = []
   for item in line:
       rowlist.append(item)
   environment.append(rowlist)
   #print(line)      
file.close() # Close file when finish with reader

#Number of Agents
#Number of iterations
#Number of Neighbours
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

#list for agents
agents = []

#Plot object figure , its size and axes. 
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#Initialised ABM with scraped data from the web (x and y data)
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)

#Make the agents
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework2.Agent(environment, agents, y, x))

carry_on = True

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        print(agents[i])
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
   
#Annimate ABM     
def update(frame_number):
        
        fig.clear() 
        
        global carry_on
        
        for i in range(num_of_agents):
            agents[i].move()
            
        if random.random() < 0.001:
            carry_on = False
            print("stopping condition")
        
        for i in range(num_of_agents):
            matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
            matplotlib.pyplot.imshow(environment)
            #print(agents[i][0],agents[i][1])

def gen_function(b = [0]):
        a = 0
        global carry_on #Not actually needed as we're not assigning, but clearer
        while (a < 10) & (carry_on) :
            yield a			# Returns control and waits next call.
            a = a + 1

# Annimation of agents interacting with the environment
#animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

# ABM Graphical User Interface (GUI)
#Function to run ABM (animation)
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()

#Builds the main window and sets its title
root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#Make menus ("Run model" and "Exit")
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 
menu_bar.add_cascade(label="Exit", command=root.destroy)
tkinter.mainloop()