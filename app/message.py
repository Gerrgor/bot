import psycopg2 as sq


class AKCBD:
    def __init__(self) -> None:
        self.conn = sq.connect(
            dbname="postgres", user="postgres", password="grisha09.03", host="localhost"
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
        self.conn.autocommit = True
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
        self.conn.autocommit = True
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
