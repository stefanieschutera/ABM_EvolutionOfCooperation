from core.CooperationModel import CooperationModel
import json
import copy


def mean_donation_rate_of_one_run(donationRate):
    numberOfSteps = len(donationRate)
    ratioOfRelevantLastSteps = 0.033
    relevantSteps = int(numberOfSteps * ratioOfRelevantLastSteps)
    meanDonationRateOfLastSteps = sum(
        donationRate[-relevantSteps:]) / relevantSteps
    return meanDonationRateOfLastSteps


def run_model(ourModel, numberOfSteps=100, saveDonationRateList=False, pathToFile=None):
    donationRate = list()
    for i in range(numberOfSteps):
        statsPerGen = ourModel.step()
        donationRate.append(statsPerGen.donationRateInGen)
    meanDonationRateOfLastSteps = mean_donation_rate_of_one_run(
        donationRate=donationRate)

    if saveDonationRateList == True:
        file = open(pathToFile, 'w+')
        file.writelines(donationRate)
        file.close()

    return meanDonationRateOfLastSteps


def run_sensitivity_analysis(numberOfSteps=100,
                             populationSize=400,
                             toleranceMinimum=0,
                             costAndBenefitRange=[(0.05, 1)],
                             numberOfPairingsRange=[3],
                             mutationRateRange=[0.1],
                             cheaterMutationRateRange=[0],
                             networkTypeRange=['complete'],
                             radiusForMateSelectionRange=[1],
                             pathToFile=None,
                             numberOfSimulationsPerConfig=1):

    model = CooperationModel(populationSize=populationSize,
                             toleranceMinimum=toleranceMinimum, networkType='cycle')
    output = list()

    for costAndBenefit in costAndBenefitRange:
        cost = costAndBenefit[0]
        benefit = costAndBenefit[1]
        for numberOfPairings in numberOfPairingsRange:
            for mutationRate in mutationRateRange:
                for cheaterMutationRate in cheaterMutationRateRange:
                    for networkType in networkTypeRange:
                        for radiusForMateSelection in radiusForMateSelectionRange:
                            for n in range(numberOfSimulationsPerConfig):
                                modelCopy = copy.deepcopy(model)
                                modelCopy.cost = cost
                                modelCopy.benefit = benefit
                                modelCopy.numberOfPairings = numberOfPairings
                                modelCopy.mutationRate = mutationRate
                                modelCopy.cheaterMutationRate = cheaterMutationRate
                                modelCopy.networkType = networkType
                                modelCopy.radiusForMateSelection = radiusForMateSelection

                                meanDonationRateOfLastSteps = run_model(
                                    modelCopy, numberOfSteps=numberOfSteps)
                                parameters = {'numberOfSteps': numberOfSteps,
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

                                output.append(
                                    {'meanDonationRateOfLastSteps': meanDonationRateOfLastSteps, 'parameters': parameters})

    outputJson = json.dumps(output, indent=4)
    with open(pathToFile, "w") as outfile:
        outfile.write(outputJson)
