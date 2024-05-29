from flask import Blueprint, render_template, url_for, request, session, flash, redirect, abort
from .models import City, Tour, Order
from datetime import datetime
from .forms import CheckoutForm
from . import db

main_bp = Blueprint('main', __name__)

# Home page
@main_bp.route('/')
def index():
    cities = db.session.scalars(db.select(City).order_by(City.id))
    return render_template('index.html', cities=cities)

# View all the tours of a city
@main_bp.route('/tours/<int:city_id>')
def citytours(city_id):
    tours = db.session.scalars(db.select(Tour).where(Tour.city_id==city_id))
    return render_template('citytours.html', tours=tours)

# Referred to as "Basket" to the user
@main_bp.route('/order', methods=['GET', 'POST'])
def order():
    tour_id = request.values.get('tour_id')
    print(f'Values: {tour_id}')
    # Retrieve order if there is one
    if 'order_id' in session.keys():
        order = db.session.scalar(db.select(Order).where(Order.id==session['order_id']))
        # Order will be None if order_id/session is stale
    else:
        # There is no order
        order = None

    # Create new order if needed
    if order is None:
        order = Order(status=False, first_name='', surname='', email='', phone='', total_cost=0.00, date=datetime.now())
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('Failed trying to create a new order!')
            order = None
    
    # Calculate total price
    total_price = 0
    if order is not None:
        for tour in order.tours:
            total_price += tour.price
    
    # Are we adding an item?
    if tour_id is not None and order is not None:
        tour = db.session.scalar(db.select(Tour).where(Tour.id==tour_id))
        try:
            order.tours.append(tour)
            for tour in order.tours:
                total_price += tour.price
            order.total_cost = total_price
            db.session.commit()
        except:
            flash('There was an issue adding the item to your basket', category='danger')
        return redirect(url_for('main.order'))
    return render_template('order.html', order=order, total_price=total_price)

@main_bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    id = request.form['id']
    print(f'Tour to delete ID is: {id}')
    if 'order_id' in session:
        order = db.session.scalar(db.select(Order).where(Order.id==session['order_id']))
        if not order:
            flash("There's no order to delete!")
            return redirect(request.referrer)
        print(order.tours)
        tour_to_delete = db.session.scalar(db.select(Tour).where(Tour.id==id))
        print(f'Deleting: {tour_to_delete.name}')
        try:
            tour_to_delete.qty = 0
            order.tours.remove(tour_to_delete)
            db.session.commit()
        except:
            print('Something went wrong when trying to delete the order')
            abort(500)
    return redirect(url_for('main.order'))

# Empty basket
@main_bp.route('/deleteorder')
def deleteorder():
    if 'order_id' in session:
        order = db.session.scalar(db.select(Order).where(Order.id==session['order_id']))
        for tour in order.tours:
            order.tours.remove(tour)
        session.pop('order_id')
        db.session.commit()
        flash('Basket emptied!')
    else:
        flash("There's no order to delete!")
        return redirect(request.referrer)
    return redirect(url_for('main.index'))

# Complete the order
@main_bp.route('/checkout', methods=['GET', 'POST'])
def checkout():
    form = CheckoutForm() 
    if 'order_id' in session:
        order = db.session.scalar(db.select(Order).where(Order.id==session['order_id']))
        if not order.tours:
            flash('You need to add some tours to your basket first!')
            return(redirect(request.referrer))
        if form.validate_on_submit():
            order.status = True
            order.first_name = form.firstname.data
            order.surname = form.surname.data
            order.email = form.email.data
            order.phone = form.phone.data
            total_cost = 0
            for tour in order.tours:
                total_cost += (tour.price * tour.qty)
            order.total_cost = total_cost
            order.date = datetime.now()
            try:
                db.session.commit()
                deleteorder()
                flash('Thank you! One of our team members will contact you soon.')
                return redirect(url_for('main.index'))
            except:
                flash('There was an issue completing your order')
                return (redirect(request.referrer))
    return render_template('checkout.html', form=form)