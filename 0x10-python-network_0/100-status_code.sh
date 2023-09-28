#!/bin/bash
# Send request to URL .
awk 'NR==1{printf "%s", $2}' headers "$(curl -sI "$1" -o headers)"
