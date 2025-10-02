class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        sum=0
        for i in self.marks:
         sum+=i
        print("hi",self.name,"your average score is:",sum/3)     
s1=Student("Aditya",[78,89,92])
s1.average()