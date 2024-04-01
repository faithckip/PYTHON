class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")
        
#Create an instance of the person class
person1 = Person("Faith", 30, "Female")
person2 = Person("Keith", 34, "Male")
person3 = Person("Shela", 36, "Female")

#Call the introduce method to display the person's information
person1.introduce()
person2.introduce()
person3.introduce()