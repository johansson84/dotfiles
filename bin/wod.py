from bs4 import BeautifulSoup
import urllib.request

with urllib.request.urlopen('http://www.crossfitvaxjo.se/wod/') as response:
   html = response.read()

wod = BeautifulSoup(html, 'html.parser').find(id="start-wod")

print(wod.get_text('\n'))
