"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import csv

file_1 = "north_data/customers_data.csv"
file_2 = "north_data/employees_data.csv"
file_3 = "north_data/orders_data.csv"


def read_customers():
    """Считывает данные из customers_data.csv"""
    dic = []
    with open(file_1, 'r', encoding='utf-8') as file:
        file_read = csv.reader(file, delimiter=',')
        for line in file_read:
            dic.append(line)

    return dic


def read_employees_data():
    """Считывает данные из employees_data.csv"""
    dic = []
    with open(file_2, 'r', encoding='utf-8') as file:
        file_read = csv.reader(file, delimiter=',')
        for line in file_read:
            dic.append(line)

    return dic


def read_orders_data():
    """Считывает данные из orders_data.csv"""
    dic = []
    with open(file_3, 'r', encoding='utf-8') as file:
        file_read = csv.reader(file, delimiter=',')
        for line in file_read:
            dic.append(line)

    return dic


def main():
    """Заполнит созданные таблицы данными"""

    conn = psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password="Zima-2023"
    )

    data = read_customers()
    with conn:
        cursor = conn.cursor()
        for item in data[1:]:
            cursor.execute(f"INSERT INTO customers_data (customer_id, company_name, contact_name)"
                           f" VALUES ('{item[1]}', '{item[2]}', '{item[3]}')")

    data_2 = read_employees_data()
    with conn:
        cursor = conn.cursor()
        for item in data_2[1:]:
            cursor.execute(f"INSERT INTO customers_data (first_name, last_name, title, birth_date, notes)"
                           f" VALUES ('{item[1]}', '{item[2]}', '{item[3]}','{item[4]}', '{item[5]}')")

    data_3 = read_orders_data()
    with conn:
        cursor = conn.cursor()
        for item in data_3[1:]:
            cursor.execute(f"INSERT INTO customers_data (order_id, customer_id, employee_id, order_date,ship_city)"
                           f" VALUES ('{item[1]}', '{item[2]}', '{item[3]}','{item[4]}', '{item[5]}')")


if __name__ == 'main':
    main()
