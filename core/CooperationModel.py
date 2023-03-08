import random
import copy
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

    def __init__(self, populationSize = 100, cost = 1.0, benefit = 0.05, numberOfPairings = 3, mutationRate = 0.1, toleranceMinimum = 0, cheaterType = None, networkType = 'complete', randomSeed = None) -> None:
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

        for id in range(1, self.populationSize +1):
            agents.add(Agent(ID=id))

        return agents
    
    def find_mate(self, agent):


        setWithoutCurrentAgent = list()
        for a in self.agents:
            if a.ID != agent.ID:
                setWithoutCurrentAgent.append(a)
        
        
        mate = random.choice(setWithoutCurrentAgent)

        return mate
        
        
    def pairing(self):
        #Pairing Phase, Agents donate
        for agent in self.agents:
            for p in range(self.numberOfPairings):
                mate = self.find_mate(agent)
                agent.donate(recipient = mate, cost = self.cost, benefit = self.benefit)
        

    def mating(self):
        #Mating Phase, Agents Compare Fitness
        for agent in self.agents:
            mate = self.find_mate(agent)
            agent.compareFitness(mate)


    def mutating(self):
        #Mutation Phase, Agents Reproduce
        for agent in self.agents:
            agent.mutate(self.mutationRate)



    def generateNewGeneration(self):
        for agent in self.agents:
            agent.reproduce()

    def step(self):
        #Running the model one step
        self.pairing()
        self.mating()
        self.mutating()
        self.generateNewGeneration()


    

    
