class StatsPerGen:

    def __init__(self) -> None:
        self.sumOfDonationsMade = 0
        self.sumOfAllDonationInteractions = 0
        self.donationRateInGen = 0

    def printStats(self):
        print("Number of donations made in this generation = ",
              self.sumOfDonationsMade)
        print("Number of donations attempted in this generation = ",
              self.sumOfAllDonationInteractions)
        print("Donation rate for this generation = ",
              self.donationRateInGen * 100, "%")

    def add_agents_donation_values(self, agent):
        self.sumOfDonationsMade += agent.donationsMade
        self.sumOfAllDonationInteractions += agent.noOfDonationInteractions

    def calculate_donation_rate(self):
        self.donationRateInGen = self.sumOfDonationsMade / \
            self.sumOfAllDonationInteractions
