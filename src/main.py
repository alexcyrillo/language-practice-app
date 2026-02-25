from core.menu import main_menu
from database import db

def main():
  db.init()

  while True:
    main_menu()

if __name__ == "__main__":
  main()