import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import os

URL_TEMPLATE = "https://coinmarketcap.com/"
page = requests.get(URL_TEMPLATE)

if page.status_code == 200:
  soup = bs(page.text, "html.parser")

  content = []

  table = soup.find_all("table", class_="cmc-table")

  for tr in table:
    for item in tr.find_all("tr"):
      content.append(item)
  content.pop(0)

  result = []
  for item in content:
      coin = {}
      if not item.has_attr("class"):
          coin = {
              "name": item.find(class_="sc-4984dd93-0 kKpPOn").text, 
              "symbol": item.find(class_="sc-4984dd93-0 iqdbQL coin-item-symbol").text,
              "price": item.find(class_="sc-cadad039-0 clgqXO").text,
              "cap": item.find(class_="sc-4984dd93-0 jZrMxO").find(class_="sc-edc9a476-1 gqomIJ").text
          }
          result.append(coin)

def all():
    print("%-15s %-15s %-15s %-20s" % ("Name", "Symbol", "Price", "Cap"))
    for item in result:      
        print("%-15s %-15s %-15s %-20s" % (item.get("name"), item.get("symbol"), item.get("price"), item.get("cap")))

def search():
    name = input()
    element = None
    for item in result:
        if item.get("name") == name:
            element = item
            break
    if element is not None:
        print("%-15s %-15s %-15s %-20s" % ("Name", "Symbol", "Price", "Cap"))
        print("%-15s %-15s %-15s %-20s" % (element.get("name"), element.get("symbol"), element.get("price"), element.get("cap")))
    else:
        print(" Валюта не найдена")

os.system('cls')
print("   Меню \n 1. Печать списком \n 2. Поиск")

match input():
    case "1":
        os.system('cls')
        all()
    case "2":
        os.system('cls')
        print(" Введите название: ")
        search()
    case _:
        print("Error")
