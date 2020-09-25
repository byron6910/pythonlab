# -*- coding: utf-8 -*-

countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

while True:
    country=str(input('Escribe el nombre del pais:')).lower()
    try:
        print('La poblacion del pais {} es: {} millones'.format(country,countries[country]))

    except KeyError:
        print('No hemos tenido respuesta del pais {}'.format(country))
