class Mobile:
    def __init__(self):
        self.company = ""
        self.model = ""
        self.price = 0.0
    
    def set_details(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price
    
    def display_details(self):
        print(f"Company: {self.company}, Model: {self.model}, Price: ${self.price}")

if __name__ == "__main__":
       mobile = Mobile()
    mobile.set_details("Samsung", "Galaxy S21", 799.99)
    mobile.display_details()