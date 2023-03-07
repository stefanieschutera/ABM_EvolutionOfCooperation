import copy
import random

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

        self.child_tag = copy.copy(self.tag)
        self.child_tolerance = copy.copy(self.tolerance)
        self.child_cheater_flag = copy.copy(self.cheater_flag)

        self.donations_made = 0
        self.donations_attempted = 0
        self.donations_made_forever = 0
        self.donations_attempted_forever = 0


    def donate(self, recipient, cost, benefit):
        pass

    def compareFitness(self, mate):
        pass

    def reproduce(self):
        pass

    