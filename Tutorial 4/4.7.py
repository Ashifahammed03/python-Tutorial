class StudentDetails:
    def __init__(self):
        self.rollno = 0
        self.mark1 = 0
        self.mark2 = 0
    
    def readData(self, rollno, mark1, mark2):
        self.rollno = rollno
        self.mark1 = mark1
        self.mark2 = mark2
    
    def computeTotal(self):
        return self.mark1 + self.mark2
    
    def printDetails(self):
        print(f"Roll No: {self.rollno}, Mark1: {self.mark1}, Mark2: {self.mark2}, Total: {self.computeTotal()}")


if __name__ == "__main__":
     student_data = StudentDetails()
    student_data.readData(103, 85, 90)
    student_data.printDetails()