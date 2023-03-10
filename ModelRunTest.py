# Only for Testing
import csv

import matplotlib.pyplot as plt
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


xvalues = []
yvalues = []
radiusForMateSelection = output[0]["parameters"]["radiusForMateSelection"]

for index in range(len(output)):
    xvalues.append(output[index]["parameters"]["numberOfPairings"])
    yvalues.append(output[index]["meanDonationRateOfLastSteps"])

ax = plt.axes()
plt.plot(xvalues, yvalues, color = 'g',
         linestyle = 'dashed', marker = 'o',
         label = "R = "+  str(radiusForMateSelection) + " ")
plt.xlabel('Pairings')
plt.ylabel('Mean Donation Rate')

ax.set_xticks(xvalues)
ax.set_yticks(yvalues)
plt.title('Sensitivity Analysis', fontsize = 20)
plt.legend()
plt.show()

openfile.close()
