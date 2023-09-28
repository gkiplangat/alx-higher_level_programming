#!/bin/bash
# Take URL & displays all HTTP methods server will accept
curl -sI $1 | grep Allow | cut -d ' ' -f2-
