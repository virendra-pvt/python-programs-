age=int(input("\nEnter Your Age: "))
has_id_card=input("Do You Have ID Card? (yes/no): ").lower()
if age >= 18 and has_id_card == "yes":
    print("You are eligible to vote.")
if age < 18 and has_id_card == "yes":
    print("You are not eligible to vote.")
