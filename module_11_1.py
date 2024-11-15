# Цель: познакомиться с использованием сторонних библиотек в Python и применить их в различных задачах.
#
# Задача:
#
#     Выберите одну или несколько сторонних библиотек Python, например, requests, pandas, numpy, matplotlib, pillow.
#     После выбора библиотек(-и) изучите документацию к ней(ним), ознакомьтесь с их основными возможностями и функциями. К каждой библиотеке дана ссылка на документацию ниже.
#
# Если вы выбрали:
#
#     requests - запросить данные с сайта и вывести их в консоль.
#     pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.
#     numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
#     matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.
#     pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.
#
# В приложении к ссылке на GitHub напишите комментарий о возможностях, которые предоставила вам выбранная библиотека и как вы расширили возможности Python с её помощью.
# Примечания:
#
#     Можете выбрать не более 3-х библиотек для изучения.
#     Желательно продемонстрировать от 3-х функций/классов/методов/операций из каждой выбранной библиотеки.

# query Weather {
#   # Погода в Йошкар-Оле  расположен на 56,6388 северной широты и 47,8908 восточной долготы на высоте 94 метра над уровнем моря
#   weatherByPoint(request: { lat: 56.6388, lon: 47.8908 }) {
#     now {
#       c: temperature
#       f: temperature(unit: FAHRENHEIT)
#       icon(format: SVG)
#     }
#     forecast {
#       hours(first: 48) {
#         edges {
#           node {
#             timestamp
#             temperature
#           }
#         }
#       }
#     }
#   }
# }

access_key = ''     # ключ доступа к яндекс погоде

from pprint import pprint
import requests


def get_temp_by_lat_lon(lat, lon):
    global access_key

    headers = {
        'X-Yandex-Weather-Key': access_key
    }
    response = requests.get('https://api.weather.yandex.ru/v2/forecast?lat=56.6388&lon=47.8908', headers=headers)
    if response.json() == {'message': 'forbidden'}:
        print(f'Доступ к сервису Яндекс погода запрещен. '
              f'Возможно превышено число бесплатных обращений или не верный ключ доступа!')
    else:
        temp = response.json()['fact']['temp']      # temp - температура, pressure_mm-давление, humidity - влажность, wind_speed - скорость ветра,
        # pprint(response.json())
        return temp

    return None


# Погода в Йошкар-Оле  расположен на 56,6388 северной широты и 47,8908 восточной долготы на высоте 94 метра над уровнем моря
#   weatherByPoint(request: { lat: 56.6388, lon: 47.8908 }) {
#temp_i_ola = get_temp_by_lat_lon(56.6388, 47.8908)
temp_i_ola = None
if temp_i_ola is not None:
    print(f"Текущая температура в Йошкар-Оле: {temp_i_ola}")
else:
    print(f"К сожалению температуру в Йошкар-Оле определить не удалось!")

# Информация о заголовке запроса
response = requests.get("https://urban-university.ru/")
print(f"\nИнформация о заголовке запроса: {response.url}")
pprint(response.headers)

# Поис по критериям
query = {'q': 'Россия Природа', 'order': 'popular', 'min_width': '800', 'min_height': '600'}
req = requests.get('https://www.google.com/search?sca_esv=04e68c913ef2a454', params=query)
print(f"Изображение Google Природа России: {req.url}")
query = {'text': 'Россия реки', 'order': 'popular', 'min_width': '800', 'min_height': '600'}
req = requests.get('https://yandex.ru/images/search', params=query)
print(f"Изображение Яндекс Россия реки: {req.url}")

# source: https://code.tutsplus.com/ru/using-the-requests-module-in-python--cms-28204t
def download_image(path, fname):
    print(f"Загрузка изображения url={path}")
    try:
        req = requests.get(path, stream=True)

        req.raise_for_status()

        with open(fname, 'wb') as fd:
            for chunk in req.iter_content(chunk_size=50000):
                #print('Received a Chunk')
                fd.write(chunk)
        print(f"Изображение загружено и сохранено в {fname}")
    except Exception as ex:
        print("В процессе загрузки изображения возникли ошибки: ", ex)

url_img = "https://cdn.culture.ru/images/80e1103d-29ec-5774-8edb-99bc74ddc43c"
fname_img = "downloadImage.jpg"
download_image(url_img, fname_img)

"""
    Пример работы с библиотекой Pillow
    source: https://habr.com/ru/articles/681248/
"""
from PIL import Image
filename = fname_img
with Image.open(filename) as img:
    img.load()
img.show()

# Вращение изображения
print(f"img.format={img.format}, img.size={img.size}, img.mode={img.mode}")
converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
converted_img.show()

# Изменение режима
gray_img = img.convert("L")  # Grayscale
gray_img.show()

"""
    Пример работы с библиотекой matplotlib
    source: https://skillbox.ru/media/code/biblioteka-matplotlib-dlya-postroeniya-grafikov/  
"""
# Первый график
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [25, 32, 34, 20, 25]
plt.plot(x, y)
plt.show()

# Второй график
#     православие — 66 %
#     ислам — 6 %
#     «являюсь верующим, но к какой-либо конкретной конфессии не принадлежу» — 4 %
#     неверующие — 14 %
#     другие - 10
vals = [66, 6, 14, 10, 4]
labels = ["православие", "ислам", "неверующие", "другие", "верующие вне конфессии"]

plt.pie(vals, labels=labels, autopct='%1.1f%%')
plt.title("Конфессиональный состав населения России (ВЦИОМ 2021 год)")
plt.show()

# Третий график
x = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май']
y = [2, 4, 3, 1, 7]

plt.bar(x, y, label='Величина прибыли') #Параметр label позволяет задать название величины для легенды
plt.xlabel('Месяц года')
plt.ylabel('Прибыль, в млн руб.')
plt.title('Пример столбчатой диаграммы')
plt.legend()
plt.show()
