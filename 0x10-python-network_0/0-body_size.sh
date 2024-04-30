#!/bin/bash
# this script takes in a url, sends and displays
# the size of the body of response

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a request to the URL and get the size of the response body in bytes
response_size=$(curl -s -o /dev/null -w "%{size_download}" "$1")

# Display the size of the response body
echo "Size of the response body: $response_size bytes"
