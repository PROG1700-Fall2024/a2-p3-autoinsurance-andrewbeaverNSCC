#Program 3 – Auto Insurance
#Write a program that computes monthly insurance according to the provided schedule. 

#Student #:     w0402993
#Student Name:  Andrew Beaver

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    print("Auto Insurance Calculator")

    gender = input("\nAre you 'Male' or 'Female': ").lower()

    age = int(input("Enter your age: "))

    vehiclePrice = float(input("Enter the purchase price of the vehicle: "))

    if gender == "male":
        if age >= 15 and age < 25:
            insPrice = (vehiclePrice * 0.25) / 12
        elif age >= 25 and age < 40:
            insPrice = (vehiclePrice * 0.17) / 12
        elif age >= 40 and age < 70:
            insPrice = (vehiclePrice * 0.1) / 12
    if gender == "female":
        if age >= 15 and age < 25:
            insPrice = (vehiclePrice * 0.2) / 12
        elif age >= 25 and age < 40:
            insPrice = (vehiclePrice * 0.15) / 12
        elif age >= 40 and age < 70:
            insPrice = (vehiclePrice * 0.1) / 12

    print("\nYour monthly insurance will be ${0:.2f}".format(insPrice))

    # YOUR CODE ENDS HERE

main()