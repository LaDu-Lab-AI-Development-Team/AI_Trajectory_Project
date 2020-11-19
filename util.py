#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 02:09:20 2020
@author: mselvaraj
"""
import random

class Node():
    def __init__(self, state, dataPath,classification):
        self.state = state
        self.classification = classification
        self.dataPath = dataPath
class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = random.choice(self.frontier)
            self.frontier.remove(node)
            return node

class MouseInfoNode():
    def __init__(self, time, x, y, inPlatform, nw, ne, sw, se, perimeter):
        self.time = time
        self.x = x
        self.y = y
        self.inPlatform = inPlatform
        self.nw = nw
        self.ne = ne
        self.sw = sw
        self.se = se
        self.perimeter = perimeter