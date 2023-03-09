

class StatsPerGen:

    def __init__(self) -> None:
        self.sumOfDonationsMadeInGen = 0
        self.sumOfDonationAttemptedInGen = 0
        self.donationRateInGen = 0

    def printStats(self):
        print("Number of donations made in this generation = ",
              self.sumOfDonationsMadeInGen)
        print("Number of donations attempted in this generation = ",
              self.sumOfDonationAttemptedInGen)
        print("Donation Rate for this generation = ",
              self.donationRateInGen * 100, "%")

    def add_agents_donation_values(self, agent):
        self.sumOfDonationsMadeInGen += agent.donationsMade
        self.sumOfDonationAttemptedInGen += agent.donationsAttempted

    def calculate_donation_rate(self):
        self.donationRateInGen = self.sumOfDonationsMadeInGen / \
            self.sumOfDonationAttemptedInGen
