from core.CooperationModel import CooperationModel
import pandas as pd
from datetime import datetime



def run_model(ourModel, numberOfSteps = 30000):
    
    d = {'donations': [], 'donationsAttempted': []}
    statsDf = pd.DataFrame(data=d)

    for i in range(numberOfSteps):
        ourModel.step()
        statsPerGen = ourModel.get_donation_statistic_for_gen()
        genDf = pd.DataFrame({'donations': [statsPerGen.sumOfDonationsMadeInGen], 'donationsAttempted': [statsPerGen.sumOfDonationAttemptedInGen]})
        pd.concat([statsDf, genDf])

    # Last generation
    statsPerGen.printStats()

    #TODO Save statsDf

def tun_sensitivity_analysis(): #TODO define parameters
    pass
    


now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)


ourModel = CooperationModel(populationSize=400)

run_model(ourModel)

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
