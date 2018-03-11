# coding: utf

import os
import datetime
import json
import math
import datetime
import sys
sys.path.append("./vendor")
from pprint import pprint

lambda_tmp_dir = '/tmp'
ffmpeg_bin = "{0}/ffmpeg.linux64".format(lambda_tmp_dir)
os.environ['IMAGEIO_FFMPEG_EXE'] = ffmpeg_bin
from moviepy.editor import *

os.chdir('/opt/share/kifu_moviepy')
clip = (VideoFileClip("video/kifu_movie_20180309_152354.mp4"))
clip.write_gif("gif/kifu_movie_sample.gif")
