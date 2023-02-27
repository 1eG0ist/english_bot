import sqlite3 as sq
import openpyxl
from sql_ import SQLighter
book = openpyxl.open(r"S:\python_projects\EnglishMemory\english_excel_files\5000_7000_English_words_tables.xlsx", read_only=True)

sheet = book.active

db = SQLighter(r"S:\databases\eng_db.db")

for i in range(1, 9872):
    if sheet[i][0].value != None:
        db.insert_eng_words(sheet[i][0].value, sheet[i][1].value, sheet[i][2].value)
