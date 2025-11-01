#13. Write a Program that takes tempareture and humidity as input from the user and checks if values are provided. 

temperature =input("Enter the temperature: ")
humidity =input("Enter the humidity: ")

# Check if both values are provided
if temperature== "":
    print("Temperature not provided.")
else:
    print("Temperature provided:", temperature)

if humidity== "":
    print("Humidity not provided.")
else:
    print("Humidity provided:",humidity)