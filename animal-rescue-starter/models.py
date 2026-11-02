import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "rescue.db"


def query(sql, values=()):
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    rows = connection.execute(sql, values).fetchall()
    connection.close()
    return rows


def get_dogs():
    rows = query ("SELECT * FROM dogs ORDER BY name")
    return rows


def get_cats():
    rows = query("SELECT * FROM cats ORDER BY name")
    return rows