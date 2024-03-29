#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id"""

import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./script_name.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            html = response.info()
            value = html.get('X-Request-Id', 'Header not found')
            print(value)
    except Exception as e:
        print("Error:", e)

