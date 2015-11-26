import os
import clipboard
import requests
import datetime

directory = os.path.expanduser("~/screenshots/")
filename = "Screenshot_" + datetime.datetime.now().strftime("%m-%d-%y_%I-%M%p") + ".png"
path = os.path.join(directory, filename)
if not os.path.exists(directory):
        os.makedirs(directory)

os.system("scrot -s " + path)

file = {'file': open(path, 'rb')}
url = "http://frogbox.es/whff/upload.php?raw"
r = requests.post(url, files=file)

clipboard.copy("http://i.frogbox.es/" + r.text + ".png")

