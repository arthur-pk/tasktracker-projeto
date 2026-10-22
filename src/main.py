"""
TaskTracker - Aplicação CLI de Gerenciamento de Tarefas
Fase 2 - Bootcamp II
"""

def validar_titulo() -> str:
    """Solicita e valida o título da tarefa (não aceita vazio ou apenas espaços)."""
    while True:
        titulo = input("Digite o título da tarefa: ").strip()
        if titulo:
            return titulo
        print("❌ Erro: O título é obrigatório e não pode estar vazio. Tente novamente.\n")

def validar_prioridade() -> str:
    """Solicita e valida a prioridade (Alta, Média ou Baixa)."""
    opcoes_validas = {
        "1": "Alta", "alta": "Alta",
        "2": "Média", "média": "Média", "media": "Média",
        "3": "Baixa", "baixa": "Baixa"
    }
    while True:
        print("\nEscolha a prioridade:")
        print("  1. Alta")
        print("  2. Média")
        print("  3. Baixa")
        entrada = input("Digite a opção (1-3 ou Alta/Média/Baixa): ").strip().lower()
        
        if entrada in opcoes_validas:
            return opcoes_validas[entrada]
        
        print("❌ Erro: Prioridade inválida! Escolha apenas entre Alta, Média ou Baixa.")

def cadastrar_tarefa(tarefas: list) -> None:
    """Realiza o cadastro de uma nova tarefa com validações de regra de negócio."""
    print("\n" + "=" * 40)
    print("      CADASTRO DE NOVA TAREFA")
    print("=" * 40)
    
    titulo = validar_titulo()
    descricao = input("Digite a descrição da tarefa (opcional): ").strip()
    prioridade = validar_prioridade()
    data_limite = input("Digite a data limite (ex: DD/MM/AAAA): ").strip()
    
    tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "descricao": descricao if descricao else "Sem descrição",
        "prioridade": prioridade,
        "data_limite": data_limite if data_limite else "Não informada",
        "status": "Pendente"
    }
    
    tarefas.append(tarefa)
    print(f"\n✅ Tarefa '{titulo}' cadastrada com sucesso!")

def visualizar_tarefas(tarefas: list) -> None:
    """Exibe todas as tarefas cadastradas de forma legível no terminal."""
    print("\n" + "=" * 40)
    print("      LISTA DE TAREFAS CADASTRADAS")
    print("=" * 40)
    
    if not tarefas:
        print("\nℹ️  Nenhuma tarefa cadastrada no momento.")
        return
    
    for t in tarefas:
        print("-" * 40)
        print(f"ID:          #{t['id']}")
        print(f"Título:      {t['titulo']}")
        print(f"Descrição:   {t['descricao']}")
        print(f"Prioridade:  {t['prioridade']}")
        print(f"Data Limite: {t['data_limite']}")
        print(f"Status:      {t['status']}")
        print("-" * 40)
    print(f"Total de tarefas: {len(tarefas)}")

def main():
    """Loop principal da aplicação CLI."""
    tarefas = []
    
    while True:
        print("\n" + "=" * 40)
        print("         TASKTRACKER - MENU")
        print("=" * 40)
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")
        
        opcao = input("\nEscolha uma opção (1-3): ").strip()
        
        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            print("\n👋 Encerrando o TaskTracker. Até logo!")
            break
        else:
            print("\n❌ Opção inválida! Escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()