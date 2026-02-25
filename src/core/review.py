from database import db

def compare_answer(question, answer):
  if(question == answer):
    return True
  else:
    return False

def review():
  # falta tratamenro de erro 
  review_qt = int(input("Quantas palavras deseja revisar? (0 - Para revisar tudo)\n"))

  result = db.list_aleatory_questions(review_qt)

  for el in result:
    question = el[0]
    correct_answer = el[1]
    print("---------------------------")
    user_answer = input(f"{question}\n")

    if(compare_answer(correct_answer, user_answer)):
      print("Correto")
    else:
      print(f" Incorreto\n Correto: {correct_answer}\n Sua resposta: {user_answer}")
    print("---------------------------")