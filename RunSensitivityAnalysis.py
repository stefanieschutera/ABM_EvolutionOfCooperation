from SensitivityAnalysis import *
from datetime import datetime
import sys

sys.setrecursionlimit(100000)

start = datetime.now()

file = 'output/test.json'

numberOfSteps = 100

run_sensitivity_analysis(numberOfSteps = numberOfSteps, 
                             populationSize=400, 
                             toleranceMinimum=0, 
                             costAndBenefitRange = [(0.05, 1)], 
                             numberOfPairingsRange=[1,2,3,4,5], 
                             mutationRateRange=[0.1], 
                             cheaterMutationRateRange=[0], 
                             networkTypeRange=['complete'], 
                             radiusForMateSelectionRange = [1], 
                             pathToFile = file)



passed_time = datetime.now() - start

print("Passed Time for ", numberOfSteps, "time steps =", passed_time)
