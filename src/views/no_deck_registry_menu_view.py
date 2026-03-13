import tkinter as tk

from utils.clean_frame import clean_frame
from utils.select_from_list import list_menu_options

class NoDeckRegistryMenuView:
  def __init__(self, controller, root_window):
    no_deck_options = [
      ("Criar Deck", self._create_deck),
      ("Importar Deck do Anki", self._import_from_anki)
    ]
    self.controller = controller
    self._on_press_create_deck_callback = None
    self._on_press_import_anki_callback = None
    clean_frame(root_window)
    self.frame = tk.Frame(root_window)
    self.frame.pack()

    list_menu_options(self, self.frame, no_deck_options)

  def _create_deck(self):
    if(self._on_press_create_deck_callback != None):
      clean_frame(self.frame)
      label = tk.Label(self.frame, text="Digite o Nome do Deck")
      label.grid(column = 0, row = 0)
      entry = tk.Entry(self.frame)
      entry.grid(column = 0, row = 1)
      bt = tk.Button(self.frame, text="Enviar", command=lambda: (self._on_press_create_deck_callback(entry.get()), self.controller.show_deck_selection_menu()))
      bt.grid(column = 0, row = 2)

  def _import_from_anki(self):
    if(self._on_press_import_anki_callback != None):
      self._on_press_import_anki_callback()

  def on_press_create_deck(self, callback):
      self._on_press_create_deck_callback = callback

  def on_press_import_anki(self, callback):
    self._on_press_import_anki_callback = callback