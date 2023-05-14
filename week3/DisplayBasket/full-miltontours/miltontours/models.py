from datetime import datetime

class City:
    def __init__(self, id, name, description, image):
        self.id = id
        self.name = name
        self.description = description
        self.image = image

    def get_city_details(self):
        return str(self)

    def __repr__(self):
        str = "Id: {}, Name: {}, Description: {}, Image: {} \n" 
        str =str.format( self.id, self.name,self.description,self.image)
        return str

class Tour:
    def __init__(self, id, name, description, image, price, city, date):
        self.id = id
        self.name = name
        self.description = description
        self.image = image
        self.price = price
        self.city = city
        self.date = date
    
    def get_tour_details(self):
        return str(self)

    def __repr__(self):
        str = "Id: {}, Name: {}, Description: {}, Image: {}, Price: {}, City: {}, Date: {}\n" 
        str =str.format( self.id, self.name,self.description,self.image, self.price, self.city, self.date)
        return str

class Order:
    def __init__(self, id, status, firstname, surname, email, phone, date, tours, total_cost):
        self.id = id
        self.status = status
        self.firstname = firstname
        self.surname = surname
        self.email = email
        self.phone = phone
        self.date = date
        self.tours = tours
        self.total_cost = total_cost
    
    def get_tour_details(self):
        return str(self)

    def __repr__(self):
        str = "id: {}, Status: {}, Firstname: {}, Surname: {}, Email: {}, Phone: {}, Date: {}, Tours: {}, Total Cost: {}\n" 
        str =str.format( self.id, self.status,self.firstname,self.surname, self.email, self.phone, self.date, self.tours, self.total_cost)
        return str