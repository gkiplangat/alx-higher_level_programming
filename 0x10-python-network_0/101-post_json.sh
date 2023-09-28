#!/bin/bash
# Send JSON POST request to URL.
curl -s -d "@$2" -H "Content-Type: application/json" -X POST "$1"
