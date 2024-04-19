FROM redislabs/redisearch as redisearch
FROM ann-benchmarks

ENV https_proxy=http://proxy-dmz.intel.com:912
ENV http_proxy=http://proxy-dmz.intel.com:911

# Install Redis
RUN apt-get update && apt-get install -y curl lsb-core
RUN curl -fsSL https://packages.redis.io/gpg | gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
RUN echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/redis.list
RUN apt-get update
RUN apt-get install -y redis

COPY --from=redisearch /usr/lib/redis/modules/redisearch.so /usr/lib/redis/modules/redisearch.so

RUN pip3 install redisearch redis
