#!/bin/bash
# the script that displays HTTP methods the server accepts
curl -svX OPTIONS "$1"
