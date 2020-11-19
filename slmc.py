#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 18:19:52 2020

@author: mselvaraj, amoore, blukas
"""


import os
from util import Node, StackFrontier, QueueFrontier, MouseInfoNode
import time
import shutil
import csv

def standardize(mousePath):
    #function that will adjust the x and y values of the mouse nodes so that they are standardized for the AI
    
    #TO DO: Write this function!!!!
    
    return mousePath

def spatialDirect(mousePath):
    #function that will return true if mousePath satisfies conditions for Spatial Direct Trajectory
    
    #TO DO: Write this function!!!!
    
    return False

def spatialIndirect(mousePath):
    #function that will return true if mousePath satisfies conditions for Spatial Indirect Trajectory
    
    #TO DO: Write this function!!!!
    
    return False

def focalCorrect(mousePath):
    #function that will return true if mousePath satisfies conditions for Focal Correct Trajectory
    
    #TO DO: Write this function!!!!
    
    return False

def scanning(mousePath):
    #function that will return true if mousePath satisfies conditions for Scanning Trajectory
    
    #TO DO: Write this function!!!!
    
    return False
    
def random(mousePath):
    #function that will return true if mousePath satisfies conditions for Random Trajectory
    
    #TO DO: Write this function!!!!
    
    return False

def focalIncorrect(mousePath):
    #function that will return true if mousePath satisfies conditions for Focal Incorrect Trajectory
    
    #TO DO: Write this function!!!!
    
    return False

def chaining(mousePath):
    #function that will return true if mousePath satisfies conditions for Chaining Trajectory
    
    #TO DO: Write this function!!!!
    
    return False

def peripheralLooping(mousePath):
    #function that will return true if mousePath satisfies conditions for peripheral looping Trajectory
    
    #TO DO: Write this function!!!!
    
    return False

def circling(mousePath):
    #function that will return true if mousePath satisfies conditions for circling Trajectory
    
    #TO DO: Write this function!!!!
    
    return False

def main():
    #returns ouput file with picture classifications

    timestr = time.strftime("%m%d%Y-%H%M%S")
    outName = timestr+"_output.csv"
    output = open(outName, "x")
    output.write("plot,strategy \n")
    output.close()
    queue = QueueFrontier()
    fields = ["Time", "Centre position X", "Centre position Y", "In platform", "In nw quad", "In ne quad", "In sw quad", "In se quad", "In perimeter"]
    #print("Checkpoint 1")
    for filename in os.listdir("plots"):
        if not filename.startswith('.'):
            dataPath = "plots/" + filename
            newNode = Node(filename,dataPath, "none")
            queue.add(newNode)
            #print("Checkpoint 2")
    #print("Checkpoint 3")
    while (queue.empty() == False):
        outputCont = open(outName, "a")
        pathNode = queue.remove()
        mousePath = []
        with open(pathNode.dataPath, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file, fieldnames = fields)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count+=1
                    #print("Checkpoint 4")
                    continue
                if line_count == 1:
                    line_count+=1
                    #print("Checkpoint 5")
                    continue
                if line_count == 2:
                    line_count+=1
                    #print("Checkpoint 6")
                    continue
                mousePath.append(MouseInfoNode(row["Time"], row["Centre position X"], row["Centre position Y"], row["In platform"], row["In nw quad"], row["In ne quad"], row["In sw quad"], row["In se quad"], row["In perimeter"]))
                #print("Checkpoint 7")
                line_count+=1
        
        mousePath = standardize(mousePath)
       
        # for node in mousePath:
        #     print(node.to_string())
            
        if (spatialDirect(mousePath)):
            outputCont.write(pathNode.state + "," + "Spatial Direct" + "\n")  
            
        elif (spatialIndirect(mousePath)):
            outputCont.write(pathNode.state + "," + "Spatial Indirect" + "\n")
            
        elif (focalCorrect(mousePath)):
            outputCont.write(pathNode.state + "," + "Focal Correct" + "\n")
        
        elif (scanning(mousePath)):
            outputCont.write(pathNode.state + "," + "Scanning" + "\n")
            
        elif (random(mousePath)):
            outputCont.write(pathNode.state + "," + "Random" + "\n")
            
        elif (focalIncorrect(mousePath)):
            outputCont.write(pathNode.state + "," + "Focal Incorrect" + "\n")
            
        elif (chaining(mousePath)):
            outputCont.write(pathNode.state + "," + "Chaining" + "\n")
            
        elif (peripheralLooping(mousePath)):
            outputCont.write(pathNode.state + "," + "Peripheral Looping" + "\n")
            
        elif (circling(mousePath)):
            outputCont.write(pathNode.state + "," + "Circling" + "\n")
        
        else:
            outputCont.write(pathNode.state + "," + "Undefined" + "\n")
            #print("Checkpoint 8")
        
        outputCont.close()
        #print("Checkpoint 9")
        shutil.move(pathNode.dataPath,("finished_" + pathNode.dataPath))
    output.close();
    #print("Checkpoint 10")
    
if __name__ == "__main__":
    main()