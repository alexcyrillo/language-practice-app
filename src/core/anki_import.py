import core.anki_connection as con
import re
from database import db
from core.select_from_list import select_from_list

question_fields = 'palavra'
answer_fields = 'traducao'

def import_from_anki():
  ankiconnect = con.check_connection()

  if(ankiconnect):
    cards_clean = []
    deck_names = con.get_decks_name()
    deck_index = select_from_list(deck_names, "Escolha qual deck deseja importar")
    selected_deck = deck_names[deck_index]
    cards_ids = con.get_cards_id(deck_names[deck_index])

    cards = con.get_cards(cards_ids)

    for card in cards:
      fields = card.get('fields', {})

      if(fields.get(question_fields, {}).get('value') and fields.get(answer_fields, {}).get('value')):
        cards_clean.append([fields.get(question_fields, {}).get('value'), fields.get(answer_fields, {}).get('value')])

      for card in cards_clean:
        for i, el in enumerate(card):
          card[i] = re.sub('<.*?>', '', el) 

    save_to_db(selected_deck, cards_clean)
  else:
    print("Garanta que o Anki esta aberto e com o addon AnkiConnect instalado")

def save_to_db(deck_name, cards):
  decks = db.list_decks()
  decks_name = []

  for deck in decks:
    decks_name.append(deck[1])

  if(deck_name not in decks_name):
    db.create_deck(deck_name)
  else:
    print("Deck registrado anteriormente")

  for card in cards:
    db.create_question(card[0], card[1], deck_name)

