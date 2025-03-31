class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.cost = 0.0
    
    def get_details(self, title, author, cost):
        self.title = title
        self.author = author
        self.cost = cost
    
    def print_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Cost: ${self.cost}")



if __name__ == "__main__":
       book = Book()
    book.get_details("Python Programming", "John Doe", 45.99)
    book.print_details()
