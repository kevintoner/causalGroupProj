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
from datetime import datetime 



print(f"Started at {datetime.now()}")
data = pd.read_csv('bank_churn_clean.csv')

f = open('bankdata-ges-5000-p5.txt','r')
graph_data = json.load(f)


graph = nx.node_link_graph(graph_data,directed=True)

labels = dict(enumerate(data.columns))
graph = nx.relabel_nodes(graph,labels)
nx.draw_networkx(graph)
matplotlib.rcParams['figure.figsize'] = (800,800)
plt.show()

nx.drawing.nx_agraph.write_dot(graph,path='bank-ges-3000-p5.dot')

exit()

digraph = """ digraph {
    CreditScore -> IsActiveMember   [weight=-1];
    Geography -> Age    [weight=-1];
    Geography -> Balance    [weight=1];
    Geography -> Exited [weight=-1];
    Gender -> Exited    [weight=-1];
    Age -> IsActiveMember   [weight=1];
    Age -> Exited   [weight=1];
    Tenure -> HasCrCard [weight=-1];
    Balance -> NumOfProducts    [weight=-1];
    Balance -> Exited   [weight=-1];
    NumOfProducts -> Exited [weight=-1];
    HasCrCard -> IsActiveMember [weight=1];
    IsActiveMember -> Exited    [weight=1];
    EstimatedSalary;
    }"""


model = CausalModel(
        data = data,
        graph=digraph.replace('\n',' '),
        treatment='Gender',
        outcome='Exited'
    )
model.view_model()
display(Image(filename='causal_model.png'))

identified_estimand = model.identify_effect(proceed_when_unidentifiable=True)
print(identified_estimand)


estimate = model.estimate_effect(identified_estimand, method_name="iv.instrumental_variable", target_units="ate")
print(estimate)

refute_results = model.refute_estimate(identified_estimand, estimate, method_name="random_common_cause")
print(refute_results)

print(f"Finished at {datetime.now()}")
