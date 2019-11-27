from apps.users import users_bp


@users_bp.route('/users/')
def user_index():
    return 'user_index!'

