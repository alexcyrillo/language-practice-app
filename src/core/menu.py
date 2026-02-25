from core.review import review
from core.create_question import create_question
from core.anki_import import import_from_anki
from core.select_from_list import select_from_list
from database import db

def main_menu(selected_deck = None):
  options = ["Estudar", "Decks", "Importar Deck do AnkiConnect", "Mudar Deck", "Sair"]
  
  if(selected_deck == None):
    selected_deck = deck_selection()

  print("\n---MENU PRINCIPAL---")
  print(f"Deck Selecionado: {selected_deck}")
  selected_option = select_from_list(options)
  print("--------------------")

  match selected_option:
    case 0:
      review(selected_deck)
    case 1:
      deck_menu(selected_deck)
    case 2:
      anki_import_menu(selected_deck)
    case 3:
      selected_deck = None
      main_menu(selected_deck)
    case 4:
      exit()
    case _:
      print ("Opcao Invalida")

def deck_menu(selected_deck):
  options = ["Listar Cards", "Editar Card", "Mudar Deck Selecionado", "Apagar Deck", "Voltar"]

  print("\n---OPCOES DO DECK---")
  print(f"Deck Selecionado: {selected_deck}")
  selected_option = select_from_list(options)
  print("--------------------")

  match selected_option:
    case 0:
      print ("Implementar")
    case 1:
      print ("Implementar")
    case 2:
      deck_menu()
    case 3:
      print ("Implementar")
    case 4:
      main_menu()
    case _:
      print ("Opcao Invalida")

def anki_import_menu(selected_deck):
  options = ["Importar Novo", "Atualizar Decks", "Voltar"]

  print("\n--IMPORTAR DO ANKI--")
  print(f"Deck Selecionado: {selected_deck}")
  selected_option = select_from_list(options)
  print("--------------------")

  match selected_option:
    case 0:
      import_from_anki()
    case 1:
      print ("Implementar")
    case 2:
      main_menu()
    case _:
      print ("Opcao Invalida")


def deck_selection():
  decks_list = db.list_decks()
  print("\n---SELECAO DE DECK---")
  deck_index = select_from_list(decks_list, "Selecione um Deck")
  print("--------------------")

  return decks_list[deck_index][1]