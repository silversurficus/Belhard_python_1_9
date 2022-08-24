"""
Реализация Haversine formula для Python.
https://en.wikipedia.org/wiki/Haversine_formula

Написать функцию distance, которая будет возвращать расстояние между
точками GPS на карте в метрах.

Функция должна принимать следующие аргументы:
* a_lat - широта первой точки
* a_lon - долгота первой точки
* b_lat - широта второй точки
* b_lon - долгота второй точки

Алгоритм:
1. Посчитать значение каждой координаты в радианах.
Формула: float(value) * pi / 180
2. Вычислить sin и cos радианов широт из п1.
3. Вычислить разницу (delta) радианов долгот из п1.
4. Вычислить sin и cos разницы долгот из п3.
5. Вычислить y = sqrt(pow(b_lat_cos * delta_sin, 2)) + pow(a_lat_cos * b_lat_sin - a_lat_sin * b_lat_cos * delta_cos, 2))
6. Вычислить x = a_lat_sin * b_lat_sin + a_lat_cos * b_lat_cos * delta_cos
7. Вычислить ad = atan2(y, x)
8. Вернуть ad * EARTH_R
"""
import math
EARTH_R = 6372795
def distance(a_lat, a_lon, b_lat, b_lon):
    a_lat = float(a_lat) * math.pi / 180
    b_lat = float(b_lat) * math.pi / 180
    a_lon = float(a_lon) * math.pi / 180
    b_lon = float(b_lon) * math.pi / 180
    a_lat_sin = math.sin(a_lat)
    b_lat_sin = math.sin(b_lat)
    a_lat_cos = math.cos(a_lat)
    b_lat_cos = math.cos(b_lat)
    delta_lon = a_lon - b_lon
    delta_cos = math.cos(delta_lon)
    delta_sin = math.sin(delta_lon)
    y = math.sqrt((math.pow(b_lat_cos * delta_sin, 2)) + math.pow(a_lat_cos * b_lat_sin - a_lat_sin * b_lat_cos * delta_cos, 2))
    x = a_lat_sin * b_lat_sin + a_lat_cos * b_lat_cos * delta_cos
    ad = math.atan2(y, x)
    return ad * EARTH_R