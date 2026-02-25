from src.core.menu import menu
import src.database.db as db

def main():
  db.init()

  while True:
    menu()

if __name__ == "__main__":
  main()