#     Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers,
#     которая возвращает количество лошидиных сил для автомобиля
#     Создайте наследника класса Car - класс Nissan и переопределите свойство price,
#     а также переопределите функцию horse_powers
#     Дополнительно создайте класс Kia, который также будет наследником класса Car
#     и переопределите также свойство price, а также переопределите функцию horse_powers

class Car:
    price = 1000000

    def horse_powers(self):
        return 10


class Nissan (Car):

    def horse_powers(self):
        return 200


class Kia (Car):

    def horse_powers(self):
        return 150


nissan = Nissan()
nissan.price = 500000
kia = Kia()
kia.price = 800000
