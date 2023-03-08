import copy
import random
import numpy as np

class Agent:
    '''
    Class holding the agents of the ABM

    
    Attributes
    ---------------
    Tag: float
        Individual agent tag on [0,1]
    Tolerance: float
        Individual agent tolerance
        Initially on [0,1] then >= LOWER_TOLERANCE
    
    cheater_flag        ;; initially FALSE
    child_tag
    child_tolerance
    child_cheater_flag
    fitness
    donations_made
    donations_attempted
    donations_made_forever
    donations_attempted_forever


    Methods
    ----------------
    __init__()
        Creates agent with initial parameters ...
        Arguments to provide are
    ...
    ...
    
    '''

    def __init__(self, ID) -> None:
        self.ID = ID

        self.tag = random.random() 
        self.tolerance = random.random() 
        self.cheater_flag = False
        
        self.fitness = 0

        self.child_tag = None
        self.child_tolerance = None
        self.child_cheater_flag = None

        self.donations_made = 0
        self.donations_attempted = 0
        self.donations_made_forever = 0
        self.donations_attempted_forever = 0


    def donate(self, recipient, cost, benefit):
        tagDifference = abs(self.tag - recipient.tag)
        if tagDifference <= self.tolerance:
            self.fitness -= cost
            recipient.fitness += benefit
        return

    def compareFitness(self, mate):
        if self.fitness > mate.fitness:
            self.child_tag = copy.deepcopy(self.tag)
            self.child_tolerance = copy.deepcopy(self.tolerance)
            self.child_cheater_flag = copy.deepcopy(self.cheater_flag)
        elif self.fitness < mate.fitness:
            self.child_tag = copy.deepcopy(mate.tag)
            self.child_tolerance = copy.deepcopy(mate.tolerance)
            self.child_cheater_flag = copy.deepcopy(mate.cheater_flag)
        else :
            # randomly select between an agent and mate

            selectedagent = random.choice([self, mate])
            self.child_tag = copy.deepcopy(selectedagent.tag)
            self.child_tolerance = copy.deepcopy(selectedagent.tolerance)
            self.child_cheater_flag = copy.deepcopy(selectedagent.cheater_flag)

    def mutate(self, mutationRate):
        if random.random() < mutationRate:
            noise = np.random.normal(0, 0.01)
            self.child_tolerance += noise
            if self.child_tolerance < 0:
                self.child_tolerance = 0
            self.child_tag = random.random()


    def reproduce(self):
        self.tolerance = copy.deepcopy(self.child_tolerance)
        self.tag = copy.deepcopy(self.child_tag)
        self.cheater_flag = copy.deepcopy(self.child_cheater_flag)
        self.child_tag = None
        self.child_tolerance = None
        self.child_cheater_flag = None
        self.fitness = 0

