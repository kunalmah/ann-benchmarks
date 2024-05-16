FROM milvusdb/knowhere-env:pyknowhere1.3-20230303

WORKDIR /home/app
COPY run_algorithm.py requirements.txt ./
ENV https_proxy=http://proxy-dmz.intel.com:912
ENV http_proxy=http://proxy-dmz.intel.com:911

# update python packages
RUN python3 -m pip install -r requirements.txt
RUN python3 -m pip install scipy==1.10.1
RUN python3 -c 'import pyknowhere'

ENTRYPOINT ["python3", "-u", "run_algorithm.py"]
