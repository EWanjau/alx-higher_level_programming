#!/usr/bin/env bash
# script sends a request tto URL and displays the size of the response in bytes
curl -sI "$1" | grep -i content-length | awk '{print $2}'
