from os import remove
from os.path import split

import requests
from bs4 import BeautifulSoup

url = ('https://pitergsm.ru/catalog/phones/iphone/iphone-se-2022/14459/'
       )

response = requests.get(url)
text = response.text
soup = BeautifulSoup(text)
set = soup.prettify()[soup.prettify().index('<div class="tabs__tab js_tabs_tab" id="tab-specs">'):soup.prettify().index('<div class="tabs__tab js_tabs_tab" id="tab-delivery">')]
set_text = set.split(' ')
new_text = [item for item in set_text if item != '']
print(new_text)
diagonal, screen,matrix,resolution,plotnost ,mod= '','','','','',''
if 'дюйм\n' in new_text and 'Тип' in new_text :
    diagonal = new_text[new_text.index( 'дюйм\n')+6:new_text.index('Тип')-7]
if 'Тип' in new_text and 'Разрешение' in new_text :
    screen = new_text[new_text.index( 'Тип')+5:new_text.index('Разрешение')-6]
if 'Разрешение' in new_text and 'Плотность' in new_text :
    resolution = new_text[new_text.index( 'Разрешение')+7:new_text.index('Плотность')-7]
if 'Матрица\n' in new_text and 'Плотность' in new_text :
    plotnost = new_text[new_text.index( 'Плотность')+6:new_text.index('Матрица\n')-6]
if 'Матрица\n' in new_text and 'Беспроводная' in new_text :
    matrix = new_text[new_text.index( 'Матрица\n')+6:new_text.index('Беспроводная')-9]
if 'связи\n' in new_text and 'Стандарт' in new_text:
    mod = new_text[new_text.index('связи\n')+6 :new_text.index('Стандарт')-7 ]
##if ''
##if 'связи\n' in new_text and 'Стандарт' in new_text:
##    mod = new_text[new_text.index('Стандарт')+6 :new_text.index('Стандарт')-7 ]
print(diagonal, screen, resolution, plotnost, matrix, mod)

##print(soup.prettify()[soup.prettify().index('<div class="tabs__tab js_tabs_tab" id="tab-specs">'):soup.prettify().index('<div class="tabs__tab js_tabs_tab" id="tab-delivery">')])
##for i in range(soup.prettify().index('<div class="tabs__tab js_tabs_tab" id="tab-specs">'), soup.prettify().index('<div class="tabs__tab js_tabs_tab" id="tab-delivery">')):
##    print(soup.prettify()[i],' ')

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

def parse_iphone_specs(data):
    new_text = ' '.join(data)
    specs = {}

    if 'Диагональ экрана, дюйм' in new_text and 'Тип экрана' in new_text:
        specs['diagonal'] = new_text[new_text.index('Диагональ экрана, дюйм') + len('Диагональ экрана, дюйм'):new_text.index('Тип экрана')].strip()

    if 'Тип экрана' in new_text and 'Разрешение экрана' in new_text:
        specs['screen_type'] = new_text[new_text.index('Тип экрана') + len('Тип экрана'):new_text.index('Разрешение экрана')].strip()
    if 'Разрешение экрана' in new_text and 'Плотность пикселей, ppi' in new_text:
        specs['resolution'] = new_text[new_text.index('Разрешение экрана') + len('Разрешение экрана'):new_text.index('Плотность пикселей, ppi')].strip()
    if 'Плотность пикселей, ppi' in new_text and 'Беспроводная связь' in new_text:
        specs['ppi'] = new_text[new_text.index('Плотность пикселей, ppi') + len('Плотность пикселей, ppi'):new_text.index('Беспроводная связь')].strip()


    if 'Модуль сотовой связи' in new_text and 'Стандарт Wi-Fi' in new_text:
        specs['cellular_module'] = new_text[new_text.index('Модуль сотовой связи') + len('Модуль сотовой связи'):new_text.index('Стандарт Wi-Fi')].strip()
    if 'Стандарт Wi-Fi' in new_text and 'Bluetooth' in new_text:
        specs['wifi_standard'] = new_text[new_text.index('Стандарт Wi-Fi') + len('Стандарт Wi-Fi'):new_text.index('Bluetooth')].strip()
    if 'Bluetooth' in new_text and 'Версия Bluetooth' in new_text:
        specs['bluetooth'] = new_text[new_text.index('Bluetooth') + len('Bluetooth'):new_text.index('Версия Bluetooth')].strip()
    if 'Версия Bluetooth' in new_text and 'Другое' in new_text:
        specs['bluetooth_version'] = new_text[new_text.index('Версия Bluetooth') + len('Версия Bluetooth'):new_text.index('Другое')].strip()
    if 'Другое' in new_text and 'SIM-карта' in new_text:
        specs['other_wireless'] = new_text[new_text.index('Другое') + len('Другое'):new_text.index('SIM-карта')].strip()


    if 'Количество физических SIM' in new_text and 'Тип SIM-карты' in new_text:
        specs['sim_count'] = new_text[new_text.index('Количество физических SIM') + len('Количество физических SIM'):new_text.index('Тип SIM-карты')].strip()
    if 'Тип SIM-карты' in new_text and 'Дополнительная информация' in new_text:
        specs['sim_type'] = new_text[new_text.index('Тип SIM-карты') + len('Тип SIM-карты'):new_text.index('Дополнительная информация')].strip()


    if 'Сканер отпечатков пальца' in new_text and 'Общее' in new_text:
        specs['fingerprint_scanner'] = new_text[new_text.index('Сканер отпечатков пальца') + len('Сканер отпечатков пальца'):new_text.index('Общее')].strip()


    if 'Год релиза' in new_text and 'Система' in new_text:
        specs['release_year'] = new_text[new_text.index('Год релиза') + len('Год релиза'):new_text.index('Система')].strip()


    if 'ОС' in new_text and 'Процессор' in new_text:
        specs['os'] = new_text[new_text.index('ОС') + len('ОС'):new_text.index('Процессор')].strip()
    if 'Процессор' in new_text and 'Количество ядер' in new_text:
        specs['processor'] = new_text[new_text.index('Процессор') + len('Процессор'):new_text.index('Количество ядер')].strip()
    if 'Количество ядер' in new_text and 'Видеопроцессор' in new_text:
        specs['cores'] = new_text[new_text.index('Количество ядер') + len('Количество ядер'):new_text.index('Видеопроцессор')].strip()
    if 'Видеопроцессор' in new_text and 'Слот для карты памяти' in new_text:
        specs['gpu'] = new_text[new_text.index('Видеопроцессор') + len('Видеопроцессор'):new_text.index('Слот для карты памяти')].strip()
    if 'Слот для карты памяти' in new_text and 'Обяз. к предустановке ПО' in new_text:
        specs['memory_slot'] = new_text[new_text.index('Слот для карты памяти') + len('Слот для карты памяти'):new_text.index('Обяз. к предустановке ПО')].strip()
    if 'Обяз. к предустановке ПО' in new_text and 'Фотокамера' in new_text:
        specs['preinstalled_software'] = new_text[new_text.index('Обяз. к предустановке ПО') + len('Обяз. к предустановке ПО'):new_text.index('Фотокамера')].strip()


    if 'Камера, Мп' in new_text and 'Диафрагма' in new_text:
        specs['camera_mp'] = new_text[new_text.index('Камера, Мп') + len('Камера, Мп'):new_text.index('Диафрагма')].strip()
    if 'Диафрагма' in new_text and 'Фронтальная камера, Мп' in new_text:
        specs['aperture'] = new_text[new_text.index('Диафрагма') + len('Диафрагма'):new_text.index('Фронтальная камера, Мп')].strip()
    if 'Фронтальная камера, Мп' in new_text and 'Интерфейсы и разъёмы' in new_text:
        specs['front_camera_mp'] = new_text[new_text.index('Фронтальная камера, Мп') + len('Фронтальная камера, Мп'):new_text.index('Интерфейсы и разъёмы')].strip()


    if 'Интерфейсы' in new_text and 'Другие функции' in new_text:
        specs['interfaces'] = new_text[new_text.index('Интерфейсы') + len('Интерфейсы'):new_text.index('Другие функции')].strip()


    if 'Системы навигации' in new_text and 'Датчики' in new_text:
        specs['navigation_systems'] = new_text[new_text.index('Системы навигации') + len('Системы навигации'):new_text.index('Датчики')].strip()
    if 'Датчики' in new_text and 'Поддерживаемые форматы' in new_text:
        specs['sensors'] = new_text[new_text.index('Датчики') + len('Датчики'):new_text.index('Поддерживаемые форматы')].strip()


    if 'Формат видео' in new_text and 'Формат аудио' in new_text:
        specs['video_formats'] = new_text[new_text.index('Формат видео') + len('Формат видео'):new_text.index('Формат аудио')].strip()
    if 'Формат аудио' in new_text and 'Аккумулятор и время работы' in new_text:
        specs['audio_formats'] = new_text[new_text.index('Формат аудио') + len('Формат аудио'):new_text.index('Аккумулятор и время работы')].strip()


    if 'Воспроизведение музыки, ч' in new_text and 'Тип аккумулятора' in new_text:
        specs['music_playback_hours'] = new_text[new_text.index('Воспроизведение музыки, ч') + len('Воспроизведение музыки, ч'):new_text.index('Тип аккумулятора')].strip()
    if 'Тип аккумулятора' in new_text and 'Размеры и вес' in new_text:
        specs['battery_type'] = new_text[new_text.index('Тип аккумулятора') + len('Тип аккумулятора'):new_text.index('Размеры и вес')].strip()
print(parse_iphone_specs(new_text))

##print(key_words('https://pitergsm.ru/catalog/phones/iphone/iphone-13/12124/'))
## <div class="tabs__tab js_tabs_tab" id="tab-specs">