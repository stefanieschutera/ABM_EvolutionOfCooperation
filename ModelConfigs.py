configVaryingPairingsBC10 = {"numberOfSteps": 30000,
                             "populationSize": 400,
                             "toleranceMinimum": -10**(-6),
                             "costAndBenefitRange": [(0.1, 1)],
                             "numberOfPairingsRange": range(1, 31),
                             "mutationRateRange": [0.01],
                             "cheaterMutationRateRange": [0],
                             "networkTypeRange": ['cycle'],
                             "radiusForMateSelectionRange": [1],
                             }

configVaryingPairingsTest1 = {"numberOfSteps": 2000,
                              "populationSize": 100,
                              "toleranceMinimum": -10**(-6),
                              "costAndBenefitRange": [(1, 10)],
                              "numberOfPairingsRange": [1],
                              "mutationRateRange": [0.01],
                              "cheaterMutationRateRange": [0],
                              "networkTypeRange": ['cycle'],
                              "radiusForMateSelectionRange": [1],
                              }

# 20230310_134954_output.json
# 20230310_142326_output.json
configVaryingPairingsTest = {"numberOfSteps": 5000,
                             "populationSize": 250,
                             "toleranceMinimum": -10**(-6),
                             "costAndBenefitRange": [(0.1, 1)],
                             "numberOfPairingsRange": [9],
                             "mutationRateRange": [0.01],
                             "cheaterMutationRateRange": [0],
                             "networkTypeRange": ['cycle'],
                             "radiusForMateSelectionRange": [1],
                             }

# cycle vs complete 20230310_135957_output.json
configVaryingPairingsTest3 = {"numberOfSteps": 5000,
                              "populationSize": 200,
                              "toleranceMinimum": -10**(-6),
                              "costAndBenefitRange": [(0.1, 1)],
                              "numberOfPairingsRange": [9],
                              "mutationRateRange": [0.01],
                              "cheaterMutationRateRange": [0],
                              "networkTypeRange": ['cycle', 'complete'],
                              "radiusForMateSelectionRange": [100],
                              }

# cycle vs complete 20230310_140106_output.json
configVaryingPairingsTest4 = {"numberOfSteps": 10000,
                              "populationSize": 200,
                              "toleranceMinimum": -10**(-6),
                              "costAndBenefitRange": [(0.1, 1)],
                              "numberOfPairingsRange": [9],
                              "mutationRateRange": [0.01],
                              "cheaterMutationRateRange": [0],
                              "networkTypeRange": ['cycle', 'complete'],
                              "radiusForMateSelectionRange": [100],
                              }


# 20230310_140359_output.json
configVaryingPairingsTest5 = {"numberOfSteps": 5000,
                              "populationSize": 200,
                              "toleranceMinimum": -10**(-6),
                              "costAndBenefitRange": [(0.1, 1)],
                              "numberOfPairingsRange": [9],
                              "mutationRateRange": [0.1],
                              "cheaterMutationRateRange": [0],
                              "networkTypeRange": ['cycle', 'complete'],
                              "radiusForMateSelectionRange": [100],
                              }


configVaryingPairingsTest6 = {"numberOfSteps": 5000,
                              "populationSize": 200,
                              "toleranceMinimum": -10**(-6),
                              "costAndBenefitRange": [(0.1, 1)],
                              "numberOfPairingsRange": [9],
                              "mutationRateRange": [0.1],
                              "cheaterMutationRateRange": [0],
                              "networkTypeRange": ['cycle', 'complete'],
                              "radiusForMateSelectionRange": [1],
                              }
