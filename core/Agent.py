import copy
import random
import networkx as nx
import numpy as np


class Agent:

    # TODO Update comment
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
        self.neighborsWithinRadius = None
        tolerance, tag, cheaterFlag = random.random(), random.random(), False
        self._initialize_agent(tolerance, tag, cheaterFlag)

    def _initialize_agent(self, tolerance, tag, cheaterFlag):
        self.tolerance = tolerance
        self.tag = tag
        self.cheaterFlag = cheaterFlag
        self.fitness = 0
        self.childTag = None
        self.childTolerance = None
        self.childCheaterFlag = None
        self.donationsMade = 0
        self.noOfDonationInteractions = 0

    def initialize_agent_neighbors(self, radiusForMateSelection, network):
        neighborsWithinRadius = nx.single_source_shortest_path(
            network, self, cutoff=radiusForMateSelection)
        neighborsWithinRadius.pop(self)
        self.neighborsWithinRadius = list(neighborsWithinRadius)

    def donate(self, recipient, cost, benefit):
        if self.cheaterFlag == False:
            tagDifference = abs(self.tag - recipient.tag)
            if tagDifference <= self.tolerance:
                self.fitness -= cost
                recipient.fitness += benefit
                self.donationsMade += 1
        self.noOfDonationInteractions += 1

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

    def mutate(self, mutationRate):
        if random.random() < mutationRate:
            centreOfDistribution = 0
            standardDeviationOfDistribution = 0.01
            noise = np.random.normal(
                centreOfDistribution, standardDeviationOfDistribution)
            self.childTolerance += noise
            if self.childTolerance < 0:
                self.childTolerance = 0
        if random.random() < mutationRate:
            self.childTag = random.random()
            # If cheaterFlag is True then this means that this agent WILL NEVER DONATE
            # If cheaterMutationRate is 0 then this means that cheaterFlag is False
        # remove cheater
        # if random.random() <= mutationRate:
            # self.childCheaterFlag = True
        # else:
            # self.childCheaterFlag = False

    def give_birth(self):
        tolerance, tag, cheaterFlag = copy.deepcopy(
            self.childTolerance), copy.deepcopy(self.childTag), copy.deepcopy(self.childCheaterFlag)
        self._initialize_agent(tolerance, tag, cheaterFlag)
