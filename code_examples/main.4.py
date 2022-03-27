#!/usr/bin/python3     
    
class User():    
    def __init__(self, name, age):    
        self.name = name    
        self.age = age    
    
    def toString(self):    
        return f"Hello {self.name} you are {self.age} years old"    
    
def main():    
    name = input("Please enter your name: " )    
    age = input("Please enter your age: " )    
    user = User(name, age)    
        
    print(user.toString())    
    
    return name    
    
def sayGoodBye(name):    
    print(f"Goodbye {name}")    
    
    
if __name__ ==  "__main__":    
    name = main()    
    sayGoodBye(name)    
