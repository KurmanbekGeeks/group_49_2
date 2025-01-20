# main_db.py
import sqlite3
from db import queries

# db = sqlite3.connect('db/registered.sqlite3')
db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()

async def create_db():
    if db:
        print('База данных подключена')
    # cursor.execute(queries.CREATE_TABLE_registered)
    cursor.execute(queries.CREATE_TABLE_store)
    cursor.execute(queries.CREATE_TABLE_store_detail)

async def sql_insert_registered(fullname, age, email, city, photo):
    cursor.execute(queries.INSERT_registered_query, (
        fullname, age, email, city, photo
    ))
    db.commit()


async def sql_insert_store(name_product, size, price, photo, product_id):
    cursor.execute(queries.INSERT_store_query, (
        name_product, size, price, photo, product_id
    ))
    db.commit()


async def sql_insert_detail(product_id, category, info_product):
    cursor.execute(queries.INSERT_store_detail_query, (
        product_id, category, info_product
    ))
    db.commit()