## Script Information

This script retrieves tasks from a Google Calendar and categorizes them as either hedonic or eudaimonic based on predefined keywords in the task names. It uses the Google Calendar API for authentication and event retrieval. The categorization is performed using regular expressions to identify hedonic and eudaimonic patterns in the task names.

Usage:
- Make sure you have the required libraries installed: google-api-python-client, google-auth-httplib2, google-auth-oauthlib, dateutil
- Obtain client_secret.json from Google Developers Console and save it in the same directory as this script.
- Run the script and authenticate with your Google account to access your Google Calendar data.
- The script will retrieve tasks from the last two months and categorize them as hedonic, eudaimonic, or uncategorized.
