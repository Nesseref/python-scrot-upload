import os
import clipboard
import requests
import datetime

# Set a local location to save screenshots
directory = os.path.expanduser("~/screenshots/")
# Set an owner name, blank for no owner
owner = ""
# Set a password, blank for no password
password = ""

filename = "Screenshot_" + datetime.datetime.now().strftime("%m-%d-%y_%I.%M.%S%p") + ".png"
path = os.path.join(directory, filename)
if not os.path.exists(directory):
        os.makedirs(directory)
os.system("scrot -s " + path)

file = {'file': (filename, open(path, 'rb'), 'image/png')}
url = "http://frogbox.es/whff/upload.php?raw"
payload = {'owner': owner, 'password':password}
r = requests.post(url, files=file, data=payload)

clipboard.copy("http://i.frogbox.es/" + r.text + ".png")
