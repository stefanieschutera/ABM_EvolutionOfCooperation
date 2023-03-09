from core.CooperationModel import CooperationModel
from core.StatsPerGen import StatsPerGen

testModel = CooperationModel(populationSize=10, cheaterMutationRate=0.9)

for agent in testModel.agents:
    print(agent.ID, agent.fitness, agent.tag, agent.tolerance)

for index in range(30):
    statsPerGen = testModel.step()
    statsPerGen.printStats()
testModel.plot_network()

for agent in testModel.agents:
    print(agent.ID, agent.fitness, agent.tag, agent.tolerance)
