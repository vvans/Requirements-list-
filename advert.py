class Advert:
  def __init__(self, advertTitle, actualAddvertCost):
    self.advertTitle = advertTitle
    self.actualAddvertCost = actualAddvertCost

  def getCost(self):
    return self.actualAddvertCost