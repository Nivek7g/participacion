from functools import wraps
from flask import redirect, url_for, session, flash

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Por favor inicia sesión para acceder a esta página.')
            return redirect(url_for('auth_controller.login'))
        return f(*args, **kwargs)
    return decorated_function