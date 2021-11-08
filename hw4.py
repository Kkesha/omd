import json
import keyword


class AccessByDot(dict):
    """
    Класс наследуется от типа dict и реализует доступ через точку.
    Дополнительно проверяем на ключевые слова, добавляя _.
    """
    def __init__(self, mapping):
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key = key + '_'
            setattr(self, key, value)
        for key in self.__class__.__dict__.keys():
            setattr(self, key, getattr(self, key))

    def __setattr__(self, key, value):
        if isinstance(value, (list, tuple)):
            value = [self.__class__(x)
                     if isinstance(x, dict) else x for x in value]
        elif isinstance(value, dict) and not isinstance(value, self.__class__):
            value = self.__class__(value)
        super(AccessByDot, self).__setattr__(key, value)
        super(AccessByDot, self).__setitem__(key, value)


class ColorizeMixin:
    """Миксин для замены цвета текста при выводе в консоль """
    def __repr__(self, title, price):
        return f'\033[3;{self.repr_color_code};42m{title} | {price}₽'


class Advert(ColorizeMixin, AccessByDot):
    """
    Класс разбирает словарь по ключам.
    Обязательно инициализируем атрибут price
    """
    def __init__(self, mapping):
        if 'price' in mapping:
            if mapping['price'] < 0:
                raise ValueError('price must be >= 0')
            else:
                self.price = 0
        super(Advert, self).__init__(mapping)

    def __repr__(self):
        self.repr_color_code = 33
        out_price = self['price']
        out_title = self['title']
        return ColorizeMixin.__repr__(self, out_title, out_price)


if __name__ == '__main__':
    test1 = '''{
            "title": "iPhone X",
            "price": 100,
            "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"]
            }
            }'''
    dict1 = json.loads(test1)
    advert1 = Advert(dict1)
    print('Вывод теста 1:')
    print(advert1.title)
    print(advert1.price)
    print(advert1.location.address)

    test2 = '''{
        "title":"Вельш-корги",
        "price":1000,
        "class":"dogs",
        "location": {
            "address":"сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }}'''

    dict2 = json.loads(test2)
    advert2 = Advert(dict2)

    print('\nВывод теста 2:')
    print(advert2.title)
    print(advert2.location.address)
    print(advert2.class_)

    print('\nПроверка миксина:')
    print(advert2)
