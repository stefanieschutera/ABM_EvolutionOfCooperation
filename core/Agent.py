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
        self.cheaterFlag = False
        self.fitness = 0
        self.childTag = None
        self.childTolerance = None
        self.childCheaterFlag = None

    def donate(self, recipient, cost, benefit):
        tagDifference = abs(self.tag - recipient.tag)
        if tagDifference <= self.tolerance:
            self.fitness -= cost
            recipient.fitness += benefit
            self.donations_made += 1
        self.donations_attempted += 1


    def compare_fitness(self, mate):
        if self.fitness > mate.fitness:
            parent = self
        elif self.fitness < mate.fitness:
            parent = mate
        else:
            parent = random.choice([self, mate])
        self._set_child_attributes(parent)

    def _set_child_attributes(self, parent):
        self.childTag = copy.deepcopy(parent.tag)
        self.childTolerance = copy.deepcopy(parent.tolerance)
        self.childCheaterFlag = copy.deepcopy(parent.cheaterFlag)

    def mutate(self, mutationRate, noise):
        if random.random() < mutationRate:
            self.childTolerance += noise
            if self.childTolerance < 0:
                self.childTolerance = 0
            self.childTag = random.random()

    def give_birth(self):
        self.tolerance = copy.deepcopy(self.childTolerance)
        self.tag = copy.deepcopy(self.childTag)
        self.cheaterFlag = copy.deepcopy(self.childCheaterFlag)
        self.childTag, self.childTolerance, self.childCheaterFlag, self.fitness = None, None, None, 0
