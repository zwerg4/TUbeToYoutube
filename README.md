# TUbeToYoutube

    d888888P dP     dP dP                d8888b. dP    dP                     dP            dP                
       88    88     88 88                    `88 Y8.  .8P                     88            88                
       88    88     88 88d888b. .d8888b. .aaadP'  Y8aa8P  .d8888b. dP    dP d8888P dP    dP 88d888b. .d8888b. 
       88    88     88 88'  `88 88ooood8 88'        88    88'  `88 88    88   88   88    88 88'  `88 88ooood8 
       88    Y8.   .8P 88.  .88 88.  ... 88.        88    88.  .88 88.  .88   88   88.  .88 88.  .88 88.  ... 
       dP    `Y88888P' 88Y8888' `88888P' Y88888P    dP    `88888P' `88888P'   dP   `88888P' 88Y8888' `88888P' 
    oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

## Requirements

 **m3u8 downloader**

    $ sudo apt install -y ffmpeg
    $ pip install --upgrade --user https://github.com/youthdev/m3u8downloader/archive/master.zip
 **Google Python API**

    $ pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
    
 **Simple-Youtube-API** 
 

    $ pip install simple-youtube-api
   

   
## Quick start

    $ python3 tubetoyoutube.py

## Steps

 1. Go on TUbe select the video you want
 2. Go in Inspect mode of your browser
 3. Go to "Network" 
 4. Start the video and select the GET request with name like:  '"chunklist_xxxxx_xxxx.m3u8"\n 
 5. Go to the Header of the select request and copy the link ending by m3u8
 6. Paste Link
 7. Enter video name
 8. Allow the script connecting to your Youtube Account (need to do it only once)
 9. Have fun !!
 
 ## TODO List
 - add requirements.txt
 - mutltiple uploads
 - playlist creation
 
 **If you have some things you want to see in this script, contact me or open new issue**

## Useful Youtube Shortcuts
 ,  = go backward by one frame
 
 .  = go forward by one frame
 
SHIFT + , = slow down video by 25%

SHIFT + . = speed up video by 25%