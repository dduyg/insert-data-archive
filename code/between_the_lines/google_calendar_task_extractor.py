import os
import datetime
import re
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from dateutil.relativedelta import relativedelta

# Define the scopes required for accessing Google Calendar API
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

# Path to the credentials file (created after the first authentication)
CREDS_FILE = 'credentials.json'

def authenticate_google_calendar():
    creds = None
    if os.path.exists(CREDS_FILE):
        creds = Credentials.from_authorized_user_file(CREDS_FILE, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for future use
        with open(CREDS_FILE, 'w') as f:
            f.write(creds.to_json())
    
    return creds

def categorize_task(task_name):
    hedonic_keywords = re.compile(r'\b(hedon(ic|ism|istic))\b', re.IGNORECASE)
    eudaimonic_keywords = re.compile(r'\b(eudaimon(ic|ism|istic))\b', re.IGNORECASE)

    if re.search(hedonic_keywords, task_name):
        return 'hedonic'
    elif re.search(eudaimonic_keywords, task_name):
        return 'eudaimonic'
    else:
        return 'uncategorized'

def get_calendar_tasks():
    creds = authenticate_google_calendar()
    service = build('calendar', 'v3', credentials=creds)
    
    # Define the calendar ID or leave it as 'primary' for the default calendar
    calendar_id = 'primary'
    
    # Calculate the start date for the last two months accurately
    today = datetime.datetime.today()
    two_months_ago = today - relativedelta(months=2)
    
    # Format the dates as strings in RFC3339 format for API query
    start_date = two_months_ago.strftime('%Y-%m-%dT%H:%M:%S') + 'Z'
    end_date = today.strftime('%Y-%m-%dT%H:%M:%S') + 'Z'
    
    # Define the query parameters to filter tasks for the last two months
    events_result = service.events().list(
        calendarId=calendar_id,
        singleEvents=True,
        orderBy='startTime',
        timeMin=start_date,
        timeMax=end_date
    ).execute()
    
    tasks = []
    for event in events_result.get('items', []):
        # Extract task name, start date, and type of task (hedonic/eudaimonic)
        task_name = event['summary']
        event_start = event['start'].get('dateTime', event['start'].get('date'))
        type_of_task = categorize_task(task_name)
        
        # Convert date string to Python datetime object
        if 'T' in event_start:
            start_date = datetime.datetime.fromisoformat(event_start.replace('Z', '+00:00'))
        else:
            start_date = datetime.datetime.strptime(event_start, '%Y-%m-%d')
        
        tasks.append({'task': task_name, 'date': start_date, 'type_of_task': type_of_task})
    
    return tasks

def main():
    tasks = get_calendar_tasks()
    
    # You can further process or save the tasks as a dataset here
    for task in tasks:
        print(task)

if __name__ == '__main__':
    main()
