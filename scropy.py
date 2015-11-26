import os
import clipboard
import requests
import datetime
import sys

# Set a local location to save screenshots
directory = os.path.expanduser("~/screenshots/")
# Set an owner name, blank for no owner
owner = ""
# Set a password, blank for no password
password = ""

def supload():
    filename = "Screenshot_" + datetime.datetime.now().strftime("%m-%d-%y_%I.%M.%S%p") + ".png"
    path = os.path.join(directory, filename)
    if not os.path.exists(directory):
        os.makedirs(directory)
    try:
        os.system("scrot -s " + path)
    except:
        sys.exit(0)

    file = {'file': (filename, open(path, 'rb'), 'image/png')}
    url = "http://frogbox.es/whff/upload.php?raw"
    payload = {'owner': owner, 'password':password}
    r = requests.post(url, files=file, data=payload)

    clipboard.copy("http://i.frogbox.es/" + r.text + ".png")

def tupload():
    filename = "Clipboard_" + datetime.datetime.now().strftime("%m-%d-%y_%I.%M.%S%p") + ".txt"
    path = os.path.join(directory, filename)
    if not os.path.exists(directory):
        os.makedirs(directory)
 
    try:                                                                                                                                                          
        text = clipboard.paste()
    except:
        sys.exit(0)
 
    f = open(path, 'w')
    f.write(text)
    f.close()
 
    file = {'file': (filename, open(path, 'r'), 'text/plain')}
    url = "http://frogbox.es/whff/upload.php?raw"
    payload = {'owner': owner, 'password':password}
    r = requests.post(url, files=file, data=payload)
 
    clipboard.copy("http://i.frogbox.es/" + r.text + ".txt")
 
if sys.argv[1] == "-s":
    supload()
elif sys.argv[1] == "-t":
    tupload()
else:
    print "-s [screenshot] / -t [text clipboard]"
    sys.exit(0)


