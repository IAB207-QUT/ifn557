class Order:

    def __init__(self, status, firstname, surname, email, phone, date, tours, total_cost):
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
       return f"Status: {self.status}, First Name: {self.firstname}, Surname: {self.surname}, Email: {self.email}, Phone: {self.phone}, Date: {self.date}, Tours: {self.tours}, Total Cost: {self.total_cost}\n" 