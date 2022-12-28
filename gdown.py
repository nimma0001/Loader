from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import argparse
import subprocess
frpm datetime import date

parser = argparse.ArgumentParser(description='google rive upload and download')
parser.add_argument("-l", "--links", help="Prints the supplied argument.", nargs='*')
args = parser.parse_args()

gauth = GoogleAuth()
gauth.LoadCredentialsFile('token.json')
drive = GoogleDrive(gauth)

for arg in args.links:
    link = arg.split('=')[1]
    file = drive.CreateFile({'id': link})
    name = file['title']
    name = name.lower().replace('1337xhd.', '').replace('mlsbd.shop', ' ').replace('shop',' ').replace('-', ' ').replace('  ', '').strip()
    file.GetContentFile(name, acknowledge_abuse=True)
    subprocess.call(['bash', 'did.sh', name, date.today().strftime('%d')])

    # file.delete()