import copy
import random
import numpy as np


class StatsPerGen:

    def __init__(self) -> None:
        self.sumOfDonationsMadeInGen = 0
        self.sumOfDonationAttemptedInGen = 0