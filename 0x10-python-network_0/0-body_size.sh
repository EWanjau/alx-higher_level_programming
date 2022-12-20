#!/usr/bin/env bash
# script sends a request tto URL and displays the size of the response in bytes
curl -s "$1" | wc -c