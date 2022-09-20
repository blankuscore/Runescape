import string
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from tabulate import tabulate
import numpy as np

# List of items:
#
# Steel platebody       1119
# Mithril platebody     1121
# Adamant platebody     1123
# Rune mace             1432
# Rune med helm         1147
# Rune scimitar         1333
# Rune longsword        1303
# Rune full helm        1163
# Rune battleaxe        1373
# Rune chainbody        1113
# Rune kiteshield       1201
# Rune 2h sword         1319
# Rune platelegs        1079
# Rune plateskirt       1093
# Rune platebody        1127
# Rune halberd          3202

def get_price(id):
    price_page = "https://prices.runescape.wiki/osrs/item/" + str(id)
    browser.get(price_page)
    price_retrieve = browser.find_element_by_class_name('wgl-item-price')
    price = price_retrieve.text
    name_retrieve = browser.find_element_by_tag_name('h3')
    name = name_retrieve.text
    high_alch = browser.find_element_by_class_name('wgl-item-details-table')
    highalch = high_alch.text
    return price, name, highalch

def parse_high_alch(ha):
    for i in range(len(ha)):
        if(ha[i] == "H"):
            pos1 = i
        if(ha[i] == "("):
            pos2 = i
            break
    high_alch_return = float(ha[(pos1+9):(pos2-1)].replace(',',''))
    return high_alch_return

def parse_price(pa):
    for k in range(len(pa)):
        if(pa[k] == "c"):
            pa_return = float(pa[0:(k-1)].replace(',',''))
            return pa_return

PATH = r"C:\Users\GregM\Documents\VSCode\Python\Runescape\chromedriver.exe"
browser = webdriver.Chrome(PATH)

A = np.array(["Name", "Cost", "High Alchemy", "Profit"])
id_numbers = np.array([1121,1123,1432,1147,1333,1303,1163,1373,1113,1201,1319,1079,1093,1127,3202,12484,2503,4087,7158,4585,1305, 3204, 1215, 1377,1347,2499,2501])

for x in id_numbers:
    [cost_t, name, higha_t] = get_price(x)
    cost = parse_price(cost_t)
    higha = parse_high_alch(higha_t)
    addendum = np.array([str(name), float(cost), float(higha), float(higha - cost)])
    A = np.vstack((A, addendum))

print(tabulate(A))