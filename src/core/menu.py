from core.review import review
from core.create_question import create_question

def menu():
    print("\n--- APP DE REVISÃO DE IDIOMAS ---")
    print("1. Estudar (Revisão)")
    print("2. Criar novo (Adicionar palavra)")
    print("3. Atualizar (Editar registro)")
    print("4. Sair")
    print("---------------------------------")

    option = input("Selecione uma opcao\n")

    match option:
      case "1":
        review()
      case "2":
        create_question()
      case "3":
        print("pendente")
      case "4":
        exit()
      case _:
        print ("Opcao Invalida")