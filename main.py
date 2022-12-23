import random
import json
from faker import Faker
from Conf import MODEL

faker_= Faker("ru_RU")
BOOKS = "books.txt"

def title() -> str:
    # Функция возвращает случайную строку с названием книги из файла books.txt

    with open(BOOKS, "r", encoding="utf-8") as f:
        line = f.readlines()
    # print(random.choice(line))
    return random.choice(line)

def year() -> int:

    # Функция возвращает случайное число - год, для переменной year из заданного диапазона

    year = random.randint(1868, 1932)
    return year
    # print(year)

def pages() -> int:

    # Функция возвращает значение для переменной pages - случайное число

    pages = random.randint(10, 700)
    # print(pages)
    return pages


def isbn13() -> str:

    # Функция возвращает случайный книжный номер типа: "978-1-60487-647-5"

    a = faker_.isbn13()
    # print(a)
    return a


def rating() -> float:

    # Функция возвращает случайное дробное число для переменной rating из диапазона

    rating = random.uniform(0.0, 5.0)
    rating = round(rating, 1)
    # print(rating)
    return rating


def price() -> float:

    # Функция возвращает случайное дробное число из диапазона для переменной price

    price = random.uniform(150.0, 4500.0)
    price = round(price, 1)
    # print(price)
    return price


def author() -> list:

    # Функция возвращает список авторов для переменной author

    list_ = []
    for i in range(1, 150):
        list_.append(faker_.name())
    b = random.randint(1, 3)
    authors = random.sample(list_, b)
    # print(authors)
    return authors


def generator (count =1):

    # Функция генератор, формирует список словарей из XXX книг
    """"
    :param count: счетчик со значением 1 по умолчанию

    """
    counter = count
    while True:
        dict_ = {
            "model": MODEL,
            "pk": counter,
            "fields":
                {
                    "title": title(),
                    "year": year(),
                    "pages": pages(),
                    "isbn13": isbn13(),
                    "rating": rating(),
                    "price": price(),
                    "author": author()
                }

            }
        yield dict_
        counter += 1


def json_(spisok: list):
    # Функция преобразовывает список словарей в строку формата json и записывает их в файл
    """
    :param spisok: список словарей

    """
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump(spisok, f, indent=4, ensure_ascii=False)


if __name__=="__main__":
    # Формируем список словарей из ХХХ книг и записываем его файл формата json

    gnr = generator(4)
    spisk = [next(gnr) for i in range(150)]

    json_(spisk)



