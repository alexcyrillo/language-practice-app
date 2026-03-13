import tkinter as tk
from utils.clean_frame import clean_frame
from utils.select_from_list import list_menu_options

class MainMenuView:
  def __init__(self, root_window):
    main_menu_options = [("Estudar", self._start_study), ("Decks", self._decks_menu), ("Importar Deck do AnkiConnect", self._import_from_anki_menu)]
    clean_frame(root_window)
    self.frame = tk.Frame(root_window) 
    self.frame.pack()
    self._on_study_callback = None
    self._on_decks_callback = None
    self._on_anki_import_callback = None

    list_menu_options(self, self.frame, main_menu_options)

  def on_study_button_press(self, callback):
    self._on_study_callback = callback

  def on_decks_button_press(self, callback):
    self._on_decks_callback = callback

  def on_anki_import_button_press(self, callback):
    self._on_anki_import_callback = callback

  def _start_study(self):
    if(self._on_study_callback != None):
      return 0
    
  def _decks_menu(self):
    if(self.on_decks_button_press != None):
      return 0
    
  def _import_from_anki_menu(self):
    if(self._on_anki_import_callback != None):
      return 0

  # def _create(self):
  #   bt1 = tk.Button(self.frame, text="Estudar")
  #   bt1.grid(column=0, row=0)

  #   bt2 = tk.Button(self.frame, text="Decks", command=self.decks_sub_menu)
  #   bt2.grid(column=0, row=1)

  #   bt3 = tk.Button(self.frame, text="Importar Deck do AnkiConnect", command=self.anki_sub_menu)
  #   bt3.grid(column=0, row=2)

  #   bt4 = tk.Button(self.frame, text="Sair")
  #   bt4.grid(column=0, row=3)