#!/usr/bin/python3
"""
a Python script that takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id variable
found in the header of the response.
"""


if __name__ == "__main__":
    from urllib import request
    import sys

    with request.urlopen(sys.argv[1]) as response:
        req_id = response.headers["X-Request-Id"]
        print(req_id)
