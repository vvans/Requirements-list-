from campaign import Campaign

class Client:

  def __init__(self, companyName, companyAddress, companyTelephone):
    self.companyName = companyName
    self.companyAddress = companyAddress
    self.companyTelephone = companyTelephone
    self.contactName = ""
    self.contactTelephone = ""
    self.contactEmail = ""
    self.campaignList = [
      Campaign('(임의로)Sport', '2017-04-02', '2017-04-15', 1000),
      Campaign('(임의로)T-shirt', '2019-12-06', '2019-12-20', 2000),
      Campaign('(임의로)Shoes', '2020-07-01', '2020-08-31', 8000)
    ]

  def completeCampaign(self,campaignElement):
    return f"""
    [Client Information]
    Name : {self.companyName}
    Address : {self.companyAddress}
    Telephone : {self.companyTelephone}

    [Campaign Information]
    Title : {self.campaignList[campaignElement].title}
    StartDate : {self.campaignList[campaignElement].campaignStartDate}
    FinishDate : {self.campaignList[campaignElement].campaignFinishDate}
    Cost : {self.campaignList[campaignElement].actualCampaignCost}
    """

  def addNewCampaign(self, campaign: Campaign):
    self.campaignList.append(campaign)

  def getClient(self):
    return f'[Client] Name : {self.companyName}, Address : {self.companyAddress}, Telephone : {self.companyTelephone}'

  def getClientCampaigns(self):
    return self.campaignList
