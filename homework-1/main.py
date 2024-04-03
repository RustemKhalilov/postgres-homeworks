"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5434",
    database="north",
    user="postgres",
    password="triedinstvo"
)

cur = conn.cursor()
postgres_insert_query = """ INSERT INTO employees (ID, FirstName, LastName, Email, age, phonework, phonecell, homeaddress, education, salary, drivers_license, car, presence_of_diseases, medical_policy)
                                       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
# Список сотрудников
record_to_insert = [
    (1,
     'Гаврилов',
     'Никита',
     'GavrilovNikita@opg_msk.ru',
     45,
     '+7-934-521-23-48',
     '+7-934-521-23-48',
     'г. Екатеринбург, Ленина 23 кв. 121',
     'Генеральный директор',
     120000,
     'BY234-543-234',
     'land cruiser 200',
     'нет',
     '125-459-788YSP'),

    (2,
     'Борисов',
     'Егор',
     'BorosivEgor@opg_msk.ru',
     40,
     '+7-934-521-35-12',
     '+7-934-521-35-12',
     'г. Екатеринбург,Ленина 12 кв. 21',
     'Заместитель директора',
     100000,
     'BY234-105-202',
     'nfiniti qx80',
     'нет',
     '125-459-265YSP'),

    (3,
     'Шильд',
     'Татьяна',
     'ShildTatyana@opg_msk.ru',
     45,
     '+7-934-521-41-32',
     '+7-934-521-41-33',
     'г. Екатеринбург, Максима Горького 7 кв. 8',
     'Главный бухгалтер',
     900000,
     'BY234-103-305',
     'nfiniti qx80',
     'бронхит',
     '125-707-265YSP'),
]
# Заполняем таблицу
for item in record_to_insert:
    cur.execute(postgres_insert_query, item)

postgres_insert_query = """ INSERT INTO clients (ID, FirstName, LastName, Email,  phone, home_address, number_order_history_delivery, bonus_point)
                                       VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
# Список клиентов
record_to_insert = [
    (1,
     'Снегирев',
     'Виталий',
     'Snegirev@mail.ru',
     '+7-925-522-13-41',
     'г. Екатеринбург, Вокзальная 12 кв. 5',
     '105-19, 243-20, 1335-21',
     705),

    (2,
     'Раджабов',
     'Ислам',
     '-',
     '-',
     'г. Нижний Тагил, Северная 11 кв. 3',
     '101-19, 2432-21, 2335-22',
     606),

    (3,
     'Корзун',
     'Олег',
     'OLegKorzun@yandex.ru',
     '+7-923-522-78-99',
     'г. Камышлов, Береговая 5',
     '65-19, 1243-21, 4335-22',
     1025),
]
# Заполняем таблицу клиентов
for item in record_to_insert:
    cur.execute(postgres_insert_query, item)


postgres_insert_query = """ INSERT INTO orders (ID, order_number, order_time, addrees,  Email, order_composition, receipt_number, payment_method)
                                       VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""


# Список заказов
record_to_insert = [
    (1,
     '1-18',
     '13:40',
     'г. Екатеринбург, Лесная 15',
     '-',
     'Набор для рыбалки, блесна 23, фонарик',
     '342258966',
     'онлайн'),

    (2,
     '2-18',
     '15:10',
     'г. Екатеринбург, Минская 23',
     '-',
     'Телевизор Toshiba 43',
     '342258967',
     'наличные'),

    (3,
     '3-18',
     '18:10',
     '-',
     '-',
     'Телевизор DEXP 43',
     '342258968',
     'наличные'),
]
# Заполняем таблицу клиентов
for item in record_to_insert:
    cur.execute(postgres_insert_query, item)


# Закоминтили чтобы записать в базу
conn.commit()
# Закрыли курсор
cur.close()
# Закрыли соединение с БД
conn.close()
