import os
from Google import Create_Service
from googleapiclient.http import MediaFileUpload


print("""d888888PdP     dPdP              888888ba                           dP                      dP                 
   88   88     8888              88    `8b                          88                      88                 
   88   88     8888d888b..d8888b.88     88.d8888b.dP  dP  dP88d888b.88.d8888b..d8888b..d888b88.d8888b.88d888b. 
   88   88     8888'  `8888ooood888     8888'  `8888  88  8888'  `888888'  `8888'  `8888'  `8888ooood888'  `88 
   88   Y8.   .8P88.  .8888.  ...88    .8P88.  .8888.88b.88'88    888888.  .8888.  .8888.  .8888.  ...88       
   dP   `Y88888P'88Y8888'`88888P'8888888P `88888P'8888P Y8P dP    dPdP`88888P'`88888P8`88888P8`88888P'dP       
       
by zwerg4\n\n\n""")

print('Follow this steps:\n  1.) Go on TUbe select the video you want \n  2.) Go in Inspect mode of your browser\n  '
      '3.) Go to "Network" \n  4.) Start the video and select the GET request with name like: '
      '"chunklist_xxxxx_xxxx.m3u8"\n  5.) Go to the Header of the select request and copy the link ending by m3u8\n\n')

m3u8_link = input('Paste the link here:')

download_cmd = "downloadm3u8 -o test2.mp4 " + m3u8_link
os.system(download_cmd)

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'TubeDownloader'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

request_body = {
    'snippet': {
        'categoryId': 27,
        'title': 'TUbeDownloader Testing',
        'description': 'TUbeDownloader Description',
        'tags': ['TUbe', 'Education', 'Uni']
    },
    'status': {
        'privacyStatus': 'private',
        'selfDeclaredMadeForKids': False,
    },
    'notifySubscribers': False
}

mediaFile = MediaFileUpload('test2.mp4')

response_upload = service.videos().insert(
    part='snippet,status',
    body=request_body,
    media_body=mediaFile
).execute()
