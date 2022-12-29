from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import argparse
import subprocess
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date


scope = ["https://www.googleapis.com/auth/drive"]


parser = argparse.ArgumentParser(description='google rive upload and download')
parser.add_argument("-l", "--links", help="Prints the supplied argument.", nargs='*')
args = parser.parse_args()


gauth = GoogleAuth()
gauth.auth_method = 'service'
gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
drive = GoogleDrive(gauth)


about = drive.GetAbout()

print('Current user name:{}'.format(about['name']))

for arg in args.links:
    link = arg.split('=')[1]
    file = drive.CreateFile({'id': link})
    name = file['title']
    name = name.lower().replace('1337xhd.', '').replace('mlsbd.shop', ' ').replace('shop',' ').replace('-', ' ').replace('  ', '').strip()
    file.GetContentFile(name, acknowledge_abuse=True)
    subprocess.call(['bash', 'it.sh', name, date.today().strftime('%d')])

    # file.delete()
