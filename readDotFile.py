#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 14:31:35 2021

@author: ahmed.mahrooqi
"""

import json
import numpy as np
import pytrad
import dowhy
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from dowhy import CausalModel
from IPython.display import Image, display
import statsmodels
# from datetime import datetime 
import os
from os.path import exists


# Get the digraph string from dot file
def readDigraph(fileName):

    # Convert dot file to text file
    if not exists(fileName+".txt"):
        old_name = fileName+".dot"
        new_name = fileName+".txt"
        os.rename(old_name, new_name)

    # Read contents of the file
    with open('bank-ges-5000-p5.txt') as f:
        contents = f.read()

    # Convert text file back to dot file
    # os.rename(new_name, old_name)

    # Fix the string contents from the graph
    contents = contents.replace('strict digraph "" {', '""" digraph {')
    digraph = contents.replace('}', '}"""')
    return digraph

print(readDigraph("bank-ges-5000-p5"))
