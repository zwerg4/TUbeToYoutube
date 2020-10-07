import os
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo


print("""\033[32m d888888P dP     dP dP                d8888b. dP    dP                     dP            dP                
   88    88     88 88                    `88 Y8.  .8P                     88            88                
   88    88     88 88d888b. .d8888b. .aaadP'  Y8aa8P  .d8888b. dP    dP d8888P dP    dP 88d888b. .d8888b. 
   88    88     88 88'  `88 88ooood8 88'        88    88'  `88 88    88   88   88    88 88'  `88 88ooood8 
   88    Y8.   .8P 88.  .88 88.  ... 88.        88    88.  .88 88.  .88   88   88.  .88 88.  .88 88.  ... 
   dP    `Y88888P' 88Y8888' `88888P' Y88888P    dP    `88888P' `88888P'   dP   `88888P' 88Y8888' `88888P' 
oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
by zwerg4\n\n\n\033[m""")

print('Follow this steps:\n  1.) Go on TUbe select the video you want \n  2.) Go in Inspect mode of your browser\n  '
      '3.) Go to "Network" \n  4.) Start the video and select the GET request with name like: '
      '"chunklist_xxxxx_xxxx.m3u8"\n  5.) Go to the Header of the select request and copy the link ending by m3u8\n\n')

m3u8_link = input('Paste the link here:')
if not m3u8_link.endswith('.m3u8'):
      print("link needs to end with .m3u8")
      exit(-1)

video_name = input('Video name:')

video_name_mp4 = video_name.replace(" ","_") + ".mp4"

download_cmd = "downloadm3u8 -o " + video_name_mp4 + " " + m3u8_link

os.system(download_cmd)

channel = Channel()
channel.login("client_secret.json", "credentials.storage")

video = LocalVideo(file_path=video_name_mp4)

# setting snippet
video.set_title(video_name)
video.set_description("uploaded by TUbeToYoutube")
video.set_tags(["education", "TUbe", "TUbeToYoutube"])
video.set_category("education")
video.set_default_language("en-US")

# setting status
video.set_embeddable(True)
#video.set_license("creativeCommon")
video.set_privacy_status("unlisted")
video.set_public_stats_viewable(True)

video = channel.upload_video(video)

print("\nVideo successfully uploaded!! It can take some time for youtube to preocess the video.\n\n")
print("\033[32m https://youtube.com/" + str(video.id) +" \n\033[m")

#CLIENT_SECRET_FILE = 'client_secret.json'
#API_NAME = 'TubeDownloader'
#API_VERSION = 'v3'
#SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

#service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#request_body = {
#    'snippet': {
#        'categoryId': 27,
#        'title': 'TUbeDownloader Testing',
#        'description': 'TUbeDownloader Description',
#        'tags': ['TUbe', 'Education', 'Uni']
#    },
#    'status': {
#        'privacyStatus': 'private',
#        'selfDeclaredMadeForKids': False,
#    },
#    'notifySubscribers': False
#}

#mediaFile = MediaFileUpload('test2.mp4')

#response_upload = service.videos().insert(
#    part='snippet,status',
#    body=request_body,
#    media_body=mediaFile
#).execute()
