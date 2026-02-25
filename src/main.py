from core.menu import menu
from database import db

def main():
  db.init()

  while True:
    menu()

if __name__ == "__main__":
  main()