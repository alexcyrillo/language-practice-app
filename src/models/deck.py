from services import db

class Deck:
  def __init__(self):
    self.deck_list = None
    self.current_name = None

  def _list_decks(self):
    deck_list = db.list_decks()
    deck_list_names = []
    for (id, name) in deck_list:
      deck_list_names.append(name)

    return deck_list_names

  def create_deck(self, deck_name):
    self.deck_list = self._list_decks()

    if(deck_name != None and deck_name not in self.deck_list):
      db.create_deck(deck_name)

  def delete_deck(self):
    db.delete_deck(self.current_name)

  def set_deck(self, new_deck):
    self.current_name = new_deck

  def get_deck_list(self):
    self.deck_list = self._list_decks()
    return self.deck_list
