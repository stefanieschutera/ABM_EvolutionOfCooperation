from SensitivityAnalysis import *
from datetime import datetime
from ModelConfigs import configVaryingPairingsTest
import sys
import os

sys.setrecursionlimit(100000)

start = datetime.now()

if not os.path.exists('output'):
    os.mkdir('output')
file = 'output/' + start.strftime("%Y%m%d_%H%M%S") + '_output.json'

run_sensitivity_analysis(numberOfSteps=configVaryingPairingsTest["numberOfSteps"],
                         populationSize=configVaryingPairingsTest["populationSize"],
                         toleranceMinimum=configVaryingPairingsTest["toleranceMinimum"],
                         costAndBenefitRange=configVaryingPairingsTest["costAndBenefitRange"],
                         numberOfPairingsRange=configVaryingPairingsTest["numberOfPairingsRange"],
                         mutationRateRange=configVaryingPairingsTest["mutationRateRange"],
                         cheaterMutationRateRange=configVaryingPairingsTest["cheaterMutationRateRange"],
                         networkTypeRange=configVaryingPairingsTest["networkTypeRange"],
                         radiusForMateSelectionRange=configVaryingPairingsTest[
                             "radiusForMateSelectionRange"],
                         pathToFile=file)

print("Passed time for ",
      configVaryingPairingsTest["numberOfSteps"],  "time steps =", datetime.now() - start)
