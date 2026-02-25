import sqlite3, os
from dotenv import load_dotenv

load_dotenv()

def init():
  connection = sqlite3.connect(f"data/{os.getenv("DB_NAME")}")

  connection.execute('''
  CREATE TABLE IF NOT EXISTS question_tb (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     question TEXT NOT NULL UNIQUE,
                     answer TEXT NOT NULL,
                     creation_date DATETIME DEFAULT CURRENT_TIMESTAMP
                     )
  ''')

  connection.commit()
  connection.close()


def command(sql_command, values):
  connection = sqlite3.connect(os.getenv("DB_NAME"))
  cursor = connection.cursor()
  cursor.execute(sql_command, values)
  result = cursor.fetchone()
  connection.commit()
  connection.close()
  return result

def create_question(question, answer):
  sql = "INSERT INTO question_tb (question, answer) VALUES (?, ?);"
  values = (question, answer)
  command(sql, values)

def get_question(id):
  sql = "SELECT id, question, answer FROM question_tb WHERE id = ?;"
  values = (id, )
  result = command(sql, values)
  return result

def list_questions():
  sql = "SELECT id, question, answer FROM question_tb;"
  result = command(sql)
  return result