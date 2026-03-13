from services import db

def create_question():
  question = input("Qual a pergunta?\n")
  answer = input("Qual a resposta?\n")
  db.create_question(question, answer)