import subprocess

def generate_mov(filename):
    subprocess.call(['ffmpeg', '-i', f'{filename}.jpg', '-i', f'{filename}.mp3', '-y', f'{filename}.mp4'])

if __name__ == '__main__':
    generate_mov('i-dont-wanna-waste-my-time')