# # Create a class called ServiceMember that stores the branch of service, name, rank, and MOS of a service member. The class should allow you to change rank and mos using two functions changeMOS and changeRank.

# # For example:

# #     Creating an instance with soldier1 = ServiceMember('Army', 'Joe Rogan', 'E6', '11B') and printing soldier1 should return: "Service: Army, Name: Joe Rogan, Rank: E6, MOS: 11B".
# #     Calling soldier1.changeMOS('11A') and soldier1.changeRank('2LT') and then printing soldier1 should return: "Service: Army, Name: Joe Rogan, Rank: 2LT, MOS: 11A".

# class ServiceMember:
    
#     def __init__(self, service, name, rank, MOS):
#         self.service = service
#         self.name = name
#         self.rank = rank
#         self.MOS = MOS
    
#     def __str__(self):
#         return f'Service: {self.service}, Name: {self.name}, Rank: {self.rank}, MOS: {self.MOS}'

#     def changeMOS(self, newMOS):
#         self.MOS = newMOS
    
#     def changeRank(self, newRank):
#         self.rank = newRank

# soldier1 = ServiceMember('Army','Joe Rogan','E6','11B')
# print(soldier1)
# soldier1.changeMOS('11A')
# soldier1.changeRank('2LT')
# print(soldier1)

# soldier2 = ServiceMember('Army','John Wick','E5','17C')
# print(soldier2)
# soldier2.changeMOS('17A')
# soldier2.changeRank('2LT')
# print(soldier2)

# ##########################################

# # Build a simple class called Dog.

# # The class should initialize every instance of Dog created to start with the following:
# # Attribute 	Value of attribute:
# # name 	Fido
# # tricks 	empty list

# # Build a function named change_name that accepts a parameter. The parameter provided will be used to overwrite the dog's initialized name.

# # Build another function named new_trick that accepts a parameter. The parameter should be appended to the empty list of tricks that each dog is initialized with.

# # Build a conversion to string function (hint: Think of the double underscore) that returns a string in the following format:
# # "My dog's name is {name}. name can perform the following tricks: {tricks}"

# class Dog:

#     def __init__(self):
#         self.name = 'Fido'
#         self.tricks = []

#     def __str__(self):
#         return f"My dog's name is {self.name}. {self.name} can perform the following tricks: {str(self.tricks)}"

#     def change_name(self,newName):
#         self.name = newName

#     def new_trick(self,newTrick):
#         self.tricks.append(newTrick)

# test = Dog()
# print(test)
# test.change_name('Spot')
# test.new_trick('sit')
# print(test)
# test.new_trick('lay down')
# print(test)

# ##########################################

# class Car:

#     def __init__(self,year,make,model,color,trim,trans):
#         self.year = year
#         self.make = make
#         self.model = model
#         self.color = color
#         self.trim = trim
#         self.trans = trans

#     def __str__(self):
#         return f'Year: {self.year}\nMake: {self.make}\nModel: {self.model}\nColor: {self.color}\nTrim: {self.trim}\nTransmission: {self.trans}'

# car1 = Car('2024','Honda','Civic','White','EX','Automatic')  
# print(car1)

# ##########################################

class Chest:

    def __init__(self,items):
        self.chest = [items]

    def __str__(self):
        return f'Chest: {self.chest}'
    
    def add(self,newItem):
        self.chest.append(newItem)

    def drop(self,delItem):
        self.chest.remove(delItem)

    def empty(self):
        self.chest = []

chest1 = Chest('swords', 'bows', 'daggers') 
print(chest1)