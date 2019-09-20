'''
In 3 lines of code, fetch the HTML text from codingnomads' main page
and print it to your console.

TIP:
- if you wonder what to use, google something like
    "most popular python package"
- if you run into encoding/decoding errors, you're experiencing something
    very common. head over to SO and find a solution!

'''

from bs4 import BeautifulSoup
import requests

page_link = "https://codingnomads.co/"
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")
print(page_content)

'''
Method: https://codeburst.io/web-scraping-101-with-python-beautiful-soup-bb617be1f486
'''