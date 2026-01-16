# using dictionaries and functions

def phone():
    phonenumber = input("Enter Phone Number: ")
    digits_map = {
        "1": "one",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "0": "Zero",
    }
    output = " "
    for ch in phonenumber:
        output += digits_map.get(ch, "!") + " "
    print(output)

def square(number):
    return number*number

def agedisplay():
    try:
        age = int(input("Enter Age: "))
        income = 20000
        risk = income / age
        print (f"Age is: {age} and risk is : {risk} for the income {income}")
    except ZeroDivisionError:
        print("Age cannot be 0")    
    except ValueError:
        print ("Please enter a number")

print("Starting the function")
phone()
print (f"Result of the Square : {square(10)}")
agedisplay()
print("Function stopped")
