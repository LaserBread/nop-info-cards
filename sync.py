import requests
import auth

# Replace with your Google Sheet's file ID
FILE_ID = "1FJ1WksnWDxpaDTBzxLtfk3VdycHqWJ1bmXpUms4NmVA"
ACCESS_TOKEN = auth.get_access_token()

# Google Drive API export URL for .xlsx format
EXPORT_URL = f"https://www.googleapis.com/drive/v3/files/{FILE_ID}/export?mimeType=application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

# Request headers
headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

# Fetch and save the file
response = requests.get(EXPORT_URL, headers=headers)
if response.status_code == 200:
    with open("card-table.xlsx", "wb") as file:
        file.write(response.content)
    print("File downloaded successfully!")
else:
    print("Failed to download:", response.text)