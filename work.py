from __future__ import print_function
import pickle
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError




class GoogleSheet:
    SPREADSHEET_ID = '1LElB_r-7rsM6KfVVTjPxt4V008SZoHq6Kzpfqu08Rmo'  # id таблиуы
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets'] # можно все что угодно делать
    service = None

    def __init__(self):
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                print('flow')
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES
                )
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('sheets', 'v4', credentials=creds)

    def updateRangeValue(self, range, values): # Обновление ячеек (запись) range = какая ячейка value = значение
        data = [{
            'range': range,
            'values':  values
        }]

        body = {
            'valueInputOption': 'USER_ENTERED',
            'data': data
        }

        result = self.service.spreadsheets().values().batchUpdate(spreadsheetId=self.SPREADSHEET_ID, body=body).execute()
        print('{0} calls updated'.format(result.get('totalUpdatedCells')))

def main():
    gs = GoogleSheet()
    test_range = 'Test List!G2:H4'
    test_values = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    gs.updateRangeValue(test_range, test_values)

if __name__ == '__main__':
    main()

