print("=== Detective Mystery ===")

print("\nA valuable diamond has been stolen.")
print("There are three suspects:")
print("1. Alex")
print("2. Sam")
print("3. Jordan")

clues = []

while True:
    print("\n1. Search the office")
    print("2. Check security cameras")
    print("3. Interview Alex")
    print("4. Interview Sam")
    print("5. Interview Jordan")
    print("6. Make accusation")

    choice = input("Choose: ")

    if choice == "1":
        print("You found a glove.")
        clues.append("glove")

    elif choice == "2":
        print("You saw Jordan near the diamond room.")
        clues.append("camera")

    elif choice == "3":
        print("Alex says he was at home.")

    elif choice == "4":
        print("Sam says he was working late.")

    elif choice == "5":
        print("Jordan seems nervous.")

    elif choice == "6":
        suspect = input("Who is the thief? ")

        if suspect.lower() == "jordan":
            print("\nCase solved! Jordan stole the diamond.")
        else:
            print("\nWrong accusation. The thief escaped.")

        break

    else:
        print("Invalid choice.")
