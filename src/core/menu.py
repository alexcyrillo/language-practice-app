from core.review import review
from core.decks_functions import create_deck, deck_selection, delete_deck
from core.anki_import import import_from_anki, update_deck_with_ankis
from core.select_from_list import select_from_list
from database import db

def main_menu(selected_deck = None):
  if(selected_deck == None):
    selected_deck = deck_selection()

  if(selected_deck == "Nenhum deck criado"):
    options = ["Criar Deck", "Importar Deck do AnkiConnect", "Sair"]

    print("\n---MENU PRINCIPAL---")
    print(f"Deck Selecionado: {selected_deck}")
    selected_option = select_from_list(options)
    print("--------------------")

    match selected_option:
      case 0:
        create_deck()
      case 1:
        import_from_anki()
      case _:
        print ("Opcao Invalida")
  else:
    options = ["Estudar", "Decks", "Importar Deck do AnkiConnect", "Mudar Deck", "Sair"]

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
        main_menu()
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
      delete_deck(selected_deck)
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
      update_deck_with_ankis()
    case 2:
      main_menu()
    case _:
      print ("Opcao Invalida")
