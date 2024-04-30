FROM ann-benchmarks

ENV https_proxy=http://proxy-dmz.intel.com:912
ENV http_proxy=http://proxy-dmz.intel.com:911

RUN apt update && apt install -y wget
# RUN wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
# RUN bash Anaconda3-2020.11-Linux-x86_64.sh -b
# ENV PATH /root/anaconda3/bin:$PATH

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.2-0-Linux-x86_64.sh
RUN chmod a+x Miniconda3-py310_23.5.2-0-Linux-x86_64.sh
RUN bash ./Miniconda3-py310_23.5.2-0-Linux-x86_64.sh -b
ENV PATH /root/miniconda3/bin:$PATH

RUN conda config --set proxy_servers.https proxy-dmz.intel.com:912
RUN conda config --set proxy_servers.http proxy-dmz.intel.com:912

RUN python3 -m pip install ansicolors==1.1.8 docker==5.0.2
RUN conda install -c pytorch h5py numpy mkl=2023 blas=1.0=mkl

# https://developpaper.com/a-pit-of-mkl-library-in-linux-anaconda/
# ENV LD_PRELOAD /root/anaconda3/lib/libmkl_core.so:/root/anaconda3/lib/libmkl_sequential.so

# RUN apt install -y build-essential
# RUN apt install -y wget git vim
RUN apt install -y software-properties-common lsb-release
# WORKDIR /home/
#Install Latest CMake
RUN wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | gpg --dearmor - | tee /etc/apt/trusted.gpg.d/kitware.gpg >/dev/null
RUN apt-add-repository "deb https://apt.kitware.com/ubuntu/ $(lsb_release -cs) main"
RUN apt update -y
RUN apt install kitware-archive-keyring
# RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 6AF7F09730B3F0A4
RUN apt update -y
RUN apt install cmake -y
RUN apt install -y build-essential libtool autoconf unzip wget
# RUN apt-get update -y

#ADD xps-prc-ds-faiss-opt.orig ./faiss
#RUN git clone https://github.com/intel-innersource/libraries.databases.thirdparty.faiss.git ./faiss
ADD ann_benchmarks/algorithms/faiss_amx/faiss_pkg/faiss.tgz ./
RUN apt install swig -y

RUN apt-get install -y python3-dev
RUN apt-get install -y python3-numpy-dev
RUN apt-get install -y python3-pip

RUN git clone https://github.com/oneapi-src/oneDNN.git
#WORKDIR /home/app/oneDNN
RUN mkdir -p /home/app/oneDNN/build \
    && cd /home/app/oneDNN/build \
    && cmake .. \
    && make -j \
    && make install \
    && cp -aP /root/miniconda3/lib/libmkl* /usr/local/lib/


ADD ann_benchmarks/algorithms/faiss_amx/faiss_pkg/run_conda.sh /home/app/faiss/
ADD ann_benchmarks/algorithms/faiss_amx/faiss_pkg/run_conda_env.sh /home/app/faiss/
ADD ann_benchmarks/algorithms/faiss_amx/faiss_pkg/build_faiss.sh /home/app/faiss/
RUN chmod a+x /home/app/faiss/run_conda.sh
RUN chmod a+x /home/app/faiss/run_conda_env.sh
RUN chmod a+x /home/app/faiss/build_faiss.sh

#WORKDIR /home/app/faiss/
RUN cd /home/app/faiss/ \
    && ./run_conda.sh \
    && ./run_conda_env.sh \
    && ./build_faiss.sh

#RUN python3 -c 'import faiss; print(faiss.IndexFlatIP)'
#WORKDIR /home/app
RUN pip3 install psutil
RUN pip3 install pyyaml
RUN pip3 install scikit-learn scipy matplotlib
RUN pip3 install tensorflow
ENV DNNL_ENABLE=1