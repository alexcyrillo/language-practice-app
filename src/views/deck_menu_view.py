import tkinter as tk

class DeckMenuView:
  def __init__(self, root_window):
    self.frame = tk.Frame(root_window) 
    self.frame.pack()

  def init(self):
    self.title("Meus Decks")

    bt1 = tk.Button(self.frame, text="Listar Cards")
    bt1.grid(column=0, row=0)

    bt2 = tk.Button(self.frame, text="Editar Card")
    bt2.grid(column=0, row=1)

    bt3 = tk.Button(self.frame, text="Mudar Deck Selecionado")
    bt3.grid(column=0, row=2)

    bt4 = tk.Button(self.frame, text="Apagar Deck")
    bt4.grid(column=0, row=3)

    bt_back = tk.Button(self.frame, text="Voltar", command=self.main_menu)
    bt_back.grid(column=0, row=4)