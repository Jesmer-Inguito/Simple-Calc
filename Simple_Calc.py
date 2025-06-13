# print("Simple Calculator")

# choice = input("Press Enter to continue or 'e' to exit: ")

# while True:
#     if choice == "e":
#         print("Exiting the calculator.")
#         break
#     elif choice == "":
#         num_1 = int(input("Enter the first number: "))
#         operation = input("Enter the operation (+, -, *, /): ")
#         num_2 = int(input("Enter the second number: "))
#         if operation == "+":
#             print("Answer: ", str(num_1 + num_2))
#         elif operation == "-":
#             print("Answer: ", str(num_1 - num_2))
#         elif operation == "*":
#             print("Answer: ", str(num_1 * num_2))
#         elif operation == "/":
#             if num_2 != 0:
#                 print("Answer: ", str(num_1 / num_2))
#             else:
#                 print("Error: Division by zero")
#         else:
#             print("Error: Invalid operation")

# print("Simple Calculator")

# while True:
#     choice = input("\nPress Enter to continue or 'e' to exit: ").strip().lower()
    
#     if choice == "e":
#         print("Exiting the calculator. Goodbye!")
#         break
#     elif choice == "":
#         try:
#             num_1 = int(input("Enter the first number: "))
#             operation = input("Enter the operation (+, -, *, /): ")
#             num_2 = int(input("Enter the second number: "))

#             if operation == "+":
#                 print("Answer:", num_1 + num_2)
#             elif operation == "-":
#                 print("Answer:", num_1 - num_2)
#             elif operation == "*":
#                 print("Answer:", num_1 * num_2)
#             elif operation == "/":
#                 if num_2 != 0:
#                     print("Answer:", round(num_1 / num_2, 2))
#                 else:
#                     print("Error: Division by zero.")
#             else:
#                 print("Error: Invalid operation. Please use +, -, *, or /.")
#         except ValueError:
#             print("Error: Please enter valid numbers.")
#     else:
#         print("Invalid input. Press Enter to calculate or 'e' to exit.")

print("Simple Calculator")

history = []

while True:
    choice = input("\nPress Enter to continue, 'h' for history, or 'e' to exit: ").strip().lower()
    
    if choice == "e":
        print("Exiting the calculator. Goodbye!")
        break
    elif choice == "h":
        print("\nCalculation History:")
        if history:
            for record in history:
                print(record)
        else:
            print("No calculations yet.")
    elif choice == "":
        try:
            num_1 = int(input("Enter the first number: "))
            operation = input("Enter the operation (+, -, *, /): ").strip()
            num_2 = int(input("Enter the second number: "))

            if operation == "+":
                result = num_1 + num_2
            elif operation == "-":
                result = num_1 - num_2
            elif operation == "*":
                result = num_1 * num_2
            elif operation == "/":
                if num_2 == 0:
                    print("Error: Division by zero.")
                    continue
                result = round(num_1 / num_2, 2)
            else:
                print("Error: Invalid operation. Please use +, -, *, or /.")
                continue

            record = f"{num_1} {operation} {num_2} = {result}"
            history.append(record)
            print("Answer:", result)

        except ValueError:
            print("Error: Please enter valid integer numbers.")
    else:
        print("Invalid input. Try again.")