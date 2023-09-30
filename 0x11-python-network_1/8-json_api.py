#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) == 2:
        values = {"q": sys.argv[1]}
    else:
        values = {"q": ""}

    r = requests.post("http://0.0.0.0:5000/search_user", values)
    try:
        r_json = r.json()
        if r_json:
            print("[{}] {}".format(r_json['id']), r_json['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
        
