from views.deck_selection_menu_view import DeckSelectionMenuView
from views.main_menu_view import MainMenuView
from models.deck import Deck
from views.no_deck_registry_menu_view import NoDeckRegistryMenuView

class MenusController():
  def __init__(self, main_window):
    self.root_window = main_window
    self.selected_deck = None
    self.deck_select()

  def deck_select(self):
    model = Deck()
    deck_names = self.model.list_decks()
    if(deck_names == 0):
      self.show_no_deck_menu()
    else:
      self.show_deck_selection_menu(deck_names)

  def show_no_deck_menu(self):
    view = NoDeckRegistryMenuView(self.root_window)
    model = Deck
    view.on_press_create_deck(Deck.create_deck)
    view.on_press_import_anki(Deck.)
    view.list_options()

  def show_deck_selection_menu(self):
    view = DeckSelectionMenuView(self.root_window)
    view._create(self.deck_names)

  def show_main_menu(self):
    view = MainMenuView(self)

