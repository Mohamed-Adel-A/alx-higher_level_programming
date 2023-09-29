#!/usr/bin/python3
"""
a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""


if __name__ == "__main__":
    from urllib import request
    from urllib import parse
    import sys
    

    values = {"email": sys.argv[1]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    with request.urlopen(sys.argv[1], data) as response:
        result = response.read().decode("utf-8")
        print(result)
