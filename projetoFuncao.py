# Crie funções para adicionar tarefas, == CONCLUIDA
# listar tarefas, == CONCLUIDA
# marcar tarefas como concluídas, == CONCLUIDA
# --- exibir tarefas por prioridade ou categoria (Filter) ---, ==  CONCLUIDA
# e outras funcionalidades que desejar.
import os

listaDeTarefas = []


def adicionarTarefas():
  tarefa = input("Digite a terefa desejada: ")
  prioridade = input("Digite o nível de prioridade (1 - 2 - 3): ")
  categoria = input("Digite a categoria da sua tarefa: ")
  status = input("Digite o status da sua tarefa (Concluída ou Realizar): ")
  
  corpoDaTarefa = {
    "Tarefa":tarefa,
    "Prioridade":prioridade,
    "Categoria":categoria,
    "Status": status
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
      return f"A tarefa {tarefaDaVez['Tarefa']} foi marcada como concluída"
    
  return "Tarefa não encontrada.."

def filtrarTarefaPorCategoria(filtro):
  tarefas_encontradas = False
  
  for tarefaDaVez in listaDeTarefas:
    if tarefaDaVez["Categoria"] == filtro:
      tarefas_encontradas = True
      print(f"""
            Tarefa - {tarefaDaVez['Tarefa']}
            Prioridade - {tarefaDaVez['Prioridade']}
            Categoria - {tarefaDaVez['Categoria']}
            Status - {tarefaDaVez['Status']}
            """)
    if not tarefas_encontradas:
      print(f"Nenhuma tarefa foi encontrada com o filtro de Categoria: {filtro}")
      

def filtrarTarefaPorStatus(filtro):
  tarefas_encontradas = False
  
  for tarefaDaVez in listaDeTarefas:
    if tarefaDaVez["Status"] == filtro:
      tarefas_encontradas = True
      print(f"""
            Tarefa - {tarefaDaVez['Tarefa']}
            Prioridade - {tarefaDaVez['Prioridade']}
            Categoria - {tarefaDaVez['Categoria']}
            Status - {tarefaDaVez['Status']}
            """)
    if not tarefas_encontradas:
      print(f"Nenhuma tarefa foi encontrada com o filtro de Status: {filtro}")

while True:
  print("""
        --- MENU ---
        1 - ADICIONAR UMA TAREFA
        2 - LISTAR TAREFAS
        3 - MARCAR TAREFA COMO CONCLUÍDA
        4 - FILTRAR TAREFA POR CATEGORIA
        5 - FILTRAR TAREFA POR STATUS
        0 - SAIR
        """)
  opcao = int(input("Digite a opção deseja: "))
  os.system("clear")
  
  match opcao:
    case 1:
      adicionarTarefas()
    case 2:
      listarTarefas()
    case 3: 
      tarefa = input("Digite a tarefa que você deseja marcar como concluída: ")
      marcarComoConcluida(tarefa=tarefa)
    case 4:
      categoria = input("Digite a categoria que deseja visualizar: ")
      filtrarTarefaPorCategoria(filtro=categoria)
    case 5:
      status = input("Digite a status que deseja visualizar: ")
      filtrarTarefaPorStatus(filtro=status)
    case 0:
      print("Programa Finalizado")
      break
    case _:
      print("Opção inválida...")