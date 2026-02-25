import sqlite3, os
from dotenv import load_dotenv

load_dotenv()

def init():
  db_name = os.getenv("DB_NAME")
  try:
    connection = sqlite3.connect(f"data/{db_name}")
    connection.execute('''
    CREATE TABLE IF NOT EXISTS decks (
                      id INTEGER PRIMARY KEY,
                      name TEXT NOT NULL UNIQUE
                      )
    ''')
    connection.commit()
    print("Banco de Dados Conectado")
  except:
    print("Erro ao Conectar Banco de Dados")
  finally:
    connection.close()

def command(sql_command, values = None):
  db_name = os.getenv("DB_NAME")
  try:
    connection = sqlite3.connect(f"data/{db_name}")
    cursor = connection.cursor()
    if (values != None):
      cursor.execute(sql_command, values)
    else:
      cursor.execute(sql_command)
    result = cursor.fetchall()
    connection.commit()
    return result
  except:
    print("Erro ao Conectar Banco de Dados")
  finally:
    connection.close()

def create_deck(deck_name):
  # possivel sql injection, verificar
  sql = f'''CREATE TABLE IF NOT EXISTS "{deck_name}" ( id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT NOT NULL UNIQUE, answer TEXT NOT NULL);'''
  command(sql)

  # registra na tabela de decks criados
  sql = "INSERT INTO decks (name) VALUES (?)"
  values = (deck_name, )
  command(sql, values)

def list_decks():
  sql = "SELECT id, name FROM decks;"
  result = command(sql)
  return result

def create_question(question, answer, deck):
  sql = f'''INSERT INTO "{deck}" (question, answer) VALUES (?, ?);'''
  values = (question, answer)
  command(sql, values)

def get_question(id, deck):
  sql = "SELECT id, question, answer FROM ? WHERE id = ?;"
  values = (id, deck)
  result = command(sql, values)
  return result

def list_questions(deck):
  sql = "SELECT id, question, answer FROM ?;"
  values = (deck, )
  result = command(sql, values)
  return result

def edit_question(id, question, answer, deck):
  sql = f'''UPDATE "{deck}" SET question = ?, answer = ? WHERE id = ?;'''
  values = (question, answer, id)
  command(sql, values)

def delete_question(id, deck):
  sql = f'''DELETE FROM "{deck}" WHERE id = ?;'''
  values = (id)
  command(sql, values)

def list_aleatory_questions(num_of_question, deck):
  result = None
  if(num_of_question > 0):
    sql = f'''SELECT question, answer FROM "{deck}" ORDER BY RANDOM() LIMIT ?;'''
    values = (num_of_question, )
    result = command(sql, values)
  else:
    sql = f'''SELECT question, answer FROM "{deck}" ORDER BY RANDOM();'''
    result = command(sql)
  return result