#!/bin/bash
# the script that sends a DELETE request passed to the url as the first argument
curl -sX DELETE "$1"
