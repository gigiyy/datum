import os
import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Replace the values below with your own
SPREADSHEET_ID = 'your-spreadsheet-id'
RANGE_NAME = 'Sheet1!A1:B2'

# Obtain credentials from environment variables
creds = Credentials.from_authorized_user_info(
    info=os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
)

# Obtain credentials from environment variables
# creds, _ = google.auth.default(scopes=['https://www.googleapis.com/auth/spreadsheets.readonly'])


# If the credentials are expired, refresh them
if creds and creds.expired and creds.refresh_token:
    creds.refresh(Request())

# Build the Google Sheets API client
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API to read data from the sheet
result = service.spreadsheets().values().get(
    spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME
).execute()

# Print the data from the sheet
values = result.get('values', [])
if not values:
    print('No data found.')
else:
    for row in values:
        print('\t'.join(row))
