#Program 3 – Auto Insurance
#Write a program that computes monthly insurance according to the provided schedule. 

#Student #:     w0402993
#Student Name:  Andrew Beaver

def main():
    #Establish variables for insurance rates
    maleAge1 = 0.25
    maleAge2 = 0.17
    maleAge3 = 0.1

    femaleAge1 = 0.2
    femaleAge2 = 0.15
    femaleAge3 = 0.1

    #Display welcome message
    print("Auto Insurance Calculator")

    #Ask user if they are male or female
    gender = input("\nAre you 'Male' or 'Female': ").lower()

    #Ask user their age
    age = int(input("Enter your age: "))

    #Ask user the price of their vehicle
    vehiclePrice = float(input("Enter the purchase price of the vehicle: "))

    #Establish the insurance price based on male or female, then age, then vehicle price times rate divided by months (12)
    if gender == "male":
        if age >= 15 and age < 25:
            insPrice = (vehiclePrice * maleAge1) / 12
        elif age >= 25 and age < 40:
            insPrice = (vehiclePrice * maleAge2) / 12
        elif age >= 40 and age < 70:
            insPrice = (vehiclePrice * maleAge3) / 12
    if gender == "female":
        if age >= 15 and age < 25:
            insPrice = (vehiclePrice * femaleAge1) / 12
        elif age >= 25 and age < 40:
            insPrice = (vehiclePrice * femaleAge2) / 12
        elif age >= 40 and age < 70:
            insPrice = (vehiclePrice * femaleAge3) / 12

    #Display price
    print("\nYour monthly insurance will be ${0:.2f}".format(insPrice))

main()