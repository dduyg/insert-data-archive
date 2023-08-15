# `TaskTypeClassifier.py`
*<samp>The script is designed to be flexible and can be customized further based on specific needs.</samp>*


This script retrieves tasks from Google Calendar and identifies whether each task is "hedonic" or "eudaimonic" based on predefined keywords found in the task names. It uses the Google Calendar
API to retrieve events that occurred within the last two months. *The categorization is performed using regular expressions to identify hedonic and eudaimonic patterns in the task names.*

> Techniques used include OAuth 2.0 authentication, regular expressions for task categorization,
datetime manipulation, and interaction with the Google Calendar API.

### Before running the script:
- Make sure you have the required libraries installed
- Obtain client_secret.json from Google Developers Console and save it in the same directory as this script. Make sure the filename is exactly `client_secret.json`

Run the script and authenticate with your Google account to access your Google Calendar data.
