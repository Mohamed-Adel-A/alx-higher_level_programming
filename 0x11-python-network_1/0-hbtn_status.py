#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    from urllib import request
    
    r = request.urlopen("https://alx-intranet.hbtn.io/status")
    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        data = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode('utf-8')))
