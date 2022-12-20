#!/bin/bash
# the script gives size of header from the curl request
curl -sI "$1" | grep -i content-length | awk '{print $2}'
