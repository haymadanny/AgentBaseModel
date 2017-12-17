# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 12:56:15 2017

@author: Hayma
"""
import random

#Agent Class with y and x coordinates
# Passes into the Agents class the objects; "self" is the parameter label to assign to the objects
class Agent ():
    
    def __init__(self, environment, agents, y, x):
        self.environment = environment

        self.w = len(environment[0])
        self.h = len(environment)
        if (x==None):
            self.x = random.randint (0, self.w - 1)
            self.y = random.randint (0, self.h - 1)
        else :
            self.x = x
            self.y = y
        self.store = 0
        self.agents = agents
       # print (agents)
 
#Move the Agents randomly.
    def move(self):
   
        if random.random() < 0.5:
            self.x = (self.x +1) % self.w
        else: 
            self.x = (self.x -1) % self.w
        
        if random.random() < 0.5:
            self.y = (self.y +1) % self.h
        else: 
            self.y = (self.y -1) % self.h   
 
#Agent interact with the environment(eat)
    def eat(self): 
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
 
#Agent will search for close neighbours, and share resources with them.
    def share_with_neighbours(self, neighbourhood):
       for agent in self.agents:
        dist = self.distance_between(agent) 
        if dist <= neighbourhood:
            sum = self.store + agent.store
            ave = sum /2
            self.store = ave
            agent.store = ave
            #print("sharing " + str(dist) + " " + str(ave))

# The distance between any arbitrary pair of Agents.
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
              
    def __str__(self):
        return ("x=" + str(self.x) + " y=" + str(self.y))
        
        pass