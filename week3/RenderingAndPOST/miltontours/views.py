from flask import Blueprint, render_template, request

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return '<h1 style="color:red;"> Hello World!<h1>'

@bp.route('/secret')
def secret():
    return '<h1 style="color:green;">You found the secret page</h1>'

@bp.route('/checkout', methods = ['POST', 'GET'])
def checkout():
    # print form paramenters sent using POST
    print(f"First name: {request.values.get('firstname')}\nSurname: {request.values.get('surname')}\nPhone: {request.values.get('phone')}")
    return render_template('checkout.html')