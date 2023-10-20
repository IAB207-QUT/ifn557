from flask import Blueprint, render_template
from .models import City, Tour, Order
from . import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    cities = db.session.scalars(db.select(City).order_by(City.id)).all()
    return render_template('index.html', cities=cities)

@main_bp.route('/tours/<int:cityid>')
def citytours(cityid):
    tours = db.session.scalars(db.select(Tour).where(Tour.city_id==cityid)).all()
    return render_template('citytours.html', tours=tours)

# STUBS for routes not implemented yet
# (get_url links in the templates will fail without these routes defined)

@main_bp.route('/order', methods=['POST','GET'])
def order():
    #return render_template('order.html', order = order, totalprice = order.total_cost)
    # order = db.session.scalar(db.select(Order).where(Order.id==session['order_id']))
    return 'not implemented yet'

@main_bp.route('/deleteorder')
def deleteorder():
    #return render_template('index.html')
    return 'not implemented yet'

@main_bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    #return render_template('index.html')
    return 'not implemented yet'

@main_bp.route('/checkout', methods=['POST','GET'])
def checkout():
    #return render_template('checkout.html', form = form)
    return 'not implemented yet'