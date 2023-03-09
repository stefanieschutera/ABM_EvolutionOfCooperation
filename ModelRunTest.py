from core.CooperationModel import CooperationModel


testModel = CooperationModel(populationSize=10)

for agent in testModel.agents:
    print(agent.ID, agent.fitness, agent.tag, agent.tolerance)

for index in range(3):
    testModel.step()
    statsPerGen = testModel.get_donation_statistic_for_gen()
    statsPerGen.printStats()
testModel.plot_network()

for agent in testModel.agents:
    print(agent.ID, agent.fitness, agent.tag, agent.tolerance)
