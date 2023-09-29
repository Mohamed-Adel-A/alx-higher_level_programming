#!/usr/bin/python3
"""
a Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    from urllib import request
    from urllib.error import HTTPError
    from sys import argv

    try:
        with request.urlopen(argv[1]) as response:
            result = response.read().decode("utf-8")
    except HTTPError as ex:
        print("Error code", ex.code)
