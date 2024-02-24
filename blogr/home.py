from flask import Blueprint

bp=Blueprint ('home',__name__)

@bp.route('/')
def index():
    return 'Pagina de Inicio'


@bp.route('/blog')
def blog():
    return 'Pagina de Blog'