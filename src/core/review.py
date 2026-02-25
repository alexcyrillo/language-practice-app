from database import db
from core.select_from_list import select_from_list
import re

def review(deck_name):
  decks = db.list_decks()
  correct_count = 0
  incorrect_count = 0

  review_qt = int(input("Quantas palavras deseja revisar? (0 - Para revisar tudo)\n"))

  cards = db.list_aleatory_questions(review_qt, deck_name)

  for card in cards:
    question = card[0]
    correct_answer = card[1]
    print("---------------------------")
    user_answer = input(f"{question}\n")

    correct_answer_splited = correct_answer.split(";")
    for i, el in enumerate(correct_answer_splited):
      clean_el = re.sub(r'\(.*?\)', '', el)
      correct_answer_splited[i] = clean_el.strip().lower()

    if user_answer in correct_answer_splited:
      print(f"Correto!\n{correct_answer}")
      correct_count += 1
    else:
      print(f" Incorreto\n Correto: {correct_answer}\n Sua resposta: {user_answer}")
      incorrect_count += 1
    print("---------------------------")
  
    keep = input("Pressione qualquer botao para continuar; q para sair")
    if(keep == "q"):
      break

  print(f"\n-----Pontuação Final-----\nCorretas: {correct_count}\nIncorretas: {incorrect_count}\n-------------------------")
      