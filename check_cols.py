import sqlite3
db_path = 'db.sqlite3'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("PRAGMA table_info(main_app_studentguardian)")
columns = cursor.fetchall()
for col in columns:
    print(col)
conn.close()
