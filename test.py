from mp3Ripper import download_url

#testing download_url
if not download_url("https://soundcloud.com/chloeburbank/i-dont-wanna-waste-my-time",'i-dont-wanna-waste-my-time'):
    print('[!] download_url failed')