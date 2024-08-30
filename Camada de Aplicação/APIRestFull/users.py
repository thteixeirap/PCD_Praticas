from models import User

# Dados simulados
users = [
    User(1, "John Doe", "john@example.com"),
    User(2, "Jane Smith", "jane@example.com")
]

def get_all_users(page=1, per_page=10):
    start = (page - 1) * per_page
    end = start + per_page
    return users[start:end]

def find_user_by_id(user_id):
    return next((user for user in users if user.id == user_id), None)

def create_user(id, name, email):
    new_user = User(id, name, email)
    users.append(new_user)
    return new_user

def update_user(user_id, name, email):
    user = find_user_by_id(user_id)
    if user:
        user.name = name
        user.email = email
    return user

def delete_user(user_id):
    global users
    users = [user for user in users if user.id != user_id]
