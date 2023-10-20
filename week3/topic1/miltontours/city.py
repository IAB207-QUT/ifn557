class City:
    
    def __init__(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image

    def get_city_details(self):
        return str(self)

    def __repr__(self):
        return f"Name: {self.name}, Description: {self.description}, Image: {self.image}\n" 