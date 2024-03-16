import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

table_info = """
create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);

"""

cursor.execute(table_info)

cursor.execute('''Insert into STUDENT values("Amarnath", "R&D", "B", 80);''')
cursor.execute('''Insert into STUDENT values("Arpit", "software development", "A", 100);''')
cursor.execute('''Insert into STUDENT values("Poobalan", "testing", "B", 40);''')
cursor.execute('''Insert into STUDENT values("Arpit", "deployment", "A", 100);''')

data = cursor.execute("select * from STUDENT")

for row in data:
    print(row)

connection.commit()
connection.close()