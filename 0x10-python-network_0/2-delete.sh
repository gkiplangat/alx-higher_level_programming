#!/bin/bash
# Sends DELETE request to URL passed as the 1st argument & displays body of the response.
curl -s "$1" -X DELETE
