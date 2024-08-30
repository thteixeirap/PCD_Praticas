from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def create_task(self, title, description):
        task_id = str(self.next_id)  # Converte o ID da tarefa para string
        self.tasks[task_id] = {"title": title, "description": description}
        self.next_id += 1
        return f"Task created with ID {task_id}"

    def list_tasks(self):
        return self.tasks

    def delete_task(self, task_id):
        task_id = str(task_id)  # Certifica-se de que o ID é uma string
        if task_id in self.tasks:
            del self.tasks[task_id]
            return f"Task with ID {task_id} deleted"
        else:
            return f"Task with ID {task_id} not found"

# Restringe a execução a uma rota específica (/RPC2)
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Cria o servidor
server = SimpleXMLRPCServer(("localhost", 8000), requestHandler=RequestHandler)
server.register_introspection_functions()

# Instancia o gerenciador de tarefas
task_manager = TaskManager()

# Registra as funções do gerenciador de tarefas no servidor RPC
server.register_instance(task_manager)

print("Servidor RPC rodando na porta 8000...")
server.serve_forever()
