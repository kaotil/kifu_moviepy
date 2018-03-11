- Docker
[amazonlinux-python36](https://github.com/Smart-Flows/amazonlinux-python36/blob/master/Dockerfile)
[AWS Lambdaでタイムラプス動画を作る](http://qiita.com/sparkgene/items/3e4b1b536b5adec99f56)
[lambda_image_to_video](https://github.com/sparkgene/lambda_image_to_video)

```
$ docker build -t i_kifupy .
$ docker run -itd -v `pwd`/share:/opt/share --name c_kifupy i_kifupy
$ docker exec -it c_kifupy /bin/bash
$ docker stop c_kifupy
$ docker start c_kifupy
$ docker exec -it c_kifupy /bin/bash

$ docker run -it i_kifupye /bin/bash
MoviePy & sls
# cd /opt/share/
# sls create -t aws-python -p kifu_moviepy
# cd kifu_moviepy/

  - python2 でしか使えないっぽい 不要
  # cp -R /root/aws-lambda-numpy/lib /opt/share/kifu_moviepy
  # cp -R /root/aws-lambda-numpy/numpy /opt/share/kifu_moviepy
  # cp /root/libfreeimage.so /opt/share/kifu_moviepy/lib/libfreeimage.so

# cp /root/ffmpeg.linux64 /opt/share/kifu_moviepy/ffmpeg.linux64
# requirements.txt
  moviepy
# mkdir vendor
# pip3 install -r requirements.txt -t ./vendor

# chmod 755 /opt/share/kifu_moviepy/ffmpeg.linux64
# vi serverless.yml
service: kifu-moviepy
provider:
  name: aws
  runtime: python3.6
  stage: dev
  region: ap-northeast-1
functions:
  kifu_moviepy:
    handler: lambda_function.lambda_handler
package:
  exclude:
    - .gitignore
    - README.md
    - "*.pyc"
    - video/**

# sls invoke local -f hello
# sls invoke local -f kifu_moviepy
# pip3 install boto3
# sls deploy -v
# sls invoke -f kifu_moviepy
- エラーが出たら
# sls logs -f kifu_moviepy

MoviePy
pip3 install gaizeh
yum install cairo-devel
python3 sample.py

- youtube-dl
curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
chmod a+rx /usr/local/bin/youtube-dl

# pip3 install scipy
# yum install ImageMagick
# yum install ImageMagick-devel

- imagemagick
# convert -background transparent -fill white -font Courier -pointsize 70 -gravity center label:@/tmp/tmp2vyjbsqy.txt -type truecolormatte PNG32:/tmp/tmpfnx58orp.png
convert: not authorized `@/tmp/tmp2vyjbsqy.txt' @ error/constitute.c/ReadImage/454.
convert: no images defined `PNG32:/tmp/tmpfnx58orp.png' @ error/convert.c/ConvertImageCommand/3046.

# vi /etc/ImageMagick/policy.xml
  <!-- <policy domain="coder" rights="none" pattern="TEXT" /> -->
  <!-- <policy domain="coder" rights="none" pattern="LABEL" /> -->
  <!-- <policy domain="path" rights="none" pattern="@*" /> -->


bash-4.2# ll
total 27908
drwxr-xr-x 14 root root      476  8月 18 15:52 .
drwxr-xr-x  3 root root      102  8月 18 14:46 ..
-rw-r--r--  1 root root      192  8月 18 14:46 .gitignore
drwxr-xr-x  3 root root      102  8月 18 15:40 __pycache__
-rw-r--r--  1 root root 28549024  8月 18 15:11 ffmpeg.linux64
-rw-r--r--  1 root root      490  8月 18 14:46 handler.py
-rw-r--r--  1 root root      459  8月 18 15:27 handler.pyc
-rw-r--r--  1 root root     2803  8月 18 15:39 lambda_function.py
-rw-r--r--  1 root root     3280  8月 18 15:30 lambda_function.pyc
drwxr-xr-x 12 root root      408  8月 18 15:08 lib
drwxr-xr-x 35 root root     1190  8月 18 15:40 numpy
-rw-r--r--  1 root root        8  8月 18 15:12 requirements.txt
-rw-r--r--  1 root root     2882  8月 18 15:33 serverless.yml
drwxr-xr-x 19 root root      646  8月 18 15:15 vendor

# pip3 install -r requirements.txt -t ./
bash-4.2# ll
total 27928
drwxr-xr-x  29 root root      986  8月 18 16:05 .
drwxr-xr-x   3 root root      102  8月 18 14:46 ..
-rw-r--r--   1 root root      192  8月 18 14:46 .gitignore
-rw-r--r--   1 root root     1047  8月 18 16:05 OleFileIO_PL.py
drwxr-xr-x 101 root root     3434  8月 18 16:05 PIL
drwxr-xr-x  10 root root      340  8月 18 16:05 Pillow-4.2.1.dist-info
drwxr-xr-x   3 root root      102  8月 18 15:40 __pycache__
drwxr-xr-x  10 root root      340  8月 18 16:05 decorator-4.0.11.dist-info
-rw-r--r--   1 root root    15649  8月 18 16:05 decorator.py
-rw-r--r--   1 root root 28549024  8月 18 15:11 ffmpeg.linux64
-rw-r--r--   1 root root      490  8月 18 14:46 handler.py
-rw-r--r--   1 root root      459  8月 18 15:27 handler.pyc
drwxr-xr-x   9 root root      306  8月 18 16:05 imageio
drwxr-xr-x   8 root root      272  8月 18 16:05 imageio-2.1.2-py3.6.egg-info
-rw-r--r--   1 root root     2803  8月 18 15:39 lambda_function.py
-rw-r--r--   1 root root     3280  8月 18 15:30 lambda_function.pyc
drwxr-xr-x  12 root root      408  8月 18 15:08 lib
drwxr-xr-x  14 root root      476  8月 18 16:05 moviepy
drwxr-xr-x   9 root root      306  8月 18 16:05 moviepy-0.2.3.2.dist-info
drwxr-xr-x  35 root root     1190  8月 18 15:40 numpy
drwxr-xr-x   9 root root      306  8月 18 16:05 numpy-1.13.1.dist-info
drwxr-xr-x   9 root root      306  8月 18 16:05 olefile
drwxr-xr-x   7 root root      238  8月 18 16:05 olefile-0.44-py3.6.egg-info
-rw-r--r--   1 root root        8  8月 18 15:12 requirements.txt
-rw-r--r--   1 root root     2882  8月 18 15:33 serverless.yml
drwxr-xr-x  19 root root      646  8月 18 16:05 tests
drwxr-xr-x  12 root root      408  8月 18 16:05 tqdm
drwxr-xr-x  10 root root      340  8月 18 16:05 tqdm-4.11.2.dist-info
drwxr-xr-x  19 root root      646  8月 18 15:15 vendor

# pip3 install numpy -t ./vendor
