from flask import Blueprint, render_template, request, session

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    if 'firstname' in session:
        message = ('<h1 style="color:red;"> Hello {}</h1>'.format(session['firstname']))
    else:
        message = '<h1 style="color:red;"> Hello World!<h1>'
    return message

@bp.route('/secret/')
def secret():
    return '<h1 style="color:yellow;">You found the secret page</h1>'

@bp.route('/checkout/', methods=['POST','GET'])
def checkout():
    
    # put form firstname into session
    session['firstname'] = request.values.get('firstname')

    return render_template('checkout.html')

