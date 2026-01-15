tarefas = []

def criar_tarefa(titulo, prioridade):
    if not titulo:
        raise ValueError("O título da tarefa é obrigatório")

    tarefa = {
        "titulo": titulo,
        "prioridade": prioridade
    }
    tarefas.append(tarefa)
    return tarefa

def listar_tarefas():
    return tarefas
