FROM ubuntu:22.04

ENV https_proxy=http://proxy-dmz.intel.com:912
ENV http_proxy=http://proxy-dmz.intel.com:911

RUN apt-get update
RUN apt-get install -y python3-numpy python3-scipy python3-pip build-essential git
RUN pip3 install -U pip
RUN python3 --version | grep 'Python 3.10'

WORKDIR /home/app
COPY requirements.txt run_algorithm.py ./
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "-u", "run_algorithm.py"]
