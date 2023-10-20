from flask import Blueprint, render_template, request

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return '<h1 style="color:red;"> Hello World!<h1>'

@bp.route('/secret')
def secret():
    return '<h1 style="color:green;">You found the secret page</h1>'

@bp.route('/checkout')
def checkout():
    # print form paramenters sent using GET
    print(f"First name: {request.args.get('firstname')}\nSurname: {request.args.get('surname')}\nPhone: {request.args.get('phone')}")
    return render_template('checkout.html')