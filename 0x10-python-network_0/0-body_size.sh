#!/bin/bash
# Send request to URL with curl.
curl -sI "$1" | grep Content-Length | cut -d " " -f 2
