import subprocess

subprocess.run([
    'ffmpeg', '-i', 'in.mp4',
    '-vcodec', 'libx264', '-crf', '28',
    'out.mp4'
])
