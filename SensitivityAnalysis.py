from core.CooperationModel import CooperationModel
import copy


def mean_donation_rate_of_one_run(donationRate):
    numberOfSteps = len(donationRate)
    relevantStepsForCalculation = int(numberOfSteps * 0.033)
    meanDonationRateOfLastSteps = sum(donationRate[-relevantStepsForCalculation:]) / relevantStepsForCalculation
    return meanDonationRateOfLastSteps



def run_model(ourModel, numberOfSteps = 100, saveDonationRateList = False, pathToFile = None):
    donationRate = list()
    for i in range(numberOfSteps):
        ourModel.step()
        genStats = ourModel.get_donation_statistics_for_gen()
        donationRate.append(genStats.sumOfDonationsMadeInGen / genStats.sumOfDonationAttemptedInGen)
    meanDonationRateOfLastSteps = mean_donation_rate_of_one_run(donationRate=donationRate)
    
    if saveDonationRateList == True:
        file = open(pathToFile,'w')
        file.writelines(donationRate)
        file.close()

    return meanDonationRateOfLastSteps #TODO maybe think about other structure here


def run_sensitivity_analysis(numberOfSteps = 100, 
                             populationSize=400, 
                             toleranceMinimum=0, 
                             costAndBenefitRange = [(0.05, 1)], 
                             numberOfPairingsRange=[3], 
                             mutationRateRange=[0.1], 
                             cheaterMutationRateRange=[0], 
                             networkTypeRange=['complete'], 
                             radiusForMateSelectionRange = [1], 
                             pathToFile = None): 
    
    model = CooperationModel(populationSize=populationSize, toleranceMinimum=toleranceMinimum)

    for costAndBenefit in costAndBenefitRange:
        cost = costAndBenefit[0]
        benefit = costAndBenefit[1]
        for numberOfPairings in numberOfPairingsRange:
            for mutationRate in mutationRateRange:
                for cheaterMutationRate in cheaterMutationRateRange:
                    for networkType in networkTypeRange:
                        for radiusForMateSelection in radiusForMateSelectionRange:
                            modelCopy = copy.deepcopy(model)
                            modelCopy.cost = cost
                            modelCopy.benefit = benefit
                            modelCopy.numberOfPairings = numberOfPairings
                            modelCopy.mutationRate = mutationRate
                            modelCopy.cheaterMutationRate = cheaterMutationRate
                            modelCopy.networkType = networkType
                            modelCopy.radiusForMateSelection = radiusForMateSelection

                            meanDonationRateOfLastSteps = run_model(modelCopy, numberOfSteps=numberOfSteps)
                            parameterDict = {'numberOfSteps': numberOfSteps, 
                                             'populationSize': populationSize,
                                             'toleranceMinimum': toleranceMinimum,
                                             'cost': cost,
                                             'benefit': benefit,
                                             'numberOfPairings': numberOfPairings,
                                             'mutationRate': mutationRate,
                                             'cheaterMutationRate': cheaterMutationRate,
                                             'networkType': networkType,
                                             'radiusForMateSelection': radiusForMateSelection
                                             }
                            if pathToFile != None:
                                file = open(pathToFile,'a')
                                file.write((meanDonationRateOfLastSteps, parameterDict))
                                file.write('\n')
                                file.close()
                            
                            


testModel = CooperationModel()
copytestModel = copy.deepcopy(testModel)