from controllers.app_controller import AppController
from services import db
import tkinter as tk


def main():
  db.init()

  window = tk.Tk()
  window.title("Nome do App")

  app_controller = AppController(window)

  window.mainloop()

if __name__ == "__main__":
  main()