class HelloWorld:
    def __init__(self, name, city):
        self.name = name
        self.city = city
    
    def greet(self):
        return f"Hello {self.name}, from {self.city}!"