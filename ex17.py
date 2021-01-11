import requests
import openpyxl
from bs4 import BeautifulSoup

n = int(input("Enter a number : "))

wb = openpyxl.load_workbook('ticker.xlsx')
ws = wb['ticker']
ticker_list = []
for i in range(2,n+2): #3048
  ticker_list.append(ws.cell(row=i, column=1).value[1:])

all_list = []
for ticker in ticker_list:
  
  url = 'https://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A' \
    + ticker + '&cID=&MenuYn=Y&ReportGB=&NewMenuID=11&stkGb=&strResearchYN='

  r = requests.get(url)
  r_html_str = r.text

  soup = BeautifulSoup(r_html_str, 'html.parser')
  tag = soup.find(id='div3')
  if tag != None:
    tag.get_text('//', strip=True)

  all_list.append(tag)
  print(ticker_list.index(ticker))

print(len(all_list))
print(all_list)