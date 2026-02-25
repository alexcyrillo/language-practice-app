def select_from_list(options, message=None):
  while True:
    try:
      for i, el in enumerate(options, start = 1):
        print(f"{i}: {el}")
      
      if(message == None):
        selected_index = int(input("Selecione uma Opcao\n")) - 1
      else:
        selected_index = int(input(f"{message}\n")) - 1

      if selected_index >= 0 and selected_index < len(options):
        return selected_index
      
      raise ValueError()
    except:
      print("Opcao Invalida")