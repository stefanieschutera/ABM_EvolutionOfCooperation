from core.CooperationModel import CooperationModel


testModel = CooperationModel(populationSize=10)

for agent in testModel.agents:
    print(agent.ID, agent.fitness, agent.tag, agent.tolerance)

for index in range(3):
    statsPerGen = testModel.step()
    statsPerGen.printStats()
testModel.plot_network()

for agent in testModel.agents:
    print(agent.ID, agent.fitness, agent.tag, agent.tolerance)
