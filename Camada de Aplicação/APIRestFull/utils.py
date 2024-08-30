def validate_user_data(data):
    if "name" not in data or "email" not in data:
        return False, "Missing 'name' or 'email' in request body."
    return True, ""

def get_pagination_params(request):
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))
    return page, per_page
