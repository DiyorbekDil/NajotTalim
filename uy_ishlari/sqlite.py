# from urllib.request import urlretrieve
# import sqlite3 as sql
# # import shutil
# # url = "https://github.com/lerocha/chinook-database/tree/85eca67d22ae15b2767851cc45abc7f8764c517f/ChinookDatabase"
# # urlretrieve(url, "chinook.db") # faylni yuklab olish
# # # shutil.unpack_archive("chinook.zip") # zip faylni ochish
# db = sql.connect("chinook.db")
# cursor = db.cursor()
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(cursor.fetchall())
from urllib.request import urlretrieve
import sqlite3 as sql

url = "https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite"
urlretrieve(url, "chinook.db")  # Download the file

db = sql.connect("chinook.db")  # Connect to the database
cursor = db.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())