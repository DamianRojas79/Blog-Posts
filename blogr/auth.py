from flask import Blueprint

bp=Blueprint ('auth',__name__, url_prefix='/auth')

@bp.route('register/')
def register():
    return 'Pagina de Register'

@bp.route('login/')
def login():
    return 'Pagina de login'

@bp.route('profile/')
def profile():
    return 'Pagina de Profile'
