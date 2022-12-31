from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import argparse
import subprocess
import json
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date

# bot settings
TOKEN="YOUR_TOKEN" 
ID="YOUR_ID"
URL="https://api.telegram.org/bot$TOKEN/sendMessage"


# command parser
parser = argparse.ArgumentParser(description='google rive upload and download')
parser.add_argument("-l", "--links", help="Prints the supplied argument.", nargs='*')
args = parser.parse_args()


# gdrive settings
scope = ["https://www.googleapis.com/auth/drive"]
gauth = GoogleAuth()
gauth.auth_method = 'service'
gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
drive = GoogleDrive(gauth)

# bot message
MESSAGE = "Screenshot 👉\nPixeldrain 👇👇👇👇\n480p👉 480_r\n720p👉 720_r\n1080p👉 1080_r\n-----------------------------\n\nOffical Site 👇👇👇👇\n480p👉 480p_r\n720p👉 720p_r\n1080p👉 1080p_r\n\nPASSWORD 👉 https://t.me/c/1227529573/1207"
all_link = {}
# loop for handling update
for arg in args.links:
    link = arg.split('=')[1]
    file = drive.CreateFile({'id': link})
    name = file['title']
    name = name.lower().replace('1337xhd.', '').replace('mlsbd.shop', ' ').replace('shop',' ').replace('-', ' ').replace('  ', '').strip()
    file.GetContentFile(name, acknowledge_abuse=True)
    drive = subprocess.check_output(['rclone', 'copy', name, 'one:Public/Dec/' + date.today().strftime('%d')])
    pixel_drain = subprocess.check_output(['curl', '-g', 'https://pixeldrain.com/api/file/', '-u:8e312a99-f6af-4e4d-bd43-04721db3fb61', '--upload-file', name])
    print(pixel_drain)
    all_link[name[:6]] = MESSAGE
    # if '480p' in name:
    #     all_links[name[:6]][480] = data
    # elif '720p' in name:
    #     all_links[name[:6]][720] = data
    # elif '1080p' in name:
    #     all_links[name[:6]][1080] = data
    try:
        pixel_link = json.loads(pixel_drain.decode().replace('\n', ''))['id']
        print(pixel_link)
        if '480p' in name:
            all_link[name[:6]] = all_link[name[:6]].replace('480_r', f'https://pixeldrain.com/u/{pixel_link}')
            all_link[name[:6]].replace('480p_r', '')
        if '720p' in name:
            all_link[name[:6]] = all_link[name[:6]].replace('720_r', f'https://pixeldrain.com/u/{pixel_link}')
            all_link[name[:6]].replace('720p_r', '')
        if '1080p' in name:
            all_link[name[:6]] = all_link[name[:6]].replace('1080_r', f'https://pixeldrain.com/u/{pixel_link}')
            all_link[name[:6]].replace('1080p_r', '')
    except Exception as e:
        print(e)

for name, link in all_link.items():
    print(name)
    print(link)
#     curl -s -X POST $URL -d chat_id=$ID -d text=name
#     curl -s -X POST $URL -d chat_id=$ID -d text=link
