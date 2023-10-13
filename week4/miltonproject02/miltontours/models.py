from . import db

class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False, default = 'defaultcity.jpg')
    tours = db.relationship('Tour', backref='City', cascade="all, delete-orphan")

    def __repr__(self):
        return f"ID: {self.id}\nName: {self.name}\nDescription: {self.description}"

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
        return f"ID: {self.id}\nName: {self.name}\nDescription: {self.description}\nPrice: {self.price}\nCity: {self.city_id}\nDate: {self.date}"

class Order(db.Model):
    __tablename__='orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    total_cost = db.Column(db.Float)
    date = db.Column(db.DateTime)
    tours = db.relationship("Tour", secondary=orderdetails, backref="orders")
    
    def __repr__(self):
        return f"ID: {self.id}\nStatus: {self.status}\nFirst Name: {self.first_name}\nSurname: {self.surname}\nEmail: {self.email}\nPhone: {self.phone}\nDate: {self.date}\nTours: {self.tours}\nTotal Cost: ${self.total_cost}"