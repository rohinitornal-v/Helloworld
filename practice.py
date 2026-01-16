# using dictionaries, classes and functions

class PrintNumbers:
    def phone(self):
        phone_number = input("Enter Phone Number: ")
        digits_map = {
            "1": "One",
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
        for ch in phone_number:
            output += digits_map.get(ch, "!") + " "
        print("Phone number in words:", output)


class Square:
    def square(self, number):
        return number * number


class AgeTryExcept:
    def agedisplay(self):
        try:
            age = int(input("Enter Age: "))
            income = 20000
            risk = income / age
            print(f"Age is: {age} and risk is: {risk} for the income {income}")
        except ZeroDivisionError:
            print("Age cannot be 0")
        except ValueError:
            print("Please enter a valid number")


# -----------------------------
# Running the program
# -----------------------------

print("Starting the functions...\n")

# Phone number in words
phone = PrintNumbers()
phone.phone()

# Square of a number
sqr = Square()
number_to_square = 10
print(f"\nSquare of {number_to_square}: {sqr.square(number_to_square)}")

# Age and risk
age = AgeTryExcept()
age.agedisplay()

print("\nFunctions finished.")