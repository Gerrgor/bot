# import sqlite3 as sq


# class AKCBD:
#     def __init__(self) -> None:
#         self.db = sq.connect("AKC.db")
#         self.cur = self.db.cursor()
#         self.cur.execute(
#             """
#         CREATE TABLE IF NOT EXISTS taken_products(
#                 'id' INTEGER PRIMARY KEY AUTOINCREMENT,
#                 'username' TEXT,
#                 'date_time' TEXT,
#                 'product' TEXT,
#                 'comment' TEXT)"""
#         )
#         self.db.commit()
#         self.cur.execute(
#             """
#         CREATE TABLE IF NOT EXISTS accumulated_products(
#                 'id' INTEGER PRIMARY KEY AUTOINCREMENT,
#                 'username' TEXT,
#                 'date_time' TEXT,
#                 'product' TEXT,
#                 'comment' TEXT)"""
#         )
#         self.db.commit()

#     def taken(self, username, date_time, product, comment):
#         self.cur.execute(
#             """
#         INSERT INTO taken_products(
#                 username,
#                 date_time,
#                 product,
#                 comment)
#                 VALUES (?, ?, ?, ?)""",
#             (username, date_time, product, comment),
#         )
#         self.db.commit()
#     def accumulated(self, username, date_time, product, comment):
#         self.cur.execute(
#             """
#         INSERT INTO accumulated_products(
#                 username,
#                 date_time,
#                 product,
#                 comment)
#                 VALUES (?, ?, ?, ?)""",
#             (username, date_time, product, comment),
#         )
#         self.db.commit()

import psycopg2 as sq


class AKCBD:
    def __init__(self) -> None:
        self.conn = sq.connect(
            dbname="AKC", user="gregor", password="grisha09.03", host='217.18.61.104', port="5432"
        )
        self.cur = self.conn.cursor()
        self.conn.autocommit = True
        self.cur.execute(
            """
        CREATE TABLE IF NOT EXISTS taken_products(
                id SERIAL PRIMARY KEY NOT NULL,
                username TEXT,
                date_time TEXT,
                product TEXT,
                comment TEXT)"""
        )
        self.cur.execute(
            """
        CREATE TABLE IF NOT EXISTS accumulated_products(
                id SERIAL PRIMARY KEY NOT NULL,
                username TEXT,
                date_time TEXT,
                 product TEXT,
                 comment TEXT)"""
        )

    def taken(self, username, date_time, product, comment):
        self.cur.execute(
            """
        INSERT INTO taken_products(
                username,
                date_time,
                product,
                comment)
                VALUES (%s, %s, %s, %s)""",
            (username, date_time, product, comment),
        )

    def accumulated(self, username, date_time, product, comment):
        self.cur.execute(
            """
        INSERT INTO accumulated_products(
                username,
                date_time,
                product,
                comment)
                VALUES (%s, %s, %s, %s)""",
            (username, date_time, product, comment),
        )
