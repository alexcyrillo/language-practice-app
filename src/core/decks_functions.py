from database import db
from core.select_from_list import select_from_list

def create_deck():
  deck_name = input("Escolha um nome para o Deck: ")
  if(deck_name != None):
    db.create_deck(deck_name)

def deck_selection():
  decks_list = db.list_decks()
  deck_names = []
  for deck in decks_list:
    deck_names.append(deck[1])

  if deck_names == []:
    return "Nenhum deck criado"

  print("\n---SELECAO DE DECK---")
  deck_index = select_from_list(deck_names, "Selecione um Deck")
  print("--------------------")

  return decks_list[deck_index][1]

def delete_deck(deck_name):
  validation = input(f"Realmente deseja excluir o deck {deck_name}? (s/n) ")
  if(validation.lower() == "s"):
    db.delete_deck(deck_name)
    print(f"Deck {deck_name} excluido")