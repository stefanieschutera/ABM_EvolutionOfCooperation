# Only for Testing

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
