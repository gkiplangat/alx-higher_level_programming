#!/bin/bash
# Send request to URL passed as an argument & displays only the status code of the response.
awk 'NR==1{printf "%s", $2}' headers "$(curl -sI "$1" -o headers)"
