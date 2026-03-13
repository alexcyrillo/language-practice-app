import tkinter as tk

from utils.clean_frame import clean_frame

class DeckSelectionMenuView:
  def __init__(self, controller, root_window, deck_names):
    clean_frame(root_window)
    self.frame = tk.Frame(root_window)
    self.frame.pack()
    self.controller = controller
    self._on_button_press_callback = None
    self.selected_deck = tk.StringVar()
    self._create(deck_names)

  def _create(self, deck_names):
    last_idx = 0

    label = tk.Label(self.frame, text="Selecione um Deck")
    label.grid(column=0, row=0)

    for i, deck in enumerate(deck_names):
      bt = tk.Radiobutton(self.frame, text=deck, variable=self.selected_deck, value=deck)
      bt.grid(column = 0, row = i + 1)
      last_idx = i + 1

    self.selected_deck.set(deck_names[0])

    send_button = tk.Button(self.frame, text="Selecionar", command=self._set_deck_and_close)
    send_button.grid(column = 0, row = last_idx + 1)

  def _set_deck_and_close(self):
    if(self._on_button_press_callback != None):
      self._on_button_press_callback(self.selected_deck.get())
      self.controller.show_main_menu()

  def on_button_press(self, callback):
    self._on_button_press_callback = callback