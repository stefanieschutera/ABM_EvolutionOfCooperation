# Only for Testing
import csv

import matplotlib.pyplot as plt
import pandas as pd
import csv
import json


from core.CooperationModel import CooperationModel

testModel = CooperationModel(populationSize=10, cheaterMutationRate=0.9)

for agent in testModel.agents:
    print(agent.ID, agent.fitness, agent.tag, agent.tolerance)

for index in range(3):
    statsPerGen = testModel.step()
    statsPerGen.printStats()

testModel.plot_network()

for agent in testModel.agents:
    print(agent.ID, agent.fitness, agent.tag, agent.tolerance)


# Opening JSON file
with open('output/20230309_163856_output.json', 'r') as openfile:

    # Reading from json file
    output = json.load(openfile)

print(output[0]["parameters"]["numberOfSteps"])
