## Explaining `TaskTypeClassifier.py`

This script retrieves tasks from Google Calendar and identifies whether each task is categorized
as hedonic or eudaimonic based on predefined keywords in the task names. It uses the Google Calendar
API to retrieve events that occurred within the last two months. The categorization is performed using regular expressions to identify hedonic and eudaimonic patterns in the task names.

> Techniques used include OAuth 2.0 authentication, regular expressions for task categorization,
datetime manipulation, and interaction with the Google Calendar API.

### Usage:
- Make sure you have the required libraries installed
- Obtain client_secret.json from Google Developers Console and save it in the same directory as this script.
- Replace 'client_secret.json' with your own Google Calendar API credentials file.
- Run the script and authenticate with your Google account to access your Google Calendar data.

> The script is designed to be flexible and can be customized further based on your specific needs.
