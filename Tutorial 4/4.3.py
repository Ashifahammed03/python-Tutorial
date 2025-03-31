class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price
    
    def cost(self):
        print(f"Model: {self.model}, Year: {self.year}, Price: ${self.price}")
if __name__ == "__main__":
   car1 = Car("Toyota", 2022, 30000)
    car2 = Car("Honda", 2021, 25000)
    car1.cost()
    car2.cost()
    