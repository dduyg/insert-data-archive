# Explaining `TaskTypeClassifier.py`

This script retrieves tasks from Google Calendar and identifies whether each task is categorized
as hedonic or eudaimonic based on predefined keywords in the task names. It uses the Google Calendar
API to retrieve events that occurred within the last two months. The categorization is performed using regular expressions to identify hedonic and eudaimonic patterns in the task names.

### Usage:
- Make sure you have the required libraries installed: google-api-python-client, google-auth-httplib2, google-auth-oauthlib, dateutil
- Obtain client_secret.json from Google Developers Console and save it in the same directory as this script.
- Run the script and authenticate with your Google account to access your Google Calendar data.

> The script is designed to be flexible and can be customized further based on your specific needs.
