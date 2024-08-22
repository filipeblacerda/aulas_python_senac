"""
Atividade Python - Menu
Grupo: Filipe Lacerda
        Hugo Alves
        Jairo Marques
"""


while True:
  print("MENU")
  print("1 - Criar Turma")
  print("2 - Adicionar Professor")
  print("3 - Adicionar Estudante")
  print("4 - Adicionar Nota")
  print("5 - Consultar Nota")
  print("6 - Salvar Nota")
  print("7 - Sair\n")

  opcao =  input("Escolha a opçao no menu: \n")

  if opcao == "1": 
    print("Criar Turma.\n")
    turma = input("Digite o nome da turma: ")
    print("Turma", turma, "criada com sucesso.\n")

  elif opcao == "2":
    print("Adicionar Professor.\n")
    nome = input("Digite o nome do professor: ")
    print("Professor", nome, "adicionado com sucesso.\n")

  elif opcao == "3":
    print("Adicionar Estudante.\n")
    nome = input("Digite o nome do estudante: ")
    print("Estudante", nome, "adicionado com sucesso.\n")

  elif opcao == "4":
    print("Adicionar Nota.\n")
    nome = input("Digite a nota do estudante: ")
    print("Nota adicionada com sucesso.\n")

  elif opcao == "5":
    print("Consultar Nota.\n")

  elif opcao == "6":
    print("Salvar Nota.\n")

  elif opcao == "7":
    print("Voce saiu do programa!!\n")
    break

  else:
    print("Digite uma opção válida!!\n")