import sys
from subprocess import run, PIPE
from pathlib import Path

args = sys.argv[1:]
video_file = Path(' '.join(args))
run(['ffmpeg', '-i', video_file.name, '-vcodec', 'h264', '-acodec','aac', video_file.name.replace('.' + video_file.name.split('.')[-1], '-compressed.' + video_file.name.split('.')[-1])])