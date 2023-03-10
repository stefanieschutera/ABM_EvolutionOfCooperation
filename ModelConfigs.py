configVaryingPairingsBC10 = {"numberOfSteps": 30000,
                             "populationSize": 400,
                             "toleranceMinimum": -10**(-6),  # stays the same
                             "costAndBenefitRange": [(0.1, 1)],
                             "numberOfPairingsRange": range(1, 31),
                             "mutationRateRange": [0.01],
                             # see netlogo code
                             "cheaterMutationRateRange": [0],
                             "networkTypeRange": ['cycle'],
                             "radiusForMateSelectionRange": [1],
                             }
