from core.CooperationModel import CooperationModel

testModel = CooperationModel(populationSize=10)

for agent in testModel.agents:
    print(agent.ID, agent.fitness, agent.tag, agent.tolerance)

testModel.step()

for agent in testModel.agents:
    print(agent.ID, agent.fitness, agent.tag, agent.tolerance)


