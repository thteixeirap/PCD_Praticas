import xmlrpc.client

# Conecta ao servidor RPC
server = xmlrpc.client.ServerProxy("http://localhost:8000/RPC2")

# Criar uma nova tarefa
response = server.create_task("Complete RPC Project", "Finish the RPC task manager project.")
print(response)

# Listar todas as tarefas
tasks = server.list_tasks()
print("Lista de Tarefas:")
for task_id, task in tasks.items():
    print(f"ID: {task_id}, Title: {task['title']}, Description: {task['description']}")

# Deletar uma tarefa
response = server.delete_task(1)
print(response)

# Tentar deletar uma tarefa inexistente
response = server.delete_task(999)
print(response)
