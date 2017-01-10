#!/usr/bin/env python

import requests

print requests .__version__


response = requests.get("https://raw.githubusercontent.com/joshdeng/comput404lab1/master/checkversion.py")

print response.status_code

print response.text