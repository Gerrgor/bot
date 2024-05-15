import sqlite3 as sq


class AKCBD:
    def __init__(self) -> None:
        self.db = sq.connect("AKC.db")
        self.cur = self.db.cursor()
        self.cur.execute(
            """
        CREATE TABLE IF NOT EXISTS taken_products(
                'id' INTEGER PRIMARY KEY AUTOINCREMENT,
                'username' TEXT,
                'date_time' TEXT,
                'product' TEXT,
                'comment' TEXT)"""
        )
        self.db.commit()
        self.cur.execute(
            """
        CREATE TABLE IF NOT EXISTS accumulated_products(
                'id' INTEGER PRIMARY KEY AUTOINCREMENT,
                'username' TEXT,
                'date_time' TEXT,
                'product' TEXT,
                'comment' TEXT)"""
        )
        self.db.commit()

    def taken(self, username, date_time, product, comment):
        self.cur.execute(
            """
        INSERT INTO taken_products(
                username,
                date_time,
                product,
                comment)
                VALUES (?, ?, ?, ?)""",
            (username, date_time, product, comment),
        )
        self.db.commit()
    def accumulated(self, username, date_time, product, comment):
        self.cur.execute(
            """
        INSERT INTO accumulated_products(
                username,
                date_time,
                product,
                comment)
                VALUES (?, ?, ?, ?)""",
            (username, date_time, product, comment),
        )
        self.db.commit()