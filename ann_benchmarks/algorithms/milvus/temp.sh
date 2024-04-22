#!/bin/bash

MILVUS_M=80
sed -i "s/^\([[:space:]]*\)M: \[.*/\1M: [${MILVUS_M}]/" ./config.yml

MILVUS_QUERY_ARGS=250
sed -i "s/^\([[:space:]]*\)query_args: \[\[.*/\1query_args: [[${MILVUS_QUERY_ARGS}]]/" ./config.yml
