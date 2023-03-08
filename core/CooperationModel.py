import random
import numpy as np

from core.Agent import Agent


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

    def __init__(self, populationSize=100, cost=1.0, benefit=0.05, numberOfPairings=3, mutationRate=0.1, toleranceMinimum=0, cheaterType=None, networkType='complete', randomSeed=None) -> None:
        self.populationSize = populationSize
        self.cost = cost
        self.benefit = benefit
        self.numberOfPairings = numberOfPairings
        self.mutationRate = mutationRate
        self.toleranceMinimum = toleranceMinimum
        self.cheaterType = cheaterType
        self.agents = self.initialize_agents()
        self.networkType = networkType
        self.randomSeed = randomSeed
        if self.randomSeed is not None:
            random.seed(self.randomSeed)
            np.random.seed(self.randomSeed)

    def initialize_agents(self):
        agents = set()
        for i in range(1, self.populationSize + 1):
            agents.add(Agent(ID=i))
        return agents

    def find_mate(self, currentAgent):
        allExceptCurrentAgent = list()
        for agent in self.agents:
            if agent.ID != currentAgent.ID:
                allExceptCurrentAgent.append(agent)

        mate = random.choice(allExceptCurrentAgent)
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
            agent.mutate(self.mutationRate)

    def giving_birth_to_next_gen(self):
        for agent in self.agents:
            agent.give_birth()

    def step(self):
        self.pairing()
        self.mating()
        self.mutating()
        self.giving_birth_to_next_gen()
