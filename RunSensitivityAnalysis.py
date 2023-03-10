from SensitivityAnalysis import *
from datetime import datetime
from ModelConfigs import configVaryingPairingsBC10
import sys
import os

sys.setrecursionlimit(100000)
start = datetime.now()

if not os.path.exists('output'):
    os.mkdir('output')

file = 'output/' + start.strftime("%Y%m%d_%H%M%S") + '_output.json'

run_sensitivity_analysis(numberOfSteps=configVaryingPairingsBC10["numberOfSteps"],
                         populationSize=configVaryingPairingsBC10["populationSize"],
                         toleranceMinimum=configVaryingPairingsBC10["toleranceMinimum"],
                         costAndBenefitRange=configVaryingPairingsBC10["costAndBenefitRange"],
                         numberOfPairingsRange=configVaryingPairingsBC10["numberOfPairingsRange"],
                         mutationRateRange=configVaryingPairingsBC10["mutationRateRange"],
                         cheaterMutationRateRange=configVaryingPairingsBC10["cheaterMutationRateRange"],
                         networkTypeRange=configVaryingPairingsBC10["networkTypeRange"],
                         radiusForMateSelectionRange=configVaryingPairingsBC10[
                             "radiusForMateSelectionRange"],
                         pathToFile=file)


print("Passed time for ",
      configVaryingPairingsBC10["numberOfSteps"],  "time steps =", datetime.now() - start)
