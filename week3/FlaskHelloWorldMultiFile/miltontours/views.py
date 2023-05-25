from flask import Blueprint, request, redirect, url_for, render_template
from .forms import CheckoutForm

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route("/checkout", methods=['GET','POST'])
def checkout():
    checkout_form = CheckoutForm()
    if request.method == 'POST':
        print(request.values.get('firstname'))
        print(request.values.get('surname'))
        print(request.values.get('phone'))
        return redirect(url_for('main.index'))
    return render_template('checkout.html', form=checkout_form)


@bp.route('/secret/')
def secret():
    return '<h1 style="color:yellow;">You found the secret page</h1>'

