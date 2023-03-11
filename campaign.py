from advert import Advert


class Campaign:

  def __init__(self, title, campaignStartDate, campaignFinishDate,
               actualCampaignCost):
    self.title = title
    self.campaignStartDate = campaignStartDate
    self.campaignFinishDate = campaignFinishDate
    self.actualCampaignCost = actualCampaignCost
    self.advertList = [
      Advert('(임의로)newspaper', 100),
      Advert('(임의로)magazine', 300),
      Advert('(임의로)internet', 900)
    ]

  def getCampaignDetails(self):
    return f'[Campaign] Title : {self.title}, StartDate : {self.campaignStartDate}, FinishDate : {self.campaignFinishDate}, actualCampaignCost : {self.actualCampaignCost}'

  def totalOfAdvertList(self):
    return sum([advert.getCost() for advert in self.advertList])

  def checkCampaignBudget(self):
    return self.actualCampaignCost + self.totalOfAdvertList()
