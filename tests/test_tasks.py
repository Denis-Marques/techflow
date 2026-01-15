from src.app import criar_tarefa, listar_tarefas

def test_criar_tarefa():
    tarefa = criar_tarefa("Entrega urgente", "Alta")
    assert tarefa["titulo"] == "Entrega urgente"

def test_listar_tarefas():
    tarefas = listar_tarefas()
    assert len(tarefas) >= 1
