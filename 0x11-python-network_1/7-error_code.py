#!/usr/bin/python3
"""
a Python script that takes in a URL,
sends a request to the URL and displays the body of the response.
"""


if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    st_code = r.status_code

    if st_code >= 400:
        print("Error code: {}".format(st_code))
    else:
        print(r.text)
