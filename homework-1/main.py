"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv
import os.path


def csv_reader(path1, file_name):
    fileID = os.path.join(path1, file_name)  # Считываем файл с диска
    with open(fileID, encoding='utf-8') as r_file:
        # Создаем объект reader, указываем символ-разделитель ","
        file_reader = csv.reader(r_file, delimiter=",", quotechar=',')
        csv_list = []
        # Считывание данных из CSV файла
        for row in file_reader:
            csv_list.append(row)
    #Получаем список из файла
    return csv_list


conn = psycopg2.connect(
    host="localhost",
    port="5434",
    database="north",
    user="postgres",
    password="triedinstvo"
)

path1 = "north_data"
file_name = "customers_data.csv"

customers_data = csv_reader(path1, file_name)

file_name = "employees_data.csv"
employees_data = csv_reader(path1, file_name)

file_name = "orders_data.csv"
orders_data = csv_reader(path1, file_name)

cur = conn.cursor()
postgres_insert_query = """ INSERT INTO employees (employee_id, first_name, last_name, birth_date, title, notes)
                                       VALUES (%s,%s,%s,%s,%s,%s)"""

# Заполняем таблицу
for index, item in enumerate(employees_data):
    if index > 0:
       row_to_table=[]
       if len(item) == 6:
          row_to_table = item
          cur.execute(postgres_insert_query, row_to_table)
       elif len(item) > 6:
          temp_row = ''
          for index2, item2 in enumerate(item):
              if index2 >= 6:
                 temp_row += item2
          row_to_table=[item[0], item[1], item[2], item[3], item[4], temp_row]
          cur.execute(postgres_insert_query, row_to_table)


postgres_insert_query = """ INSERT INTO customers (customer_id, company_name, contact_name)
                                       VALUES (%s,%s,%s)"""


for index, item in enumerate(customers_data):
    if index > 0:
       cur.execute(postgres_insert_query, item)

postgres_insert_query = """ INSERT INTO orders (order_id, customer_id, employee_id, order_date,  ship_city)
                                       VALUES (%s,%s,%s,%s,%s)"""


for index, item in enumerate(orders_data):
    if index > 0:
       cur.execute(postgres_insert_query, item)

# Закоминтили чтобы записать в базу
conn.commit()
# Закрыли курсор
cur.close()
# Закрыли соединение с БД
conn.close()
