#!/usr/bin/python3
"""
This script will send a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

if __name__ == '__main__':
    import urllib.parse
    import urllib.request
    import sys

    argv = sys.argv
    url = argv[1]
    email = argv[2]
    DATA = urllib.parse.urlencode({"email": email})
    DATA = DATA.encode('ascii')

    with urllib.request.urlopen(url, DATA) as response:
        print(response.read().decode('utf-8'))
