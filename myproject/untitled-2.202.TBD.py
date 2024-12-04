import sqlite3 as s

connection = s.connect ('database.db')
cursor = connection.cursor ()

cursor.execute ('''
CREATE TABLE IF NOT EXISTS TEXTtest(
id INTEGER PRIMARY KEY,
Profession TEXT NOT NULL,
Skills TEXT NOT NULL,
Description TEXT NOT NULL,
Test TEXT NOT NULL,
complete_test TEXT DEFAULT 'Not Complete',
test_result TEXT DEFAULT 'Not Complete'
)
''')

cursor.execute ('''
CREATE TABLE IF NOT EXISTS MTest(
id INTEGER PRIMARY KEY,
Category TEXT NOT NULL,
Question TEXT NOT NULL,
Answer TEXT NOT NULL,
FOREIGN KEY (Question) REFERENCES TEXTtest(Test) ON DELETE SET NULL
)
''')

def add_CQA (Category, Question, Answer):
    cursor.execute('INSERT INTO MTest (Category, Question, Answer) VALUES (?, ?, ?)', (Category, Question, Answer))
    connection.commit

def add_information(Profession, Skills, Description, Test):
    cursor.execute('''
        INSERT INTO TEXTtest (Profession, Skills, Description, Test) 
        VALUES (?, ?, ?, ?)
    ''', (Profession, Skills, Description, Test))
    connection.commit()
    
def update_test_complete(test_id, status):
    cursor.execute ('UPDATE TEXTtest SET status = ? WHERE id = ?' , (status, test_id))
    connection.commit ()
    
def update_text_result(test_id, status):
    cursor.execute ('UPDATE TEXTtest SET status = ? WHERE id = ?' , (status, test_id))
    connection.commit ()

def list_TEXT():
    cursor.execute ('SELECT * FROM TEXTtest')
    TEXTtest = cursor.fetchall ()
    for Test in TEXTtest:
        print (Test)


connection.commit ()
connection.close ()