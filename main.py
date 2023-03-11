from fastapi import FastAPI, Request, Form
import uvicorn
from fastapi.templating import Jinja2Templates
from staff import Staff
from client import Client
from campaign import Campaign

app = FastAPI()
templates = Jinja2Templates(directory='templates/')

staffList = [
  Staff('(임의로)김부장', '10', '010-0000-0000', 'abcd1234@khu.ac.kr', '2010-10-09')
]
clientList = [Client('(임의로)경희대', '경기 용인시 기흥구 ~~', '031-201-0000')]

# getClient -> getClientCampaign에서 어떤 경로를 통해서 들어갔는지 확인하기 위해서 필요하다
# state는 모델 설계를 바탕으로 몇 가지로 제한한다.
# client, checkCampaignBudget, addNewCampaign, completeCampaign
state = 'client'

#Add a new campaign을 실시할 때 clientList의 순서를 저장하기 위해서
numberSelectionClientList = 0


@app.get('/')
def get_main_form(request: Request):
  return templates.TemplateResponse('main.html', context={'request': request})


@app.get('/staff')
def get_staff_form(request: Request):
  return templates.TemplateResponse('staff.html', context={'request': request})


@app.get('/staff_join')
def get_staff_join(request: Request):
  return templates.TemplateResponse('staff_join.html',
                                    context={'request': request})


@app.post('/staff_join2')
def get_staff_join2(request: Request,
                    staffName=Form(...),
                    staffNo=Form(...),
                    staffTelephone=Form(...),
                    staffEmailAddress=Form(...),
                    staffStartDate=Form(...)):
  staff = Staff(staffName, staffNo, staffTelephone, staffEmailAddress,
                staffStartDate)
  staffList.append(staff)
  for i in range(len(staffList)):
    print(staffList[i].getStaffDetails())
  return templates.TemplateResponse('staff_join2.html',
                                    context={
                                      'request': request,
                                      'staff_info': staff.getStaffDetails()
                                    })


@app.get('/assign_staff_contact')
def get_assign_staff_contact(request: Request):
  return templates.TemplateResponse(
    'assign_staff_contact.html',
    context={
      'request':
      request,
      'staffNameList': [staff.staffName for staff in staffList],
      'staffNoList': [staff.staffNo for staff in staffList],
      'staffTelephoneList': [staff.staffTelephone for staff in staffList],
      'staffEmailAddressList':
      [staff.staffEmailAddress for staff in staffList],
      'staffStartDateList': [staff.staffStartDate for staff in staffList],
      'companyNameList': [client.companyName for client in clientList],
      'companyAddressList': [client.companyAddress for client in clientList],
      'companyTelephoneAddressList':
      [client.companyTelephone for client in clientList],
      'contactNameList': [client.contactName for client in clientList],
      'contactEmailList': [client.contactEmail for client in clientList],
      'contactTelephoneList':
      [client.contactTelephone for client in clientList],
      'new_state':
      state
    })


@app.post('/assign_staff_contact_result')
def post_assign_staff_contact_result(
  request: Request,
  assignStaffContactSelectionStaff=Form(...),
  assignStaffContactSelectionClient=Form(...)):
  # to assign staff contact
  staffList[int(assignStaffContactSelectionStaff)].assignStaffContact(
    clientList[int(assignStaffContactSelectionClient)])

  return templates.TemplateResponse(
    'assign_staff_contact_result.html',
    context={
      'request':
      request,
      'companyNameList': [client.companyName for client in clientList],
      'companyAddressList': [client.companyAddress for client in clientList],
      'companyTelephoneAddressList':
      [client.companyTelephone for client in clientList],
      'contactNameList': [client.contactName for client in clientList],
      'contactEmailList': [client.contactEmail for client in clientList],
      'contactTelephoneList':
      [client.contactTelephone for client in clientList]
    })


@app.get('/get_staff')
def get_staff_detail(request: Request):
  return templates.TemplateResponse(
    'get_staff.html',
    context={
      'request': request,
      'staffNameList': [staff.staffName for staff in staffList],
      'staffNoList': [staff.staffNo for staff in staffList],
      'staffTelephoneList': [staff.staffTelephone for staff in staffList],
      'staffEmailAddressList':
      [staff.staffEmailAddress for staff in staffList],
      'staffStartDateList': [staff.staffStartDate for staff in staffList]
    })


@app.get('/client')
def get_client_form(request: Request):
  return templates.TemplateResponse('client.html',
                                    context={'request': request})


@app.get('/client_join')
def get_client_join(request: Request):
  return templates.TemplateResponse('client_join.html',
                                    context={'request': request})


@app.post('/client_join2')
def get_client_join2(request: Request,
                     companyName=Form(...),
                     companyAddress=Form(...),
                     companyTelephone=Form(...)):
  client = Client(companyName, companyAddress, companyTelephone)
  clientList.append(client)
  for i in range(len(clientList)):
    print(clientList[i].getClient())
  return templates.TemplateResponse('client_join2.html',
                                    context={
                                      'request': request,
                                      'client_info': client.getClient()
                                    })


@app.get('/get_client')
def get_client_detail2(request: Request):
  global state
  state = 'client'
  return templates.TemplateResponse(
    'get_client.html',
    context={
      'request':
      request,
      'companyNameList': [client.companyName for client in clientList],
      'companyAddressList': [client.companyAddress for client in clientList],
      'companyTelephoneAddressList':
      [client.companyTelephone for client in clientList],
      'contactNameList': [client.contactName for client in clientList],
      'contactEmailList': [client.contactEmail for client in clientList],
      'contactTelephoneList':
      [client.contactTelephone for client in clientList],
      'new_state':
      state
    })


@app.post('/get_client')
def get_client_detail(request: Request, new_state=Form(...)):
  global state
  state = new_state
  return templates.TemplateResponse(
    'get_client.html',
    context={
      'request':
      request,
      'companyNameList': [client.companyName for client in clientList],
      'companyAddressList': [client.companyAddress for client in clientList],
      'companyTelephoneAddressList':
      [client.companyTelephone for client in clientList],
      'new_state':
      state
    })


# 추후에 return 되는 방식 변경할려면 하자
@app.post('/get_client_campaigns')
def get_client_campaign_deailt(request: Request, selectionClient=Form(...)):
  global numberSelectionClientList
  numberSelectionClientList = int(selectionClient)
  clientCampaignsList = clientList[
    numberSelectionClientList].getClientCampaigns()
  return templates.TemplateResponse(
    'get_client_campaigns.html',
    context={
      'request':
      request,
      'state':
      state,
      'titleList':
      [clientCampaigns.title for clientCampaigns in clientCampaignsList],
      'campaignStartDateList': [
        clientCampaigns.campaignStartDate
        for clientCampaigns in clientCampaignsList
      ],
      'campaignFinishDateList': [
        clientCampaigns.campaignFinishDate
        for clientCampaigns in clientCampaignsList
      ],
      'actualCampaignCostList': [
        clientCampaigns.actualCampaignCost
        for clientCampaigns in clientCampaignsList
      ],
      'relatedAdvertCostList': [
        clientCampaigns.totalOfAdvertList()
        for clientCampaigns in clientCampaignsList
      ],
      'checkCampaignBudget': [
        clientCampaigns.checkCampaignBudget()
        for clientCampaigns in clientCampaignsList
      ],
      'totalClientCost':
      sum([
        clientCampaigns.checkCampaignBudget()
        for clientCampaigns in clientCampaignsList
      ])
    })


@app.post('/complete_campaign')
def post_complete_campaign(request: Request, selectionCampaign=Form(...)):
  client = clientList[numberSelectionClientList]
  campaign = client.getClientCampaigns()[int(selectionCampaign)]
  relatedAdvert = ''
  for i in campaign.advertList:
    relatedAdvert += f'{i.advertTitle}, '
  print(
    client.completeCampaign(int(selectionCampaign)) + 'RelatedAdvert : ' +
    relatedAdvert[:-2])
  return templates.TemplateResponse('complete_campaign.html',
                                    context={
                                      'request': request,
                                      'clientName': client.companyName,
                                      'clientAddress': client.companyAddress,
                                      'clientTelephone':
                                      client.companyTelephone,
                                      'campaignTitle': campaign.title,
                                      'campaignStartDate':
                                      campaign.campaignStartDate,
                                      'campaignFinishDate':
                                      campaign.campaignFinishDate,
                                      'campaignCost':
                                      campaign.actualCampaignCost,
                                      'relatedAdvert': relatedAdvert[:-2]
                                    })


@app.get('/campaign_join')
def get_campaign_join(request: Request):
  return templates.TemplateResponse('campaign_join.html',
                                    context={'request': request})


@app.post('/campaign_join2')
def get_campaign_join2(request: Request,
                       title=Form(...),
                       campaignStartDate=Form(...),
                       campaignFinishDate=Form(...),
                       actualCampaignCost=Form(...)):
  campaign = Campaign(title, campaignStartDate, campaignFinishDate,
                      int(actualCampaignCost))
  clientList[numberSelectionClientList].addNewCampaign(campaign)
  print(campaign.getCampaignDetails())
  return templates.TemplateResponse('campaign_join2.html',
                                    context={
                                      'request':
                                      request,
                                      'campaign_info':
                                      campaign.getCampaignDetails()
                                    })


@app.get('/campaign')
def get_campaign_form(request: Request):
  return templates.TemplateResponse('campaign.html',
                                    context={'request': request})


@app.get('/advert')
def get_advert_form(request: Request):
  return templates.TemplateResponse('advert.html',
                                    context={'request': request})


uvicorn.run(app, host="0.0.0.0", port='8000')
