import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from core.Agent import Agent
from core.StatsPerGen import StatsPerGen


class CooperationModel:
    '''
    Class holding the environment of the ABM

    Open Questions:
    - How to model space and location of the agents?

    Attributes
    ---------------

    ...
    ...


    Methods
    ----------------
    __init__()
        Creates ABM with the parameters ...
        Arguments to provide are
    ...
    ...

    '''

    def __init__(self, populationSize=100, cost=1.0, benefit=0.05, numberOfPairings=3, mutationRate=0.1, toleranceMinimum=0, cheaterMutationRate=0, networkType='complete', radiusForMateSelection=1, randomSeed=None) -> None:
        self.populationSize = populationSize
        self.cost = cost
        self.benefit = benefit
        self.numberOfPairings = numberOfPairings
        self.mutationRate = mutationRate
        centreOfDistribution = 0
        standardDeviationOfDistribution = 0.01
        self.noise = np.random.normal(
            centreOfDistribution, standardDeviationOfDistribution)
        self.toleranceMinimum = toleranceMinimum  # TODO use it
        self.cheaterMutationRate = cheaterMutationRate
        self.networkType = networkType
        self.agents = self.initialize_agents()
        self.network = self.initialize_network()
        self.radiusForMateSelection = radiusForMateSelection
        self.initialize_agent_neighbors()
        self.randomSeed = randomSeed
        if self.randomSeed is not None:
            random.seed(self.randomSeed)
            np.random.seed(self.randomSeed)

    def initialize_agents(self):
        agents = set()
        for i in range(1, self.populationSize + 1):
            agents.add(Agent(ID=i))
        return agents

    def initialize_agent_neighbors(self):
        for agent in self.agents:
            agent.initialize_agent_neighbors(
                radiusForMateSelection=self.radiusForMateSelection, network=self.network,)

    def initialize_network(self):
        if self.networkType == 'complete':
            network = nx.complete_graph(self.agents)
        elif self.networkType == 'cycle':
            network = nx.cycle_graph(self.agents)
        else:
            raise Exception("Network Type unknown")
        return network

    def plot_network(self):
        fig, ax = plt.subplots()
        nx.draw_networkx(self.network, with_labels=False, ax=ax)
        plt.show()

    def find_mate(self, currentAgent):
        mate = random.choice(currentAgent.neighborsWithinRadius)
        return mate

    def pairing(self):
        for agent in self.agents:
            for p in range(self.numberOfPairings):
                mate = self.find_mate(agent)
                agent.donate(recipient=mate, cost=self.cost,
                             benefit=self.benefit)

    def mating(self):
        for agent in self.agents:
            mate = self.find_mate(agent)
            agent.compare_fitness(mate)

    def mutating(self):
        for agent in self.agents:
            agent.mutate(self.mutationRate, self.noise,
                         self.cheaterMutationRate)

    def giving_birth_to_next_gen(self):
        for agent in self.agents:
            agent.give_birth()

    def step(self):
        self.pairing()
        self.mating()
        self.mutating()
        statsPerGen = self.get_donation_statistic_for_gen()
        self.giving_birth_to_next_gen()
        return statsPerGen

    def get_donation_statistic_for_gen(self):
        statsPerGen = StatsPerGen()
        for agent in self.agents:
            statsPerGen.sumOfDonationsMadeInGen += agent.donationsMade
            statsPerGen.sumOfDonationAttemptedInGen += agent.donationsAttempted
        return statsPerGen
