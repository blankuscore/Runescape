import time
import string
import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from tabulate import tabulate
import numpy as np

import requests
from urllib.request import Request, urlopen
from urllib import request
import json
from io import BytesIO
from PIL import Image

URL_start = "https://www.albion-online-data.com/api/v2/stats/Prices/"
URL_end = ".json?locations=Lymhurst"

character_limit = 2000

build_string = URL_start + URL_end






"""
response = requests.get(URL)
data = response.json()
print(data)
print(data[0])
print(data[0]['item_id'])
print(data[0]['sell_price_max'])
"""

#data = response.json()
#print(data['facts'][0])

#Update driver here: https://sites.google.com/chromium.org/driver/
#PATH = r"C:\Users\GregM\Documents\VSCode\Python\Runescape\Skilling\Crafting\chromedriver.exe"
#browser = webdriver.Chrome(PATH)
#options = Options()
#options.add_experimental_option("excludeSwitches", ["enable-logging"])
#browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)

# Chopped Fish (T1) T1_FISHCHOPS

#A = np.array(["Name", "Cost"])
#B = np.array(["Name", "Cost", "Profit"])
"""
def get_price(id):
    price_page = "https://albiononline2d.com/en/item/id/" + str(id)
    browser.get(price_page)
    price_retrieve = browser.find_element(By.XPATH, '//*[@id="market-table-body"]/tr[4]/td[2]')
    price = price_retrieve.text
    name_retrieve = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[2]/div/div[1]/div[2]/h1')
    name = name_retrieve.text
    return name, price

#print(get_price("T1_FISHCHOPS"))
#print(get_price("T1_SEAWEED"))

"""