from mp3Ripper import download_soundcloud_files

#testing download_url
if not download_soundcloud_files("https://soundcloud.com/chloeburbank/i-dont-wanna-waste-my-time",'i-dont-wanna-waste-my-time'):
    print('[!] download_url failed')