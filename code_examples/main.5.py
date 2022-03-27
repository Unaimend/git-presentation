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
