from flask import Blueprint

bp=Blueprint ('post',__name__, url_prefix='/post')

@bp.route('/posts')
def posts():
    return 'Pagina de posts'

@bp.route('/create')
def  create():
    return 'Pagina de crteate'

@bp.route('/update')
def update():
    return 'Pagina de update'
