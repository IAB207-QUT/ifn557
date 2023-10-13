from . import db

class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False, default = 'defaultcity.jpg')
    tours = db.relationship('Tour', backref='City', cascade="all, delete-orphan")

    def __repr__(self):
        return f"ID: {self.id}, Name: {self.name}, Description: {self.description}, Image: {self.image}\n"

orderdetails = db.Table('orderdetails', 
    db.Column('order_id', db.Integer,db.ForeignKey('orders.id'), nullable=False),
    db.Column('tour_id',db.Integer,db.ForeignKey('tours.id'),nullable=False),
    db.PrimaryKeyConstraint('order_id', 'tour_id') )

class Tour(db.Model):
    __tablename__ = 'tours'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False)
    price = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))
    
    def __repr__(self):
        return f"ID: {self.id}, Name: {self.name}, Description: {self.description}, Image: {self.image}, Price: {self.price}, City: {self.city_id}, Date: {self.date}\n"

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    first_name = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    total_cost = db.Column(db.Float)
    date = db.Column(db.DateTime)
    tours = db.relationship("Tour", secondary=orderdetails, backref="orders")
    
    def __repr__(self):
        return f"ID: {self.id}, Status: {self.status}, First Name: {self.first_name}, Surname: {self.surname}, Email: {self.email}, Phone: {self.phone}, Date: {self.date}, Tours: {self.tours}, Total Cost: {self.total_cost}\n"