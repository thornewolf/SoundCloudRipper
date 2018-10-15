import sys
import requests
import re

url = sys.argv[-1]
html = requests.get(url)