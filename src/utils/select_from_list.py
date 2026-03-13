from typing import Callable
import tkinter as tk

def list_menu_options(self, frame, options: list[tuple[str, Callable[[], None]]]):
  for idx, (bt_text, bt_command) in enumerate(options):
    bt = tk.Button(frame, text=bt_text, command=bt_command)
    bt.grid(column = 0, row = idx)