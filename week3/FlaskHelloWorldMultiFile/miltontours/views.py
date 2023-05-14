from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return '<h1 style="color:red;"> Hello World!<h1>'

@bp.route('/secret/')
def secret():
    return '<h1 style="color:yellow;">You found the secret page</h1>'

