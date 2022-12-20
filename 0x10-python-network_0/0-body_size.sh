#!/usr/bin/env bash
curl -sI "$1" | grep -i content-length | awk '{print $2}'

