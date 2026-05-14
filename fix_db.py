import sqlite3
import datetime

db_path = 'db.sqlite3'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Check if 0003 is already there
cursor.execute("SELECT id FROM django_migrations WHERE app='main_app' AND name='0003_alter_customuser_user_type_registrar_guardian_and_more'")
row = cursor.fetchone()

if not row:
    print("Inserting 0003 into django_migrations...")
    cursor.execute(
        "INSERT INTO django_migrations (app, name, applied) VALUES (?, ?, ?)",
        ('main_app', '0003_alter_customuser_user_type_registrar_guardian_and_more', datetime.datetime.now())
    )
    conn.commit()
    print("Done.")
else:
    print("0003 already exists in django_migrations.")

conn.close()
