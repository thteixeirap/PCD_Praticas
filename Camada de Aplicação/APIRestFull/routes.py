from flask import Blueprint, request, jsonify
from users import get_all_users, find_user_by_id, create_user, update_user, delete_user
from utils import validate_user_data, get_pagination_params

bp = Blueprint('api', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    page, per_page = get_pagination_params(request)
    users_list = get_all_users(page, per_page)
    return jsonify([user.to_dict() for user in users_list])

@bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = find_user_by_id(user_id)
    return jsonify(user.to_dict()) if user else ('', 404)

@bp.route('/users', methods=['POST'])
def create_new_user():
    data = request.get_json()
    is_valid, error_message = validate_user_data(data)
    if not is_valid:
        return jsonify({"error": error_message}), 400

    new_user = create_user(data['id'], data['name'], data['email'])
    return jsonify(new_user.to_dict()), 201

@bp.route('/users/<int:user_id>', methods=['PUT'])
def update_existing_user(user_id):
    data = request.get_json()
    is_valid, error_message = validate_user_data(data)
    if not is_valid:
        return jsonify({"error": error_message}), 400

    user = update_user(user_id, data['name'], data['email'])
    return jsonify(user.to_dict()) if user else ('', 404)

@bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_existing_user(user_id):
    delete_user(user_id)
    return ('', 204)
