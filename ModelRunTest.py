from core.CooperationModel import CooperationModel

testModel = CooperationModel(populationSize=10)



for agent in testModel.agents:
    print(agent.ID, agent.fitness)

testModel.pairing()

for agent in testModel.agents:
    print(agent.ID, agent.fitness)

