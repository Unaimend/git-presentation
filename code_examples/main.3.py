#!usr/bin/python3
def main():
 name = readline()
 print("hello from python {name}")
 
 
def sayGoodBye(name):
 print(f"Goodbye {name}")

if  __name__ == "__main__":
 name = main()
 sayGoodBye(name)
