# List of options
b = ['1.add', '2.subtract', '3.divide', '4.multiply']
print('Options:', b)

# User chooses an option
x = input('Choose your option (add, subtract, divide, multiply): ').lower()

if x == 'add':
    a = int(input("Enter first number: "))
    c = int(input("Enter second number: "))
    d = a + c
    print("Result:", d)

elif x == 'subtract':
    a = int(input("Enter first number: "))
    c = int(input("Enter second number: "))
    d = a - c
    print("Result:", d)

elif x == 'divide':
    a = int(input("Enter first number: "))
    c = int(input("Enter second number: "))
    if c != 0:  # Avoid division by zero
        d = a / c
        print("Result:", d)
    else:
        print("Error: Division by zero is not allowed.")

elif x == 'multiply':
    a = int(input("Enter first number: "))
    c = int(input("Enter second number: "))
    d = a * c
    print("Result:", d)

else:
    print("Invalid option. Please choose one of the options listed.")

