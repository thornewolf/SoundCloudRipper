import sys
import requests
import re
from urllib.request import urlopen

url = "https://soundcloud.com/chloeburbank/i-dont-wanna-waste-my-time"
html = requests.get(url)
track_id = re.search(r'soundcloud://sounds:(.+?)"', html.text)
final_page = requests.get("https://api.soundcloud.com/i1/tracks/{0}/streams?client_id=LvWovRaJZlWCHql0bISuum8Bd2KX79mb".format(track_id.group(1)))
download_url = final_page.json()['http_mp3_128_url']

dlmp3 = urlopen(download_url)
with open('testing2.mp3', 'wb') as filee:
    filee.write(dlmp3.read())