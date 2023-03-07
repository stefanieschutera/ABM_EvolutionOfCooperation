import random

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

    def __init__(self, populationSize = 100, cost = 1.0, benefit = 0.05, numberOfPairings = 3, mutationRate = 0.1, toleranceMinimum = 0, cheaterType = None, random_seed = None) -> None:
        self.populationSize = populationSize
        self.cost = cost
        self.benefit = benefit
        
        self.numberOfPairings = numberOfPairings
        self.mutationRate = mutationRate
        self.toleranceMinimum = toleranceMinimum
        self.cheaterType = cheaterType

        self.agents = self.initialize_agents()


        self.random_seed = random_seed

        if self.random_seed is not None:
            random.seed(self.random_seed)
            #npr.seed(self.random_seed) #just in case we also use numpy random 

    
    def initialize_agents(self):

        agents = set()

        for id in range(1, self.populationSize +1):
            agents.add(Agent(ID=id))

        return agents
        
    def pairing(self):
        #Pairing Phase, Agents donate
        pass

    def mating(self):
        #Mating Phase, Agents Compare Fitness
        pass

    def mutating(self):
        #Mutation Phase, Agents Reproduce
        pass

    def run(self):
        #Running the model
        pass

    

    
