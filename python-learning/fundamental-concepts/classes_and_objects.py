class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def walk(self):
        print(self.name + " is walking...")
        
    def speak(self):
        print('Hello my name is ' + self.name + ' and I am ' + str(self.age) + ' years old.')
    
steven = Person("Steven", 21)
print(steven.name + ' ' + str(steven.age))
steven.speak()
steven.walk()

print("-----------------------")

wesley = Person("Wesley", 21)
print(wesley.name + ' ' + str(wesley.age))
wesley.speak()
wesley.walk()
