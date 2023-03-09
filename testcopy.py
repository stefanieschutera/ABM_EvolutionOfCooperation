from core.CooperationModel import CooperationModel
import copy
import sys

sys.setrecursionlimit(10**6)


a = CooperationModel(populationSize=400)
b = copy.deepcopy(a)
