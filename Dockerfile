FROM amazonlinux:latest

# install packages
RUN yum -y update
RUN yum -y install curl vim less wget
RUN yum -y install git

# set LANG & timezone
ENV LANG=ja_JP.UTF-8
RUN rm -f /etc/localtime
RUN ln -fs /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
RUN echo 'ZONE="Asia/Tokyo"' > /etc/sysconfig/clock

# Common alias
RUN echo "alias ll='ls -la'" >> ~/.bashrc
RUN echo "alias vi=vim" >> ~/.bashrc

# serverless framework
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 6.11.2

RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash \
    && . $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default \
    && npm install -g serverless

ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH      $NVM_DIR/v$NODE_VERSION/bin:$PATH
RUN echo ". $NVM_DIR/nvm.sh" >> ~/.bashrc

# Python

ENV PYTHON_VERSION 3.6.1

RUN yum install gcc zlib zlib-devel openssl openssl-devel libffi libffi-devel wget zip -y && \
    yum clean all

RUN wget https://www.python.org/static/files/pubkeys.txt && \
    gpg --import pubkeys.txt; exit 0

RUN wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz && \
    wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz.asc && \
    gpg --verify Python-${PYTHON_VERSION}.tgz.asc && \
    tar -xvzf Python-${PYTHON_VERSION}.tgz && \
    cd Python-${PYTHON_VERSION} && \
    ./configure && \
    make && \
    make install && \
    cd .. && \
    rm -fr Python-${PYTHON_VERSION}

# Install awscli
RUN pip3 install awscli

# MoviePy

WORKDIR /root
RUN yum -y install gcc-c++
RUN git clone https://github.com/vitolimandibhrata/aws-lambda-numpy.git
RUN wget https://github.com/imageio/imageio-binaries/raw/master/freeimage/libfreeimage-3.16.0-linux64.so -O ./libfreeimage.so
#lambda_image_to_video/lib/libfreeimage.so
RUN wget https://github.com/imageio/imageio-binaries/raw/master/ffmpeg/ffmpeg.linux64 -O ./ffmpeg.linux64




# work dir
RUN mkdir -p /opt/share
WORKDIR /opt/share
