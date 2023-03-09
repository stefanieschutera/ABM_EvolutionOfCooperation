

class StatsPerGen:

    def __init__(self) -> None:
        self.sumOfDonationsMadeInGen = 0
        self.sumOfDonationAttemptedInGen = 0

    def printStats(self):
        print("Number of donations made in this generation = ", self.sumOfDonationsMadeInGen)
        print("Number of donations attempted in this generation = ", self.sumOfDonationAttemptedInGen)
        print("Donation Rate for this generation = ", (self.sumOfDonationsMadeInGen / self.sumOfDonationAttemptedInGen) * 100, "%")

