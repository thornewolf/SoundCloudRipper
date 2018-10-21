import sys
import requests
import re
from urllib.request import urlopen

def download_mp3(url,filename):
    html = requests.get(url)
    track_id = re.search(r'soundcloud://sounds:(.+?)"', html.text)
    final_page = requests.get("https://api.soundcloud.com/i1/tracks/{0}/streams?client_id=LvWovRaJZlWCHql0bISuum8Bd2KX79mb".format(track_id.group(1)))
    try:
        download_url = final_page.json()['http_mp3_128_url']
    except:
        print(f'[!] Error parsing page json for \n\t{url}')
        return False

    dlmp3 = urlopen(download_url)
    try:
        with open(f'{filename}.mp3', 'wb') as filee:
            filee.write(dlmp3.read())
        print(f'Sucessfully downloaded {filename}')
    except:
        print(f'[!] Error downloading mp3 for \n\t{url}')
    return True

def download_img(url,filename):
    html = requests.get(url)
    #print(html.text)
    img_match = re.search(r'<img src="(https://.*\.jpg)',html.text)
    if img_match:
        img_url = img_match.group(1)
    else:
        return None
    download(img_url,filename+'.jpg')


def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = requests.get(url)
        # write to file
        file.write(response.content)

def download_soundcloud_files(url, file_name):
    download_mp3(url,file_name)
    download_img(url,file_name)




if __name__=='__main__':
    download_soundcloud_files("https://soundcloud.com/chloeburbank/i-dont-wanna-waste-my-time",'i-dont-wanna-waste-my-time')