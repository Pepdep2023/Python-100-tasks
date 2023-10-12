temperature = int(input("Enter the temperature: "))
if temperature >= 100:
    print("Boiling")
elif temperature >= 32 and temperature <= 99:
    print("Liquid")
elif temperature < 32:
    print("Freezing")
    