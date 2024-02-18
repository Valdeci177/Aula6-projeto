import os

# Função para limpar a tela do console
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Definição da estrutura de dados para representar uma tarefa
class Task:
    def __init__(self, name, description, priority, category):
        self.name = name
        self.description = description
        self.priority = priority
        self.category = category
        self.completed = False

# Lista de tarefas
tasks = []

# Função para adicionar uma nova tarefa
def add_task():
    clear_screen()
    name = input("Nome da tarefa: ")
    description = input("Descrição: ")
    priority = input("Prioridade: ")
    category = input("Categoria: ")
    task = Task(name, description, priority, category)
    tasks.append(task)
    print("Tarefa adicionada com sucesso!")

# Função para listar todas as tarefas
def list_tasks():
    clear_screen()
    if tasks:
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task.name} - {task.description} - {task.priority} - {task.category} - {'Concluída' if task.completed else 'Pendente'}")
    else:
        print("Não há tarefas cadastradas.")

# Função para marcar uma tarefa como concluída
def complete_task():
    clear_screen()
    list_tasks()
    task_index = int(input("Digite o número da tarefa que deseja marcar como concluída: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index].completed = True
        print("Tarefa marcada como concluída!")
    else:
        print("Índice de tarefa inválido.")

# Função para exibir tarefas por prioridade
def tasks_by_priority():
    clear_screen()
    priority = input("Digite a prioridade das tarefas que deseja visualizar: ")
    filtered_tasks = [task for task in tasks if task.priority.lower() == priority.lower()]
    if filtered_tasks:
        for task in filtered_tasks:
            print(f"{task.name} - {task.description} - {task.priority} - {task.category} - {'Concluída' if task.completed else 'Pendente'}")
    else:
        print("Não há tarefas com essa prioridade.")

# Função para exibir tarefas por categoria
def tasks_by_category():
    clear_screen()
    category = input("Digite a categoria das tarefas que deseja visualizar: ")
    filtered_tasks = [task for task in tasks if task.category.lower() == category.lower()]
    if filtered_tasks:
        for task in filtered_tasks:
            print(f"{task.name} - {task.description} - {task.priority} - {task.category} - {'Concluída' if task.completed else 'Pendente'}")
    else:
        print("Não há tarefas nessa categoria.")

# Menu de comandos
def main_menu():
    while True:
        clear_screen()
        print("GERENCIADOR DE TAREFAS DIÁRIAS")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Visualizar Tarefas por Prioridade")
        print("5. Visualizar Tarefas por Categoria")
        print("6. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            tasks_by_priority()
        elif choice == '5':
            tasks_by_category()
        elif choice == '6':
            print("Obrigado por utilizar o Gerenciador de Tarefas!")
            break
        else:
            input("Opção inválida. Pressione Enter para continuar.")

if __name__ == "__main__":
    main_menu()
