import time
import string
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from tabulate import tabulate
import numpy as np

#Update driver here: https://sites.google.com/chromium.org/driver/
PATH = r"C:\Users\GregM\Documents\VSCode\Python\Runescape\Skilling\Crafting\chromedriver.exe"
browser = webdriver.Chrome(PATH)

# Sapphire Ring:        1637
# Sapphire Necklace:    1656
# Sapphire Bracelet:    11072
# Emerald Ring:         1639
# Emerald Necklace:     1658
# Emerald Bracelet:     11076
# Ruby Ring:            1641
# Ruby Necklace:        1660
# Ruby Bracelet:        11085

# Sapphire:             1607
# Emerald:              1605
# Ruby:                 1603
# Gold Bar:             2357

A = np.array(["Name", "Cost"])
B = np.array(["Name", "Cost", "Profit"])
raw_materials = np.array([1607, 1605, 1603, 2357])
crafted = np.array([1637, 1656, 11072, 1639, 1658, 11076, 1641, 1660, 11085])

def get_price(id):
    price_page = "https://prices.runescape.wiki/osrs/item/" + str(id)
    browser.get(price_page)
    price_retrieve = browser.find_element(By.CLASS_NAME, 'wgl-item-price')
    price = price_retrieve.text
    name_retrieve = browser.find_element(By.TAG_NAME, 'h3')
    name = name_retrieve.text
    return price, name

def parse_price(pa):
    for k in range(len(pa)):
        if(pa[k] == "c"):
            pa_return = float(pa[0:(k-1)].replace(',',''))
            return pa_return

for x in raw_materials:
    [cost_t, name] = get_price(x)
    cost = parse_price(cost_t)
    addendum = np.array([str(name), float(cost)])
    A = np.vstack((A, addendum))

print(tabulate(A))

for k in crafted:
    [cost_t, name] = get_price(k)
    cost = parse_price(cost_t)
    if(str(name)[0:2] == "Sa"):
        addendum = np.array([str(name), float(cost), float(cost) - float(A[1][1]) + float(A[4][1])])
    if(str(name)[0:2] == "Em"):
        addendum = np.array([str(name), float(cost), float(cost) - float(A[2][1]) + float(A[4][1])])
    if(str(name)[0:2] == "Ru"):
        addendum = np.array([str(name), float(cost), float(cost) - float(A[3][1]) + float(A[4][1])])
    B = np.vstack((B, addendum))

print(tabulate(B))
