#!/bin/bash
# Takes in URL & displays all HTTP methods the server will accept
curl -s -I "$1" | grep -i 'Allow' | cut -d ' ' -f 2-
