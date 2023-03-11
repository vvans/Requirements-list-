from client import Client

class Staff:
  def __init__(self, staffName, staffNo, staffTelephone, staffEmailAddress, staffStartDate):
    self.staffName = staffName
    self.staffNo = staffNo
    self.staffTelephone = staffTelephone
    self.staffEmailAddress = staffEmailAddress
    self.staffStartDate = staffStartDate

  def assignStaffContact(self, client:Client):
    client.contactName = self.staffName
    client.contactTelephone = self.staffTelephone
    client.contactEmail = self.staffEmailAddress

  def getStaffDetails(self):
    return f'[Staff] Name : {self.staffName}, No : {self.staffNo}, Telephone : {self.staffTelephone}, EmailAddress : {self.staffEmailAddress}, StartDate : {self.staffStartDate}'
  