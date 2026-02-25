import sqlite3, os
from dotenv import load_dotenv

load_dotenv()

def init():
  db_name = os.getenv("DB_NAME")
  connection = sqlite3.connect(f"data/{db_name}")

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

def command(sql_command, values = None):
  db_name = os.getenv("DB_NAME")
  connection = sqlite3.connect(f"data/{db_name}")
  cursor = connection.cursor()
  if (values != None):
    cursor.execute(sql_command, values)
  else:
    cursor.execute(sql_command)
  result = cursor.fetchall()
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

def edit_question(id, question, answer):
  sql = "UPDATE question_tb SET question = ?, answer = ? WHERE id = ?;"
  values = (question, answer, id)
  command(sql, values)

def delete_question(id):
  sql = "DELETE FROM question_tb WHERE id = ?;"
  values = (id, )
  command(sql, values)

def list_aleatory_questions(num_of_question):
  result = None
  if(num_of_question > 0):
    sql = "SELECT question, answer FROM question_tb ORDER BY RANDOM() LIMIT ?;"
    values = (num_of_question, )
    result = command(sql, values)
  else:
    sql = "SELECT question, answer FROM question_tb ORDER BY RANDOM();"
    result = command(sql)
  return result