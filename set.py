import requests
from bs4 import BeautifulSoup

url = 'https://pitergsm.ru/catalog/phones/iphone/iphone-13/12124/'

response = requests.get(url)
text = response.text
soup = BeautifulSoup(text)
print(soup.prettify())

def key_words(url):
    response = requests.get(url)
    text = response.text.split('\n')[0]
    words = text.split()
    first_index = words.index('купить')
    last_index = words.index('по')
    return words[first_index+1:last_index]

keywords_array = key_words('https://pitergsm.ru/catalog/phones/iphone/iphone-13/12124/')

def keywords_search(keywords_array):
    pass


print(key_words('https://pitergsm.ru/catalog/phones/iphone/iphone-13/12124/'))
