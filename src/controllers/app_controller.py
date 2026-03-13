from models.anki_import import AnkiImport
from utils.clean_frame import clean_frame
from views.main_menu_view import MainMenuView
from views.no_deck_registry_menu_view import NoDeckRegistryMenuView
from views.deck_selection_menu_view import DeckSelectionMenuView
from models.deck import Deck

class AppController:
  def __init__(self, main_window):
    self.root_window = main_window
    self.deck = Deck()
    self.deck_select()

  def deck_select(self):
    deck_list = self.deck.get_deck_list()
    if(deck_list == []):
      self.show_no_deck_menu()
    else:
      self.show_deck_selection_menu()

  def show_no_deck_menu(self):
    model = self.deck
    anki_importer = AnkiImport()
    view = NoDeckRegistryMenuView(self, self.root_window)
    view.on_press_create_deck(model.create_deck)
    view.on_press_import_anki(anki_importer.create_import)

  def show_deck_selection_menu(self):
    model = self.deck
    deck_list = self.deck.get_deck_list()
    view = DeckSelectionMenuView(self, self.root_window, deck_list)
    view.on_button_press(model.set_deck)

  def show_main_menu(self):
    view = MainMenuView(self.root_window)

