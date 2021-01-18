url1 = 'https://www.washingtonpost.com/wp-dyn/content/article/2010/08/29/AR2010082902749.html?sid=ST2010082902923'
url2 = 'http://content.time.com/time/magazine/article/0,9171,2005869,00.html'
url3 = 'https://www.theregister.com/2014/08/26/top_ten_gaming_keyboard_and_mouse_combos/?page=1'

from bs4 import BeautifulSoup
import requests

r = requests.get(url2)
soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.prettify())
list_num = soup.select('div.entry-content.group > p')

for tag in list_num[:6]:
	if tag == list_num[2]:
		print(tag.get_text().strip())
	else:
		print(tag.get_text())

with open('file.txt', 'a', encoding='utf-8') as f:
    for tag in list_num[:6]:
        f.write(tag.get_text().strip())

# list_str = []
# for i in list_num:
# 	list_str.append(str(i))

# html_str = ''.join(list_str)
