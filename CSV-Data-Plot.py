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

myfile = open("C:\\MAIN-FOLDER-TO-BACKUP\\programming\\My-Python\\ABM_EvolutionOfCooperation\\TestData.csv", 'r')
csv_reader = csv.reader(myfile, delimiter = ',')
xvalues = []
yvalues = []

for line in csv_reader:
    print(line)
    xvalues.append(line[0])
    yvalues.append(line[1])

ax = plt.axes()
plt.plot(xvalues, yvalues, color = 'g',
         linestyle = 'dashed', marker = 'o',
         label = "R = 1")
plt.xlabel('Pairings')
plt.ylabel('Mean Donation Rate')

ax.set_xticks(xvalues)
ax.set_yticks(yvalues)
plt.title('Sensitivity Analysis', fontsize = 20)
plt.legend()
plt.show()

myfile.close()

# JSON file processing

jsonfile = open("C:\\MAIN-FOLDER-TO-BACKUP\\programming\\My-Python\\ABM_EvolutionOfCooperation\\TestJSON.json")
jsondata = json.load(jsonfile)

for i in jsondata:
    print(i)

jsonfile.close()



