#Program 3 – Auto Insurance
#Write a program that computes monthly insurance according to the provided schedule. 

#Student #:     w0402993
#Student Name:  Andrew Beaver

def main():
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

    #Display price
    print("\nYour monthly insurance will be ${0:.2f}".format(insPrice))

main()