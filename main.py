import mp3Ripper
import mp4Creator
import re

def main():
    url = 'https://soundcloud.com/chloeburbank/i-dont-wanna-waste-my-time'
    file_name = re.search(r'soundcloud.com/.*?/(.*)',url).group(1)
    mp3Ripper.download_soundcloud_files(url, file_name)
    mp4Creator.generate_mov(file_name)



if __name__ == '__main__':
    main()
