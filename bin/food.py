from bs4 import BeautifulSoup
import urllib.request

with urllib.request.urlopen('http://www.hors.se/restaurang/motesplats-delta/') as response:
   html = response.read()

soup = BeautifulSoup(html, 'html.parser')
foodContainer = soup.find(id='tillmenyn').parent
foodDivs = foodContainer.find_all('div', 'col-xs-10 text-left')

print('')

for div in foodDivs:
	print(div.get_text().strip())
	print('')
