import tkinter as tk

class AnkiMenuView:
  def __init__(self, root_window):
    self.frame = tk.Frame(root_window) 
    self.frame.pack()

  def init(self):
    self.title("Importar Deck do Anki")

    bt1 = tk.Button(self.frame, text="Importar Novo")
    bt1.grid(column=0, row=0)

    bt2 = tk.Button(self.frame, text="Atualizar Decks")
    bt2.grid(column=0, row=1)

    bt_back = tk.Button(self.frame, text="Voltar", command=self.main_menu)
    bt_back.grid(column=0, row=2)

