# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import pytrad
import json
import networkx  as nx
from pytrad.search.ScoreBased.GES import ges
from pytrad.utils.cit import gsq
from networkx.readwrite import json_graph, gpickle
from datetime import datetime


print(f'Started at: {datetime.now()}')

data = pd.read_csv('bank_churn_clean.csv')

data_np = data.values

X,Y = data.loc[:,data.columns!='Exited'], data.loc[:,data.columns=='Exited']

#data_np = data_np[:5000]

print(data_np.shape)

Record  = ges(
      data_np,
      'local_score_CV_general',
      maxP=5,
      parameters = {'kfold': 10, 'lambda': 0.01},
    )

print(Record)
G = Record['G']
 
print(G)
print(G.nodes)

print(type(G))

DG = G.graph
print(DG)
DG= nx.from_numpy_array(DG)
dg_dump = json_graph.node_link_data(DG)


with open('bankdata-ges-all-p5.txt','w') as of:
    json.dump(dg_dump,of)

nx.write_gpickle(DG,'bankdata-ges-all-p5.gpickle')
print(f'Finished at: {datetime.now()}')
