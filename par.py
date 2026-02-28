from os import remove
from os.path import split

import requests
from bs4 import BeautifulSoup
import re
from requests import delete

url = 'https://pitergsm.ru/catalog/phones/iphone/iphone-17-pro/esim/122632/'

def parse_simple(url):
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text)
    set = soup.prettify()[soup.prettify().index('<div class="tabs__tab js_tabs_tab" id="tab-specs">'):soup.prettify().index('<div class="tabs__tab js_tabs_tab" id="tab-delivery">')]
    set_text = set.split(' ')
    new_text = [item for item in set_text if item != '']
    new_text =[item for item in new_text if not re.search(r'[a-zA-Z]', item)]
    return new_text

print(parse_simple(url))



def par(new_text):
    new_text =[item for item in new_text if not re.search(r'[a-zA-Z]', item)]

    new_text = new_text[0, new_text.index('Размеры')]
    return new_text
print(par(parse_simple(url)))