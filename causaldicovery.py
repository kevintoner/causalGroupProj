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
from pytrad.search.ConstraintBased.PC import pc
from pytrad.utils.cit import kci
from networkx.readwrite import json_graph, gpickle
from datetime import datetime


print(f'Started at: {datetime.now()}')
data = pd.read_csv('bank_churn_clean.csv')
#data = data[:5000]

data_np = data.values
print(data_np.shape)

X,Y = data.loc[:,data.columns!='Exited'], data.loc[:,data.columns=='Exited']

G  = pc(
      data  = data_np,
      alpha = 0.05,
      indep_test =  kci,
      stable=True,
      uc_rule=0,
      uc_priority= -1
    )


print(f"Finished at: {datetime.now()} ")


print(G)
DG = G.to_nx_graph()


dg_dump = json_graph.node_link_data(DG)

with open('bankdata-pc-kci-all.txt','w') as of:
    json.dump(dg_dump,of)

nx.write_gpickle(DG,'bankdata-pc-kci-all.gpickle')

