import utils.anki_connection as con
import re
from services import db

question_fields = 'palavra'
answer_fields = 'traducao'

class AnkiImport:
  def __init__(self):
    pass

  
  def create_import(self, deck_to_import):
    """
    Cria a importacao dos cards do anki

    Args:
      deck_to_import: Nome do deck vindo do banco de dados do ANKI
    """

    ankiconnect = con.check_connection()

    if(ankiconnect):
      cards_ids = con.get_cards_id(deck_to_import)
      cards = con.get_cards(cards_ids)
      cards_clean = []

      for card in cards:
        fields = card.get('fields', {})

        if(fields.get(question_fields, {}).get('value') and fields.get(answer_fields, {}).get('value')):
          cards_clean.append([fields.get(question_fields, {}).get('value'), fields.get(answer_fields, {}).get('value')])

        for card in cards_clean:
          for i, el in enumerate(card):
            card[i] = re.sub('<.*?>', '', el) 

      self._save_to_db(deck_to_import, cards_clean)

  def list_decks(self):
    """
      Lista os decks no bancos de dados do ANKI

      Returns:
        list: Lista com todos os decks registrado no ANKI
    """

    ankiconnect = con.check_connection()

    deck_names = []

    if(ankiconnect):
      deck_names = con.get_decks_name()
      return deck_names

  def update_deck_with_ankis(self, deck_to_update):
    """
      Realiza a atualizacao de um deck importado anteriormente com a versao atual banco de dados do ANKI

      Args:
      deck_to_update: Nome do deck vindo do banco de dados do ANKI
    """

    ankiconnect = con.check_connection()

    if(ankiconnect):
      cards_clean = []
      deck_names = []
      decks = db.list_decks()
      for deck in decks:
        deck_names.append(deck[1])

      for deck_name in deck_names:
        cards_ids = con.get_cards_id(deck_name)

        cards = con.get_cards(cards_ids)

        
        
        for card in cards_clean:
          db.update_or_create_question(card[0], card[1], deck_name)

  def _save_to_db(deck_name, cards):
    decks = db.list_decks()
    decks_name = []

    for deck in decks:
      decks_name.append(deck[1])

    if(deck_name not in decks_name):
      db.create_deck(deck_name)
    else:
      print("Deck criado anteriormente")

    for card in cards:
      db.create_question(card[0], card[1], deck_name)

  def _clean_cards(cards_list):
    cards_clean = []
    for card in cards_list:
      fields = card.get('fields', {})

      if(fields.get(question_fields, {}).get('value') and fields.get(answer_fields, {}).get('value')):
        cards_clean.append([fields.get(question_fields, {}).get('value'), fields.get(answer_fields, {}).get('value')])

      for card in cards_clean:
        for i, el in enumerate(card):
          card[i] = re.sub('<.*?>', '', el) 
    return cards_clean