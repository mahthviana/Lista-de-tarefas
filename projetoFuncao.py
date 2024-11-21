# Crie funções para adicionar tarefas, == CONCLUIDA
# listar tarefas, == CONCLUIDA
# marcar tarefas como concluídas, == CONCLUIDA
# --- exibir tarefas por prioridade ou categoria (Filter) ---, ==  CONCLUIDA
# e outras funcionalidades que desejar.
import os

listaDeTarefas = []

listaDeCategorias = ["Saúde", "Doméstica", "Lazer", "Estudos", "Esporte"]
listaDePrioridades = ["Baixa", "Média", "Alta", "Urgente"]
listaDeStatus = ["A Fazer", "Concluída"]

def adicionarTarefas():
  tarefa = input("Digite a terefa desejada: ")
  
  while True:
    prioridade = int(input("""
  --- MENU DE PRIORIDADE ---
          1 - BAIXA
          2 - MÉDIA
          3 - ALTA
          4 - URGENTE
                        
Digite a opção desejada: """))
    if prioridade > 0 and prioridade <= 4:
      nivelDePrioridade = listaDePrioridades[prioridade - 1]
      break
    else:
      print("Prioridade inválida")

  while True:
    categoria = int(input("""
    --- MENU DE CATEGORIAS ---
          1 - SAÚDE
          2 - DOMÉSTICA
          3 - LAZER
          4 - ESTUDOS
          5 - ESPORTE
                          
  Digite a opção desejada: """))
    if categoria > 0 and categoria <= 5:
      tipoDeCategoria = listaDeCategorias[categoria - 1]
      break
    else:
      print("Categoria inválida")
  
  while True:
    status = int(input("""
    --- MENU DE Status ---
          1 - A Fazer
          2 - Concluída
                          
  Digite a opção desejada: """))
    if status > 0 and status <= 2:
      tipoDeStatus = listaDeStatus[status - 1]
      break
    else:
      print("Prioridade inválida")
  
  corpoDaTarefa = {
    "Tarefa":tarefa,
    "Prioridade":nivelDePrioridade,
    "Categoria":tipoDeCategoria,
    "Status": tipoDeStatus
  }
  
  listaDeTarefas.append(corpoDaTarefa)



def listarTarefas():
  for tarefaDaVez in listaDeTarefas:
    print(f"""
          Tarefa - {tarefaDaVez['Tarefa']}
          Prioridade - {tarefaDaVez['Prioridade']}
          Categoria - {tarefaDaVez['Categoria']}
          Status - {tarefaDaVez['Status']}
          """)



# Depois de cclicar número 3: Digita o nome da tarefa que deseja ser concluída
# tarefa=NomeDaTarefa - Disso ela vai ser concluída
def marcarComoConcluida(tarefa):
  for tarefaDaVez in listaDeTarefas:
    if tarefaDaVez["Tarefa"] == tarefa:
      tarefaDaVez["Status"] = "Concluída"
      print(f"A tarefa {tarefaDaVez['Tarefa']} foi marcada como concluída")
    
  return "Tarefa não encontrada.."



def filtrarTarefaPorCategoria():
  tarefas_encontradas = False
  filtro = int(input("""
    --- MENU DE CATEGORIAS ---
          1 - SAÚDE
          2 - DOMÉSTICA
          3 - LAZER
          4 - ESTUDOS
          5 - ESPORTE
                          
    Digite a opção desejada: """))
  
  filtroCategoria = listaDeCategorias[filtro - 1]

  for tarefaDaVez in listaDeTarefas:
    if tarefaDaVez["Categoria"] == filtroCategoria:
      
      tarefas_encontradas = True
      print(f"""
            Tarefa - {tarefaDaVez['Tarefa']}
            Prioridade - {tarefaDaVez['Prioridade']}
            Categoria - {tarefaDaVez['Categoria']}
            Status - {tarefaDaVez['Status']}
            """)
  if not tarefas_encontradas:
    print(f"Nenhuma tarefa foi encontrada com o filtro de Categoria: {filtro}")



def filtrarTarefaPorStatus():
  tarefas_encontradas = False

  filtro = int(input("""
    --- MENU DE Status ---
          1 - A Fazer
          2 - Concluída
                          
    Digite a opção desejada: """))
  
  filtroStatus = listaDeStatus[filtro - 1]
  
  for tarefaDaVez in listaDeTarefas:
    if tarefaDaVez["Status"] == filtroStatus:
      tarefas_encontradas = True
      print(f"""
            Tarefa - {tarefaDaVez['Tarefa']}
            Prioridade - {tarefaDaVez['Prioridade']}
            Categoria - {tarefaDaVez['Categoria']}
            Status - {tarefaDaVez['Status']}
            """)
  if not tarefas_encontradas:
    print(f"Nenhuma tarefa foi encontrada com o filtro de Status: {filtro}")



def filtrarTarefaPorPrioridade():
  tarefas_encontradas = False

  filtro = int(input("""
  --- MENU DE PRIORIDADE ---
          1 - BAIXA
          2 - MÉDIA
          3 - ALTA
          4 - URGENTE
                        
Digite a opção desejada: """))
  
  filtroPrioridade = listaDePrioridades[filtro - 1]
  
  for tarefaDaVez in listaDeTarefas:
    if tarefaDaVez["Prioridade"] == filtroPrioridade:
      tarefas_encontradas = True
      print(f"""
            Tarefa - {tarefaDaVez['Tarefa']}
            Prioridade - {tarefaDaVez['Prioridade']}
            Categoria - {tarefaDaVez['Categoria']}
            Status - {tarefaDaVez['Status']}
            """)
  if not tarefas_encontradas:
    print(f"Nenhuma tarefa foi encontrada com o filtro de Prioridade: {filtro}")



# def removerTarefa():
#   nomeDaTarefa = input("Digite o nome da tarefa que deseja remover: ")
#   for tarefaDaVez in listaDeTarefas:
#     if tarefaDaVez["Tarefa"] == nomeDaTarefa:
#       listaDeTarefas.remove()



def limparTerminal():
  terminal = os.name
  if terminal == 'posix':
    os.system('clear')

  if terminal == 'nt':
    os.system('cls')

while True:
  print("""
        --- MENU ---
        1 - ADICIONAR UMA TAREFA
        2 - LISTAR TAREFAS
        3 - MARCAR TAREFA COMO CONCLUÍDA
        4 - FILTRAR TAREFA POR CATEGORIA
        5 - FILTRAR TAREFA POR STATUS
        6 - FILTRAR TAREFA POR PRIORIDADE
        0 - SAIR
        """)
  opcao = int(input("Digite a opção deseja: "))
  limparTerminal()
  
  match opcao:
    case 1:
      adicionarTarefas()
    case 2:
      listarTarefas()
    case 3: 
      tarefa = input("Digite a tarefa que você deseja marcar como concluída: ")
      marcarComoConcluida(tarefa=tarefa)
    case 4:
      filtrarTarefaPorCategoria()
    case 5:
      filtrarTarefaPorStatus()
    case 6:
      filtrarTarefaPorPrioridade()
    case 0:
      print("Programa Finalizado")
      break
    case _:
      print("Opção inválida...")