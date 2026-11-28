
print("===== WELCOME TO GUJARAT RESTAURANT =====")
print("========== MENU ==========")
print("1. Pizza       - Rs. 150")
print("2. Burger      - Rs. 100")
print("3. Sandwich    - Rs. 80")
print("4. Pasta       - Rs. 120")
print("5. Dosa        - Rs. 160")

choice = int(input("\nEnter your choice (1-5): "))

if choice == 1:
    print("You ordered Pizza.")
    print("Bill Amount = Rs. 150")

elif choice == 2:
    print("You ordered Burger.")
    print("Bill Amount = Rs. 100")

elif choice == 3:
    print("You ordered Sandwich.")
    print("Bill Amount = Rs. 80")

elif choice == 4:
    print("You ordered Pasta.")
    print("Bill Amount = Rs. 120")

elif choice == 5:
    print("You ordered Dosa.")
    print("Bill Amount = Rs. 60")

else:
    print("Invalid choice! Please select from 1 to 5.")

print("Thank you for visiting our restaurant!")
