from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os

# OAuth 2.0 Scopes for Google Drive API
SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]



CREDENTIALS_FILE = "./.secrets/credentials.json"
TOKEN_FILE = "./.secrets/token.json"

def get_access_token():
    creds = None

    # Load existing token if available
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE)

    # If credentials are invalid, re-authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())  # Refresh the token
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)  # Opens a browser for authentication

        # Save the token for future use
        with open(TOKEN_FILE, "w") as token_file:
            token_file.write(creds.to_json())

    return creds.token