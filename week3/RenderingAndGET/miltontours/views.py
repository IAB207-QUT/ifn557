from flask import Blueprint, render_template, request

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return '<h1 style="color:red;"> Hello World!<h1>'

@bp.route('/secret/')
def secret():
    return '<h1 style="color:yellow;">You found the secret page</h1>'

@bp.route('/checkout/')
def checkout():
    
    # print form paramenters sent using GET
    print('Firstname: {}\nSurname: {}\nPhone: {}'\
        .format(request.args.get('firstname'), request.args.get('surname'), request.args.get('phone')))

    return render_template('checkout.html')

