from googleapiclient.discovery import build
from google.oauth2 import service_account


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

SAMPLE_SPREADSHEET_ID = '1LElB_r-7rsM6KfVVTjPxt4V008SZoHq6Kzpfqu08Rmo' # id таблиуы



service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="""sales!A1:C3""").execute()

values = result.get('values', [])

aoa = [["1/1/2020", 4000], ["3/1/2020", 200], ["1/2/2020", 12]]

request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="sales!A9",
                                valueInputOption="USER_ENTERED", body={"values": aoa}).execute()



print(request) # сколько записей len
