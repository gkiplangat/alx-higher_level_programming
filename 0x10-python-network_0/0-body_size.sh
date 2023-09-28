#!/bin/bash
# Send request to URL with curl & displays the size of body of the response.
curl -s "$1" | wc -c
