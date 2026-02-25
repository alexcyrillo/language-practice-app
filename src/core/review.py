from src.database import db

def compare_answer(question, answer):
  if(question == answer):
    return True
  else:
    return False

def review():
  result = db.get_question(1)

  question = result[1]
  correct_answer = result[2]

  user_answer = input(f"{question}\n")

  if(compare_answer(correct_answer, user_answer)):
    print("Correto")
  else:
    print(f" Incorreto\n Correto: {correct_answer}\n Sua resposta: {user_answer}")