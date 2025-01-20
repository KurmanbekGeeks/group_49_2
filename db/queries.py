# queries.py

CREATE_TABLE_registered = """
    CREATE TABLE IF NOT EXISTS registered (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT,
    age TEXT,
    email TEXT,
    city TEXT,
    photo TEXT
    )
"""

INSERT_registered_query = """
    INSERT INTO registered (fullname, age, email, city, photo)
    VALUES (?, ?, ?, ?, ?)
"""



CREATE_TABLE_store = """
    CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product TEXT,
    size TEXT,
    price TEXT,
    photo TEXT,
    product_id TEXT
    )
"""

INSERT_store_query = """
    INSERT INTO store (name_product, size, price, photo, product_id)
    VALUES (?, ?, ?, ?, ?)
"""


CREATE_TABLE_store_detail = """
    CREATE TABLE IF NOT EXISTS store_detail (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT,
    category TEXT,
    info_product TEXT
    )
"""

INSERT_store_detail_query = """
    INSERT INTO store_detail (product_id, category, info_product)
    VALUES (?, ?, ?)
"""